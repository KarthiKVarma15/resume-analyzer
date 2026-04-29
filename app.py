import streamlit as st
from utils import extract_text_from_pdf, extract_skills, match_job_role

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    skills = extract_skills(text)

    st.subheader("Extracted Skills:")
    st.write(skills)

    results = match_job_role(skills)

    st.subheader("Job Match Scores:")
    for role, score in results.items():
        st.write(f"{role}: {score}%")

    overall_score = sum(results.values()) / len(results)
    st.subheader(f"Overall Resume Score: {overall_score:.2f}%")