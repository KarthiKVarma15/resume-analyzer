from PyPDF2 import PdfReader
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python", "java", "c++", "sql", "machine learning",
    "deep learning", "nlp", "data science", "aws",
    "docker", "html", "css", "javascript"
]

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def extract_skills(text):
    doc = nlp(text)
    found_skills = []

    for token in doc:
        if token.text.lower() in SKILLS:
            found_skills.append(token.text.lower())

    return list(set(found_skills))

JOB_ROLES = {
    "Data Scientist": ["python", "machine learning", "data science", "sql"],
    "Web Developer": ["html", "css", "javascript"],
    "DevOps Engineer": ["docker", "aws", "linux"]
}

def match_job_role(user_skills):
    results = {}

    for role, skills in JOB_ROLES.items():
        match_count = len(set(user_skills) & set(skills))
        score = (match_count / len(skills)) * 100
        results[role] = round(score, 2)

    return results