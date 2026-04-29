# AI Resume Analyzer 🚀

## 📌 Overview
AI Resume Analyzer is a web application that analyzes resumes using Natural Language Processing (NLP) and provides job role match scores along with skill improvement suggestions.

---

## 🚀 Features
- Extracts key skills from resume (PDF format)
- Matches resume with predefined job roles
- Calculates job compatibility score (%)
- Identifies missing skills for each role
- Provides overall resume score

---

## 🧠 Tech Stack
- Python
- Streamlit
- spaCy (NLP)
- Pandas
- Scikit-learn (basic usage)

---

## ⚙️ How It Works
1. Upload a resume in PDF format  
2. Extract text from the resume  
3. Identify skills using NLP techniques  
4. Compare extracted skills with job role requirements  
5. Generate match scores and missing skills  

---

## ▶️ Run Locally

Install dependencies:
```bash
pip install streamlit pandas scikit-learn spacy PyPDF2
python -m spacy download en_core_web_sm
