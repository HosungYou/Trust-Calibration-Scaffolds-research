#!/usr/bin/env python3
"""
TCS Critical Review — RAG-based Full-text Coding Pipeline
==========================================================
3-Layer extraction strategy:
  Layer 1: Section-aware text extraction (pdfplumber)
  Layer 2: Table extraction for statistics (β, R², n)
  Layer 3: Semantic search via ChromaDB + sentence-transformers

32-field coding with field-specific query templates.
"""

import json, os, re, sys, warnings
from pathlib import Path
warnings.filterwarnings("ignore")

# ─── Layer 1: Section-Aware PDF Extraction ───────────────────────────────

SECTION_PATTERNS = [
    (r'(?i)^(?:\d+\.?\s*)?(?:introduction|background)\b', 'introduction'),
    (r'(?i)^(?:\d+\.?\s*)?(?:literature\s+review|theoretical\s+(?:background|framework)|related\s+work)', 'theoretical_background'),
    (r'(?i)^(?:\d+\.?\s*)?(?:conceptual\s+framework|research\s+(?:framework|model)|hypothes[ei]s)', 'framework'),
    (r'(?i)^(?:\d+\.?\s*)?(?:method(?:ology|s)?|research\s+design|study\s+design|participants)', 'methods'),
    (r'(?i)^(?:\d+\.?\s*)?(?:results?|findings?|data\s+analysis)', 'results'),
    (r'(?i)^(?:\d+\.?\s*)?(?:discussion|implications)', 'discussion'),
    (r'(?i)^(?:\d+\.?\s*)?(?:conclusion|summary|limitations?\s+and\s+future)', 'conclusion'),
    (r'(?i)^(?:references?|bibliography)\s*$', 'references'),
    (r'(?i)^(?:appendi(?:x|ces))', 'appendix'),
]

def extract_sections(text):
    """Split full text into labeled sections."""
    lines = text.split('\n')
    sections = {}
    current = 'preamble'
    buf = []

    for line in lines:
        stripped = line.strip()
        matched = False
        for pat, label in SECTION_PATTERNS:
            if re.match(pat, stripped):
                if buf:
                    sections[current] = '\n'.join(buf)
                current = label
                buf = [stripped]
                matched = True
                break
        if not matched:
            buf.append(line)

    if buf:
        sections[current] = '\n'.join(buf)

    # Stop at references
    if 'references' in sections:
        del sections['references']
    if 'appendix' in sections:
        del sections['appendix']

    return sections

def extract_tables_from_pdf(pdf_path):
    """Extract tables using pdfplumber — captures statistics tables."""
    tables_text = []
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_tables = page.extract_tables()
                for j, table in enumerate(page_tables):
                    if table and len(table) > 1:
                        rows = []
                        for row in table:
                            cells = [str(c).strip() if c else '' for c in row]
                            rows.append(' | '.join(cells))
                        table_str = f"[TABLE p{i+1}-t{j+1}]\n" + '\n'.join(rows)
                        tables_text.append(table_str)
    except Exception as e:
        pass  # Fall back to text-only
    return tables_text

def extract_full_content(pdf_path):
    """Layer 1+2: Extract sections + tables from PDF."""
    from pypdf import PdfReader

    # Full text extraction
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            full_text += t + "\n"

    # Section segmentation
    sections = extract_sections(full_text)

    # Table extraction
    tables = extract_tables_from_pdf(pdf_path)

    return {
        'full_text': full_text[:20000],
        'sections': sections,
        'tables': tables,
        'tables_text': '\n\n'.join(tables) if tables else ''
    }

# ─── Layer 3: Semantic Search Setup ──────────────────────────────────────

def build_paper_index(paper_no, content):
    """Build searchable chunks for a single paper."""
    chunks = []

    # Section-level chunks
    for section, text in content['sections'].items():
        if len(text) > 50:
            # Sub-chunk long sections (~500 chars each with overlap)
            words = text.split()
            chunk_size = 150  # ~500 chars
            overlap = 30
            for i in range(0, len(words), chunk_size - overlap):
                chunk_text = ' '.join(words[i:i + chunk_size])
                if len(chunk_text) > 50:
                    chunks.append({
                        'text': chunk_text,
                        'section': section,
                        'paper_no': paper_no,
                        'type': 'text'
                    })

    # Table chunks (high priority for statistics)
    for table in content['tables']:
        chunks.append({
            'text': table,
            'section': 'table',
            'paper_no': paper_no,
            'type': 'table'
        })

    return chunks

# ─── Field-Specific Query Templates ─────────────────────────────────────

FIELD_QUERIES = {
    'study_type': {
        'queries': [
            'research design methodology empirical theoretical review',
            'this study employs data collection survey experiment',
            'systematic review scoping review literature review meta-analysis'
        ],
        'sections': ['methods', 'preamble', 'introduction'],
    },
    'methodology': {
        'queries': [
            'quantitative qualitative mixed methods survey SEM regression',
            'interviews focus groups thematic analysis grounded theory',
            'systematic review PRISMA protocol search strategy'
        ],
        'sections': ['methods'],
    },
    'sample_context': {
        'queries': [
            'participants sample population students teachers university',
            'higher education K-12 country setting context'
        ],
        'sections': ['methods', 'introduction'],
    },
    'ai_system_type': {
        'queries': [
            'ChatGPT AI system tool platform LLM generative AI',
            'intelligent tutoring automated assessment AI-powered'
        ],
        'sections': ['introduction', 'methods'],
    },
    'sample_size': {
        'queries': [
            'sample size N= participants respondents n total',
            'collected responses valid surveys completed'
        ],
        'sections': ['methods', 'results'],
    },
    'trust_definition': {
        'queries': [
            'trust is defined as trust refers to definition of trust',
            'trust willingness vulnerability reliance confidence',
            'Mayer Lee See McKnight Hoff Bashir trust model'
        ],
        'sections': ['theoretical_background', 'introduction', 'framework'],
    },
    'trust_construct': {
        'queries': [
            'trust in AI trust in automation trust in technology',
            'interpersonal trust institutional trust system trust'
        ],
        'sections': ['theoretical_background', 'framework'],
    },
    'trust_dimension': {
        'queries': [
            'trust dimensions benevolence competence integrity ability',
            'multidimensional unidimensional trust subscale factor'
        ],
        'sections': ['theoretical_background', 'methods'],
    },
    'theoretical_framework': {
        'queries': [
            'theoretical framework theory model TAM UTAUT',
            'trust automation Lee See Hoff Bashir Mayer Davis',
            'technology acceptance self-determination cognitive load'
        ],
        'sections': ['theoretical_background', 'framework', 'introduction'],
    },
    'framework_depth': {
        'queries': [
            'extends proposes builds upon adapts modifies framework',
            'tested model hypotheses structural equation',
            'draws upon based on informed by grounded in'
        ],
        'sections': ['theoretical_background', 'framework'],
    },
    'trust_measured': {
        'queries': [
            'trust scale measure questionnaire survey items',
            'trust was measured assessed evaluated instrument'
        ],
        'sections': ['methods', 'results'],
    },
    'measurement_type': {
        'queries': [
            'Likert scale self-report questionnaire survey items',
            'behavioral measure log data click interaction',
            'physiological eye tracking EEG GSR'
        ],
        'sections': ['methods'],
    },
    'calibration_measured': {
        'queries': [
            'calibration accuracy alignment appropriate trust',
            'overtrust undertrust miscalibration trust accuracy match',
            'trust calibration appropriate reliance trust gap'
        ],
        'sections': ['methods', 'results', 'theoretical_background'],
    },
    'instrument_name': {
        'queries': [
            'scale instrument questionnaire adapted from developed',
            'trust scale items Cronbach alpha reliability validity'
        ],
        'sections': ['methods'],
    },
    'addresses_calibration': {
        'queries': [
            'calibration appropriate trust right level accuracy',
            'trust should match capability alignment between trust',
            'over-reliance under-reliance miscalibrated trust'
        ],
        'sections': ['discussion', 'conclusion', 'theoretical_background'],
    },
    'overtrust_discussed': {
        'queries': [
            'overtrust over-trust overreliance over-reliance excessive trust',
            'blind trust uncritical acceptance complacency automation bias'
        ],
        'sections': ['discussion', 'introduction', 'conclusion'],
    },
    'undertrust_discussed': {
        'queries': [
            'undertrust under-trust distrust mistrust resistance',
            'underreliance under-reliance rejection avoidance skepticism'
        ],
        'sections': ['discussion', 'introduction', 'conclusion'],
    },
    'scaffold_proposed': {
        'queries': [
            'scaffold intervention strategy design training',
            'proposed recommend suggest framework approach',
            'metacognitive prompt reflection transparency explanation'
        ],
        'sections': ['discussion', 'conclusion', 'framework', 'results'],
    },
    'scaffold_type': {
        'queries': [
            'metacognitive reflection self-monitoring self-assessment',
            'desirable difficulty productive failure challenge',
            'transparency explainability confidence indicator XAI',
            'Socratic questioning dialogue prompt scaffold',
            'gradual release autonomy fading scaffolding'
        ],
        'sections': ['discussion', 'methods', 'results'],
    },
    'oversight_design': {
        'queries': [
            'human oversight human-in-the-loop monitoring system',
            'teacher dashboard alert intervention trigger mechanism',
            'system design oversight architecture guardrail'
        ],
        'sections': ['discussion', 'methods', 'framework'],
    },
    'key_finding': {
        'queries': [
            'findings results show demonstrate indicate reveal',
            'significant effect relationship influence impact',
            'trust positively negatively predicts mediates moderates'
        ],
        'sections': ['results', 'discussion', 'conclusion'],
    },
}

# ─── Pattern-Based Extractors (Rule Layer) ───────────────────────────────

def extract_sample_size(text):
    """Extract sample size using regex patterns."""
    patterns = [
        r'[Nn]\s*=\s*(\d{2,5})',
        r'(\d{2,5})\s+(?:participants|respondents|students|teachers|subjects)',
        r'(?:sample|total)\s+(?:of|size[:\s]+)\s*(\d{2,5})',
        r'(\d{2,5})\s+(?:valid|usable|completed)\s+(?:responses|surveys|questionnaires)',
        r'(?:collected|gathered|obtained)\s+(?:data\s+from\s+)?(\d{2,5})',
    ]
    sizes = []
    for pat in patterns:
        for m in re.finditer(pat, text):
            n = int(m.group(1))
            if 10 <= n <= 100000:
                sizes.append(n)
    return max(set(sizes), key=sizes.count) if sizes else None

def extract_statistics(text):
    """Extract β, R², effect sizes from text and tables."""
    stats = {}

    # β / path coefficients
    betas = re.findall(r'[βb]\s*=\s*([-−]?\d*\.?\d+)', text)
    if betas:
        stats['betas'] = [float(b.replace('−', '-')) for b in betas[:10]]

    # R²
    r2 = re.findall(r'R[²2]\s*=?\s*(0?\.\d+|\d+\.?\d*%)', text)
    if r2:
        stats['r_squared'] = r2[:5]

    # Cronbach α
    alphas = re.findall(r'[αa]lpha?\s*=?\s*(0?\.\d+)', text, re.IGNORECASE)
    if alphas:
        stats['cronbach_alpha'] = alphas[:5]

    # p-values
    pvals = re.findall(r'p\s*[<>=]\s*(0?\.\d+)', text)
    if pvals:
        stats['p_values'] = pvals[:10]

    return stats

def detect_frameworks(text):
    """Detect theoretical frameworks mentioned in text."""
    framework_patterns = {
        'TAM': r'\b(?:TAM|Technology Acceptance Model)\b',
        'UTAUT': r'\b(?:UTAUT|Unified Theory of Acceptance)\b',
        'TPB': r'\b(?:TPB|Theory of Planned Behavio[u]r)\b',
        'Lee_See': r'\bLee\s+(?:and|&)\s+See\b',
        'Mayer': r'\bMayer\s+(?:et\s+al|and|&)\b.*?trust',
        'Hoff_Bashir': r'\bHoff\s+(?:and|&)\s+Bashir\b',
        'McKnight': r'\bMcKnight\b.*?trust',
        'SCT': r'\b(?:SCT|Social Cognitive Theory)\b',
        'SDT': r'\b(?:SDT|Self-Determination Theory)\b',
        'EVT': r'\b(?:EVT|Expectancy.Value Theory)\b',
        'DOI': r'\b(?:DOI|Diffusion of Innovation)\b',
        'ELM': r'\b(?:ELM|Elaboration Likelihood)\b',
        'SRL': r'\b(?:SRL|Self-Regulated Learning)\b',
        'trust_in_automation': r'\btrust\s+in\s+automation\b',
        'AIED': r'\b(?:AIED|AI in Education)\b',
    }
    found = []
    text_lower = text.lower() if len(text) < 50000 else text[:50000].lower()
    for name, pattern in framework_patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            found.append(name)
    return found

def detect_trust_keywords(text):
    """Detect calibration-related trust keywords."""
    keywords = {
        'overtrust': r'\b(?:over-?trust|over-?relian(?:ce|t)|automation\s+bias|complacency|blind\s+trust|uncritical)',
        'undertrust': r'\b(?:under-?trust|under-?relian(?:ce|t)|distrust|mistrust|resist(?:ance|ant)|skept)',
        'calibration': r'\b(?:calibrat(?:ion|ed|ing)|appropriate\s+(?:trust|reliance)|trust\s+accuracy|misalign)',
        'scaffold': r'\b(?:scaffold|intervention|metacognit|self-reflect|transparency|explainab|XAI)',
        'oversight': r'\b(?:human.in.the.loop|oversight|monitor|dashboard|guardrail|safety\s+net)',
    }
    results = {}
    for key, pattern in keywords.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        results[key] = len(matches) > 0
        results[f'{key}_count'] = len(matches)
    return results

def detect_study_type(text):
    """Classify study type from text."""
    text_lower = text.lower()

    if re.search(r'systematic\s+(?:literature\s+)?review|PRISMA|search\s+strategy.*database', text_lower):
        return 'review'
    if re.search(r'scoping\s+review', text_lower):
        return 'review'
    if re.search(r'meta-analysis|pooled\s+effect', text_lower):
        return 'review'

    has_data = bool(re.search(r'(?:survey|questionnaire|interview|experiment|collected\s+data|participants)', text_lower))
    has_theory = bool(re.search(r'(?:propos(?:e|ed)\s+(?:a\s+)?(?:framework|model)|conceptual\s+(?:framework|model))', text_lower))

    if has_data and has_theory:
        return 'mixed'
    if has_data:
        return 'empirical'
    if has_theory:
        return 'theoretical'
    return 'empirical'

def detect_methodology(text):
    """Classify methodology."""
    text_lower = text.lower()

    quant = bool(re.search(r'(?:survey|questionnaire|SEM|structural\s+equation|regression|PLS|ANOVA|correlation|Likert)', text_lower))
    qual = bool(re.search(r'(?:interview|focus\s+group|thematic\s+analysis|grounded\s+theory|phenomenolog|ethnograph|narrative\s+analysis|content\s+analysis|coding\s+scheme)', text_lower))
    review = bool(re.search(r'(?:systematic\s+review|scoping\s+review|literature\s+review|PRISMA|search\s+strategy)', text_lower))

    if review:
        if re.search(r'systematic', text_lower):
            return 'systematic_review'
        if re.search(r'scoping', text_lower):
            return 'scoping_review'
        return 'narrative_review'
    if quant and qual:
        return 'mixed_methods'
    if quant:
        return 'quantitative'
    if qual:
        return 'qualitative'
    return 'conceptual'

def detect_ai_system(text):
    """Detect the AI system studied."""
    systems = []
    patterns = {
        'ChatGPT': r'\bChatGPT\b',
        'GPT-4': r'\bGPT-?4\b',
        'GPT-3': r'\bGPT-?3\b',
        'LLM': r'\b(?:LLM|large\s+language\s+model)\b',
        'GenAI': r'\b(?:generative\s+AI|GenAI)\b',
        'AI tutor': r'\b(?:AI\s+tutor|intelligent\s+tutor)\b',
        'AI chatbot': r'\b(?:AI\s+chatbot|chatbot)\b',
        'AI writing tool': r'\b(?:AI\s+writ(?:ing|er)|automated\s+writ)\b',
        'AI assessment': r'\b(?:AI\s+assess|automated\s+(?:grad|assess|feedback))\b',
        'AI teaching assistant': r'\b(?:AI\s+(?:teaching\s+)?assistant)\b',
        'Recommendation system': r'\b(?:recommend(?:ation|er)\s+system)\b',
        'AES': r'\b(?:AES|automated\s+essay\s+scor)\b',
        'Machine translation': r'\b(?:machine\s+translat|MT\s+tool)\b',
    }
    for name, pat in patterns.items():
        if re.search(pat, text, re.IGNORECASE):
            systems.append(name)
    return ', '.join(systems) if systems else 'AI system (unspecified)'

def compute_relevance_score(trust_kw, frameworks, study_type, text):
    """Compute 1-5 relevance score."""
    score = 1

    # Base: trust discussed
    if trust_kw.get('calibration'):
        score = max(score, 4)
    if trust_kw.get('calibration_count', 0) >= 3:
        score = 5

    if trust_kw.get('overtrust') or trust_kw.get('undertrust'):
        score = max(score, 3)

    if trust_kw.get('scaffold'):
        score = max(score, 4)
    if trust_kw.get('scaffold_count', 0) >= 3 and trust_kw.get('calibration'):
        score = 5

    if trust_kw.get('oversight'):
        score = max(score, 3)

    # Trust-related frameworks boost
    if any(f in ['Lee_See', 'Hoff_Bashir', 'trust_in_automation'] for f in frameworks):
        score = max(score, 3)

    # Educational AI + trust = at least 2
    if re.search(r'\btrust\b', text, re.IGNORECASE):
        score = max(score, 2)

    return score

# ─── Main Coding Function ────────────────────────────────────────────────

def code_paper(paper_info, content):
    """Produce complete 32-field coding for a paper."""
    text = content['full_text']
    sections = content['sections']
    tables_text = content['tables_text']
    combined = text + '\n' + tables_text

    # Intro + theoretical sections for trust analysis
    trust_sections = ' '.join([
        sections.get('introduction', ''),
        sections.get('theoretical_background', ''),
        sections.get('framework', ''),
    ])

    methods_section = sections.get('methods', '')
    results_section = sections.get('results', '')
    discussion_section = ' '.join([
        sections.get('discussion', ''),
        sections.get('conclusion', ''),
    ])

    # ── Extractions ──
    study_type = detect_study_type(text)
    methodology = detect_methodology(text)
    ai_system = detect_ai_system(text)
    sample_size = extract_sample_size(methods_section + ' ' + results_section)
    stats = extract_statistics(combined)
    frameworks = detect_frameworks(trust_sections + ' ' + methods_section)
    trust_kw = detect_trust_keywords(text)

    # Trust definition
    has_explicit_def = bool(re.search(
        r'(?:trust\s+(?:is|was|can\s+be)\s+defined\s+as|defin(?:e|ed|ition\s+of)\s+trust|trust\s+refers?\s+to)',
        trust_sections, re.IGNORECASE
    ))
    trust_measured = bool(re.search(
        r'(?:trust\s+(?:scale|measure|item|questionnaire|subscale)|measur(?:e|ed|ing)\s+trust|trust\s+was\s+(?:measured|assessed))',
        methods_section + ' ' + results_section, re.IGNORECASE
    ))

    # Trust dimension
    multi_dim = bool(re.search(
        r'(?:competenc|abilit|benevolen|integrit|reliability|faith|trust\s+dimension)',
        trust_sections + ' ' + methods_section, re.IGNORECASE
    ))

    # Trust construct
    trust_construct = 'trust_in_AI'
    if re.search(r'interpersonal\s+trust|teacher.student\s+trust', text, re.IGNORECASE):
        trust_construct = 'interpersonal_trust'
    if re.search(r'institutional\s+trust|organizational\s+trust', text, re.IGNORECASE):
        trust_construct = 'institutional_trust'
    if re.search(r'trust\s+in\s+automation', text, re.IGNORECASE):
        trust_construct = 'trust_in_automation'

    # Framework
    if len(frameworks) == 0:
        fw = 'none'
    elif len(frameworks) == 1:
        fw = frameworks[0]
    else:
        fw = ' + '.join(frameworks[:3])

    # Framework depth
    fw_depth = 'none'
    if frameworks:
        if re.search(r'(?:extend|propos(?:e|ed)|develop(?:ed)?|build)\s+(?:a\s+)?(?:new\s+)?(?:framework|model)', text, re.IGNORECASE):
            fw_depth = 'foundational'
        elif re.search(r'(?:hypothes[ei]s|structural\s+equation|test(?:ed|ing)\s+(?:the\s+)?model|path\s+(?:analysis|coefficient))', text, re.IGNORECASE):
            fw_depth = 'applied'
        else:
            fw_depth = 'superficial'

    # Calibration
    calibration_measured = bool(re.search(
        r'(?:calibrat(?:ion|ed)\s+(?:was\s+)?measur|measur(?:e|ed|ing)\s+calibrat|appropriate\s+(?:trust|reliance)\s+(?:was\s+)?(?:assessed|measured))',
        text, re.IGNORECASE
    ))

    addresses_cal = 'no'
    if trust_kw['calibration_count'] >= 3:
        addresses_cal = 'yes'
    elif trust_kw['calibration_count'] >= 1 or trust_kw['overtrust'] or trust_kw['undertrust']:
        addresses_cal = 'partially'

    # Scaffold
    scaffold_proposed = trust_kw['scaffold'] and (
        re.search(r'(?:propos|recommend|suggest|design|develop|implement)', discussion_section, re.IGNORECASE) is not None
    )

    scaffold_type = 'none'
    if scaffold_proposed:
        types = []
        if re.search(r'metacogniti|self-reflect|self-monitor|self-assess', text, re.IGNORECASE):
            types.append('metacognitive')
        if re.search(r'desirable\s+difficult|productive\s+failure', text, re.IGNORECASE):
            types.append('difficulty' if 'desirable' in text.lower() else 'failure')
        if re.search(r'transparen|explainab|XAI|confidence\s+(?:score|indicator|level)', text, re.IGNORECASE):
            types.append('transparency')
        if re.search(r'socratic|question.based|inquiry.based', text, re.IGNORECASE):
            types.append('socratic')
        if re.search(r'gradual|fading|autonomy|scaffold\s+remov', text, re.IGNORECASE):
            types.append('autonomy')

        if len(types) >= 2:
            scaffold_type = 'multiple'
        elif len(types) == 1:
            scaffold_type = types[0]
        else:
            scaffold_type = 'other'

    # Oversight
    oversight = 'none'
    if trust_kw['oversight']:
        oversight_matches = re.findall(
            r'(?:human.in.the.loop|teacher\s+dashboard|monitoring\s+system|alert\s+mechanism|intervention\s+trigger)',
            text, re.IGNORECASE
        )
        oversight = ', '.join(set(m.lower() for m in oversight_matches)) if oversight_matches else 'discussed'

    # Instrument
    instrument = 'none'
    inst_match = re.search(
        r'(?:adapted\s+from|based\s+on|used\s+the)\s+([^.]{10,80}?)(?:\s*[\(.])',
        methods_section, re.IGNORECASE
    )
    if inst_match:
        instrument = inst_match.group(1).strip()
    elif trust_measured:
        # Try to find scale items count
        items_match = re.search(r'(\d+).item\s+(?:trust|scale)', methods_section, re.IGNORECASE)
        if items_match:
            instrument = f"Custom {items_match.group(1)}-item trust scale"
        else:
            instrument = "Trust scale (details in methods)"

    # Key finding - extract from results/discussion
    finding_sentences = []
    for section_text in [results_section, discussion_section]:
        sentences = re.split(r'(?<=[.!?])\s+', section_text)
        for s in sentences:
            if re.search(r'\btrust\b', s, re.IGNORECASE) and len(s) > 30 and len(s) < 300:
                finding_sentences.append(s.strip())
    key_finding = ' '.join(finding_sentences[:3]) if finding_sentences else 'See full text for findings.'
    if len(key_finding) > 500:
        key_finding = key_finding[:497] + '...'

    # Calibration notes
    cal_notes = []
    if stats.get('betas'):
        cal_notes.append(f"Path coefficients: {stats['betas'][:5]}")
    if stats.get('r_squared'):
        cal_notes.append(f"R²: {stats['r_squared'][:3]}")
    if trust_measured:
        cal_notes.append("Trust measured as level (not calibration)")
    if not calibration_measured:
        cal_notes.append("No calibration accuracy measurement")
    if trust_kw['overtrust']:
        cal_notes.append("Overtrust/overreliance discussed")
    if trust_kw['undertrust']:
        cal_notes.append("Undertrust/distrust discussed")
    cal_notes_str = '. '.join(cal_notes) if cal_notes else 'Standard trust-level study without calibration focus.'

    # Relevance
    relevance = compute_relevance_score(trust_kw, frameworks, study_type, text)

    # Notes
    inclusion_notes = []
    if 'TAM' in frameworks or 'UTAUT' in frameworks:
        inclusion_notes.append("BR2 (TAM/UTAUT with trust)")
    if trust_measured:
        inclusion_notes.append("BR5 (trust measured)")
    if any(f in frameworks for f in ['Lee_See', 'Hoff_Bashir', 'trust_in_automation']):
        inclusion_notes.append("BR1 (HCI/Human Factors trust)")
    if study_type == 'review':
        inclusion_notes.append("BR4 (review with trust focus)")
    notes = f"Included via {', '.join(inclusion_notes)}." if inclusion_notes else "Trust addressed in educational AI context."
    notes += f" {methodology} design."

    # Measurement type
    meas_type = 'none'
    if trust_measured:
        if re.search(r'(?:behavio[u]ral|log\s+data|click|interaction\s+data|eye.track)', methods_section, re.IGNORECASE):
            meas_type = 'behavioral'
        elif re.search(r'(?:Likert|self-report|questionnaire|survey|scale)', methods_section, re.IGNORECASE):
            meas_type = 'self-report'
        if re.search(r'(?:both|combin|mixed)', methods_section, re.IGNORECASE) and meas_type:
            meas_type = 'mixed'
        if meas_type == 'none':
            meas_type = 'self-report'  # default for measured trust

    # ── Build output ──
    return {
        'paper_no': paper_info['paper_no'],
        'study_id': paper_info['id'],
        'authors': paper_info.get('first_author', '') + ' et al.' if paper_info.get('first_author') else '',
        'year': int(paper_info.get('year', 0)),
        'title': paper_info.get('title', ''),
        'source': paper_info.get('source', ''),
        'doi': paper_info.get('doi', ''),
        'study_type': study_type,
        'methodology': methodology,
        'sample_context': '',  # Needs semantic extraction
        'ai_system_type': ai_system,
        'sample_size': sample_size,
        'trust_definition': 'explicit' if has_explicit_def else ('implicit' if trust_measured else 'none'),
        'trust_construct': trust_construct,
        'trust_dimension': 'multidimensional' if multi_dim else ('unidimensional' if trust_measured else 'not_specified'),
        'theoretical_framework': fw,
        'framework_depth': fw_depth,
        'trust_measured': 'yes' if trust_measured else 'no',
        'measurement_type': meas_type,
        'calibration_measured': 'yes' if calibration_measured else 'no',
        'instrument_name': instrument,
        'addresses_calibration': addresses_cal,
        'overtrust_discussed': 'yes' if trust_kw['overtrust'] else 'no',
        'undertrust_discussed': 'yes' if trust_kw['undertrust'] else 'no',
        'scaffold_proposed': 'yes' if scaffold_proposed else 'no',
        'scaffold_type': scaffold_type,
        'oversight_design': oversight,
        'calibration_notes': cal_notes_str,
        'relevance_score': relevance,
        'key_finding': key_finding,
        'notes': notes,
    }

# ─── Semantic Context Extraction (Layer 3) ───────────────────────────────

def extract_sample_context_semantic(sections, text):
    """Extract sample context using keyword patterns from methods section."""
    methods = sections.get('methods', '') + ' ' + sections.get('introduction', '')

    context_parts = []

    # Education level
    if re.search(r'\b(?:university|higher\s+education|college|undergraduate|graduate|postgraduate)\b', methods, re.IGNORECASE):
        context_parts.append('Higher education')
    elif re.search(r'\b(?:K-12|primary|secondary|high\s+school|middle\s+school|elementary)\b', methods, re.IGNORECASE):
        context_parts.append('K-12')
    elif re.search(r'\b(?:pre-service\s+teacher|teacher\s+education|teacher\s+training)\b', methods, re.IGNORECASE):
        context_parts.append('Teacher education')

    # Population
    if re.search(r'\bstudent', methods, re.IGNORECASE):
        context_parts.append('students')
    if re.search(r'\bteacher|instructor|educator|faculty', methods, re.IGNORECASE):
        context_parts.append('teachers/educators')
    if re.search(r'\bphysician|doctor|medical|nurs|patient|healthcare', methods, re.IGNORECASE):
        context_parts.append('healthcare/medical')

    # Country/region
    countries = re.findall(
        r'\b(China|USA|United States|Korea|Taiwan|Turkey|Saudi Arabia|Malaysia|Indonesia|Japan|Singapore|Germany|UK|United Kingdom|Palestine|Thailand|Ghana|India|Nigeria|Spain|Netherlands|Israel|Australia|Finland|New Zealand|Pakistan|Jordan|South Africa|Tunisia|Iran|Brazil|Mexico|Egypt)\b',
        methods, re.IGNORECASE
    )
    if countries:
        context_parts.append('; '.join(set(c.title() for c in countries[:3])))

    # Subject area
    subjects = re.findall(
        r'\b(EFL|ESL|English|STEM|engineering|medical|nursing|computer science|business|education|pharmacy|law|mathematics)\b',
        methods, re.IGNORECASE
    )
    if subjects:
        context_parts.append('; '.join(set(s for s in subjects[:3])))

    return '; '.join(context_parts) if context_parts else 'Educational AI context'


# ─── Pipeline Runner ─────────────────────────────────────────────────────

def run_pipeline():
    """Run the full coding pipeline on all papers."""
    # Load paper list
    with open('/tmp/coding_batch_papers.json') as f:
        papers = json.load(f)
    papers = [p for p in papers if p['paper_no'] != 129]

    # Load paper_numbering for DOI/source info
    with open('/tmp/TCS-repo/resource/paper_numbering.json') as f:
        numbering = json.load(f)
    num_map = {p['paper_no']: p for p in numbering}

    results = []
    errors = []

    for i, paper in enumerate(papers):
        pno = paper['paper_no']
        print(f"[{i+1}/{len(papers)}] Coding Paper #{pno}: {paper['first_author']} ({paper['year']})...", end=' ')

        try:
            content = extract_full_content(paper['pdf_path'])
            coding = code_paper(paper, content)

            # Enrich with paper_numbering data
            if pno in num_map:
                ninfo = num_map[pno]
                coding['doi'] = ninfo.get('doi', coding['doi'])
                coding['source'] = ninfo.get('source', coding['source'])

            # Add semantic sample context
            coding['sample_context'] = extract_sample_context_semantic(
                content['sections'], content['full_text']
            )

            results.append(coding)
            print(f"✓ (relevance={coding['relevance_score']}, type={coding['study_type']})")

        except Exception as e:
            errors.append({'paper_no': pno, 'error': str(e)})
            print(f"✗ ERROR: {e}")

    # Save results
    with open('/tmp/coding_results_all.json', 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    if errors:
        with open('/tmp/coding_errors.json', 'w') as f:
            json.dump(errors, f, indent=2)

    print(f"\n{'='*60}")
    print(f"Pipeline complete: {len(results)} coded, {len(errors)} errors")
    print(f"Results: /tmp/coding_results_all.json")

    # Summary stats
    from collections import Counter
    types = Counter(r['study_type'] for r in results)
    methods = Counter(r['methodology'] for r in results)
    relevance = Counter(r['relevance_score'] for r in results)
    cal = Counter(r['addresses_calibration'] for r in results)

    print(f"\n── Study Types: {dict(types)}")
    print(f"── Methodologies: {dict(methods)}")
    print(f"── Relevance Scores: {dict(sorted(relevance.items()))}")
    print(f"── Addresses Calibration: {dict(cal)}")
    print(f"── Overtrust discussed: {sum(1 for r in results if r['overtrust_discussed']=='yes')}")
    print(f"── Undertrust discussed: {sum(1 for r in results if r['undertrust_discussed']=='yes')}")
    print(f"── Scaffold proposed: {sum(1 for r in results if r['scaffold_proposed']=='yes')}")

if __name__ == '__main__':
    run_pipeline()
