#!/usr/bin/env python3
"""
Download OA PDFs using Unpaywall API (via DOI) and direct publisher links.
Falls back to Semantic Scholar and OpenAlex for PDF URLs.
"""

import json
import os
import re
import sys
import time
import requests
from urllib.parse import urlparse

PDF_DIR = os.path.join(os.path.dirname(__file__), '..', 'figures', 'pdfs')
OA_FILE = os.path.join(os.path.dirname(__file__), '..', 'resource', 'oa_papers_for_download.json')
RESULTS_FILE = os.path.join(os.path.dirname(__file__), '..', 'resource', 'oa_download_results.json')

EMAIL = "research@example.com"  # For Unpaywall API
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Academic Research PDF Downloader',
    'Accept': 'application/pdf,*/*'
}

def sanitize_filename(paper_id, doi):
    """Create safe filename from paper ID."""
    return f"{paper_id}.pdf"

def try_unpaywall(doi):
    """Try Unpaywall API for OA PDF URL."""
    try:
        url = f"https://api.unpaywall.org/v2/{doi}?email={EMAIL}"
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            best = data.get('best_oa_location', {})
            if best:
                pdf_url = best.get('url_for_pdf') or best.get('url')
                if pdf_url:
                    return pdf_url
            # Try all OA locations
            for loc in data.get('oa_locations', []):
                pdf_url = loc.get('url_for_pdf') or loc.get('url')
                if pdf_url:
                    return pdf_url
    except Exception as e:
        pass
    return None

def try_semantic_scholar(doi):
    """Try Semantic Scholar for open access PDF."""
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=openAccessPdf"
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            oa_pdf = data.get('openAccessPdf', {})
            if oa_pdf and oa_pdf.get('url'):
                return oa_pdf['url']
    except Exception:
        pass
    return None

def try_openalex(doi):
    """Try OpenAlex for open access PDF."""
    try:
        url = f"https://api.openalex.org/works/doi:{doi}"
        resp = requests.get(url, timeout=15, headers={'User-Agent': f'mailto:{EMAIL}'})
        if resp.status_code == 200:
            data = resp.json()
            # Check primary location
            primary = data.get('primary_location', {})
            if primary:
                pdf_url = primary.get('pdf_url')
                if pdf_url:
                    return pdf_url
            # Check all locations
            for loc in data.get('locations', []):
                pdf_url = loc.get('pdf_url')
                if pdf_url:
                    return pdf_url
    except Exception:
        pass
    return None

def try_doi_redirect(doi):
    """Follow DOI redirect and check for direct PDF link."""
    try:
        url = f"https://doi.org/{doi}"
        resp = requests.head(url, timeout=15, allow_redirects=True, headers=HEADERS)
        final_url = resp.url
        # Some publishers serve PDF directly or have /pdf suffix pattern
        if final_url.endswith('.pdf'):
            return final_url
        # Try common publisher PDF patterns
        parsed = urlparse(final_url)
        if 'mdpi.com' in parsed.hostname:
            return final_url.rstrip('/') + '/pdf'
        if 'springer' in parsed.hostname or 'nature.com' in parsed.hostname:
            pdf_url = final_url.replace('/article/', '/content/pdf/').rstrip('/') + '.pdf'
            return pdf_url
        if 'frontiersin.org' in parsed.hostname:
            return final_url.rstrip('/') + '/pdf' if '/full' not in final_url else final_url.replace('/full', '/pdf')
    except Exception:
        pass
    return None

def download_pdf(pdf_url, filepath):
    """Download PDF from URL to filepath."""
    try:
        resp = requests.get(pdf_url, timeout=60, headers=HEADERS, allow_redirects=True, stream=True)
        if resp.status_code == 200:
            content_type = resp.headers.get('Content-Type', '')
            # Check if we actually got a PDF
            first_bytes = b''
            chunks = []
            for chunk in resp.iter_content(chunk_size=8192):
                chunks.append(chunk)
                if not first_bytes:
                    first_bytes = chunk[:10]
                    # PDF magic bytes check
                    if not first_bytes.startswith(b'%PDF') and 'pdf' not in content_type.lower():
                        # Might be HTML landing page, not a PDF
                        if b'<html' in first_bytes.lower() or b'<!doctype' in first_bytes.lower():
                            return False, "Got HTML instead of PDF"

            with open(filepath, 'wb') as f:
                for chunk in chunks:
                    f.write(chunk)

            # Verify file size (PDFs should be > 10KB typically)
            fsize = os.path.getsize(filepath)
            if fsize < 5000:
                os.remove(filepath)
                return False, f"File too small ({fsize} bytes)"
            return True, f"OK ({fsize//1024}KB)"
        else:
            return False, f"HTTP {resp.status_code}"
    except Exception as e:
        return False, str(e)[:80]

def main():
    os.makedirs(PDF_DIR, exist_ok=True)

    with open(OA_FILE, 'r') as f:
        papers = json.load(f)

    print(f"Starting download of {len(papers)} OA papers...")

    results = []
    success = 0
    failed = 0
    skipped = 0

    for i, paper in enumerate(papers):
        pid = paper['id']
        doi = paper['doi'].strip()
        title_short = paper['title'][:60]
        filename = sanitize_filename(pid, doi)
        filepath = os.path.join(PDF_DIR, filename)

        # Skip if already downloaded
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"  [{i+1:3d}/74] SKIP (exists) {pid}")
            results.append({'id': pid, 'doi': doi, 'status': 'exists', 'file': filename})
            skipped += 1
            continue

        print(f"  [{i+1:3d}/74] {pid} | {title_short}...")

        # Try multiple sources
        pdf_url = None
        source = None

        # 1. Unpaywall
        pdf_url = try_unpaywall(doi)
        if pdf_url:
            source = 'unpaywall'

        # 2. Semantic Scholar
        if not pdf_url:
            time.sleep(0.5)
            pdf_url = try_semantic_scholar(doi)
            if pdf_url:
                source = 'semantic_scholar'

        # 3. OpenAlex
        if not pdf_url:
            time.sleep(0.5)
            pdf_url = try_openalex(doi)
            if pdf_url:
                source = 'openalex'

        # 4. DOI redirect patterns
        if not pdf_url:
            pdf_url = try_doi_redirect(doi)
            if pdf_url:
                source = 'doi_redirect'

        if pdf_url:
            ok, msg = download_pdf(pdf_url, filepath)
            if ok:
                print(f"          -> OK via {source} {msg}")
                results.append({'id': pid, 'doi': doi, 'status': 'downloaded', 'source': source, 'file': filename, 'url': pdf_url})
                success += 1
            else:
                print(f"          -> FAIL via {source}: {msg}")
                # Try next source if first failed
                fallback_ok = False
                for fallback_fn, fb_name in [(try_semantic_scholar, 'semantic_scholar'), (try_openalex, 'openalex')]:
                    if fb_name == source:
                        continue
                    time.sleep(0.5)
                    fb_url = fallback_fn(doi)
                    if fb_url and fb_url != pdf_url:
                        ok2, msg2 = download_pdf(fb_url, filepath)
                        if ok2:
                            print(f"          -> OK via {fb_name} (fallback) {msg2}")
                            results.append({'id': pid, 'doi': doi, 'status': 'downloaded', 'source': fb_name, 'file': filename, 'url': fb_url})
                            success += 1
                            fallback_ok = True
                            break
                if not fallback_ok:
                    results.append({'id': pid, 'doi': doi, 'status': 'failed', 'error': msg, 'tried_url': pdf_url})
                    failed += 1
        else:
            print(f"          -> NO URL found")
            results.append({'id': pid, 'doi': doi, 'status': 'no_url', 'error': 'No PDF URL from any source'})
            failed += 1

        # Rate limiting
        time.sleep(1)

    # Save results
    summary = {
        'total': len(papers),
        'downloaded': success,
        'failed': failed,
        'skipped': skipped,
        'results': results
    }
    with open(RESULTS_FILE, 'w') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*50}")
    print(f"DONE: {success} downloaded, {failed} failed, {skipped} skipped")
    print(f"Results saved to {RESULTS_FILE}")
    print(f"PDFs saved to {PDF_DIR}/")

if __name__ == '__main__':
    main()
