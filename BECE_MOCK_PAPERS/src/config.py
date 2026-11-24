from pathlib import Path
from typing import Dict, List

# Base Directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
HARVESTED_DIR = DATA_DIR / "harvested"
METADATA_DIR = DATA_DIR / "metadata"
STORAGE_DIR = DATA_DIR / "crawlee_storage"
DATABASE_PATH = METADATA_DIR / "catalog.db"
CATALOG_JSON_PATH = METADATA_DIR / "catalog.json"

# Supported target file extensions
TARGET_EXTENSIONS = [".pdf", ".docx", ".doc", ".txt"]

# Subject Taxonomy
SUBJECTS = {
    "Mathematics": [
        "math", "mathematics", "maths", "core maths", "general maths",
        "bece maths", "jhs maths", "arithmetic"
    ],
    "Computing_ICT": [
        "computing", "ict", "information and communication technology",
        "computer studies", "bece computing", "ict past questions", "ict mock"
    ],
    "CAD": [
        "creative arts", "creative arts and design", "cad",
        "visual arts", "performing arts", "dance", "drama", "music",
        "drawing and shading", "pattern making", "casting", "weaving",
        "creativity", "artistic expression", "bece cad"
    ],
    "General_Unclassified": [
        "mock", "bece", "past questions", "pasco", "exam", "marking scheme"
    ]
}

# High-Priority Ghana Educational Portals & Exam Repositories
TARGET_DOMAINS: List[str] = [
    "colemanpublications.com",
    "waecgh.org",
    "ghana.waecdirect.org",
    "ghstudents.com",
    "ghlearner.com",
    "ghanaeducation.org",
    "mickinetsystems.com",
    "pbpagezlimited.com",
    "becezone.com",
    "kuulchat.com",
    "bestbrainexams.com",
    "gbassessment.com",
    "skulmanager.com",
    "teachersghana.com",
    "edunewsgh.com",
    "geshub.org",
    "becepastquestions.com"
]

# Primary Seed URLs across targets
SEED_URLS: List[str] = [
    "https://colemanpublications.com/education/",
    "https://waecgh.org/bece-guidelines-scheme-and-structure",
    "https://ghstudents.com/bece-past-questions-and-answers/",
    "https://ghlearner.com/past-questions/bece",
    "https://ghlearner.com/mock-exams",
    "https://ghanaeducation.org/category/bece-questions/",
    "https://ghanaeducation.org/category/mock-papers/",
    "https://mickinetsystems.com/bece-past-questions/",
    "https://mickinetsystems.com/gbat-mock-questions/",
    "https://pbpagezlimited.com/bece-mock-questions/",
    "https://becezone.com/bece-past-questions/",
    "https://kuulchat.com/bece-questions",
    "https://bestbrainexams.com/downloads/",
    "https://gbassessment.com/resources/",
    # --- Computing / ICT multi-year (gap: bank is 2024-only) ---
    "https://ghlearner.com/bece/computing/exams",
    "https://passco.com.gh/bece-past-questions/ict",
    "https://mickinetsystems.com/bece-ict-past-questions/",
    "https://ghanaeducation.org/category/ict-questions/",
    "https://becezone.com/ict/",
    # --- CAD / Creative Arts and Design ---
    "https://ghlearner.com/bece/creative-arts-and-design/exams",
    "https://ghanaeducation.org/category/creative-arts/",
    "https://passco.com.gh/bece-past-questions/creative-arts",
    # --- Maths 2013-2025 gap ---
    "https://passco.com.gh/bece-past-questions/mathematics",
    "https://ghlearner.com/bece/mathematics/exams",
    "https://mickinetsystems.com/bece-mathematics-past-questions/",
]

# Common Examination Terms for Relevance Scoring
EXAM_KEYWORDS: List[str] = [
    "bece", "mock", "past questions", "pasco", "marking scheme",
    "chief examiner", "trial questions", "sample questions", "waec", "ges",
    "common core", "ccp", "standards-based"
]

# Dork Search Query Templates for Deep Web Discovery
DORK_QUERIES: List[str] = [
    'site:ghlearner.com (filetype:pdf OR filetype:docx) ("bece" OR "mock")',
    'site:passco.com.gh (filetype:pdf OR filetype:docx) ("bece" OR "mock")',
    'site:ghanaeducation.org "download" ("bece" OR "mock") (filetype:pdf OR filetype:docx)',
    'site:mickinetsystems.com ("bece" OR "mock") (filetype:pdf OR filetype:docx)',
    'site:pbpagezlimited.com ("bece" OR "mock") (filetype:pdf OR filetype:docx)',
    'filetype:pdf "BECE" "mock" "computing" ghana',
    'filetype:pdf "BECE" "mock" "mathematics" ghana',
    'filetype:pdf "BECE" "mock" "creative arts and design" ghana',
    'filetype:pdf "BECE" "mock" "creative arts" ghana',
    'filetype:docx "BECE" "mock" ("maths" OR "computing" OR "creative arts")',
    'filetype:pdf "best brain" "mock" "bece" questions',
    'filetype:pdf "gbat" "mock" "bece" marking scheme',
    'site:drive.google.com/file/d/ ("BECE" OR "mock") ("maths" OR "computing" OR "creative arts")',
    # --- Computing / ICT multi-year harvest ---
    'filetype:pdf "BECE" "ICT" "past questions" ghana',
    'filetype:pdf "BECE" "computing" "2018" OR "2019" OR "2020" OR "2021" OR "2022" OR "2023"',
    'filetype:pdf "BECE" "computing" "Paper 1" "Paper 2" answers',
    'site:ghlearner.com (ICT OR computing) (bece OR mock) filetype:pdf',
    'site:passco.com.gh (ICT OR computing) filetype:pdf',
    # --- CAD / Creative Arts and Design ---
    'filetype:pdf "BECE" "creative arts and design" mock 2024 OR 2025 OR 2026',
    'filetype:pdf "creative arts" "BECE" past questions ghana',
    'site:ghlearner.com "creative arts" bece filetype:pdf',
    # --- Maths 2013-2025 gap ---
    'filetype:pdf "BECE" "mathematics" "2018" OR "2019" OR "2020" OR "2021" past questions',
    'filetype:pdf "BECE" "mathematics" mock "2023" OR "2024" OR "2025" questions',
    'site:passco.com.gh mathematics BECE filetype:pdf',
    'site:ghlearner.com mathematics bece filetype:pdf',
    # --- 2026 season (super mocks, serial mocks, marking schemes) ---
    'filetype:pdf "BECE" "2026" ("computing" OR "ICT") (mock OR "super mock" OR "serial mock")',
    'filetype:pdf "BECE" "2026" "creative arts and design" mock questions',
    'filetype:pdf "2026" BECE "marking scheme" ("computing" OR "ICT" OR "creative arts")',
    'filetype:pdf "2026 mock" ("computing" OR "ICT") ghana junior high',
    'filetype:pdf "2026 mock" "creative arts and design" ghana',
    'filetype:pdf ("maths" OR "computing") "mock 1" OR "mock 2" OR "mock 3" "2026" BECE ghana',
    'site:becezone.com 2026 filetype:pdf',
    'site:ghanaeducation.org 2026 mock (filetype:pdf OR filetype:docx)',
    'filetype:pdf "BECE" "first mock" OR "second mock" OR "third mock" 2026',
]

# Crawler Settings
USER_AGENT: str = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

REQUEST_TIMEOUT_SECONDS: int = 30
MAX_CONCURRENT_REQUESTS: int = 10
MAX_DOWNLOAD_SIZE_BYTES: int = 150 * 1024 * 1024  # 150 MB safety limit
