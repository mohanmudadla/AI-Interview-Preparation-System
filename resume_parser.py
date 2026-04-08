import pdfplumber
import re

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_skills(text):
    skills_db = ["python", "java", "machine learning", "sql"]
    found_skills = []
    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills

def extract_email(text):
    email = re.findall(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+", text)
    return email[0] if email else None