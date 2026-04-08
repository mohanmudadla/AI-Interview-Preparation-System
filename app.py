import streamlit as st
from resume_parser import extract_text_from_pdf, extract_skills, extract_email
from question_generator import generate_questions
from evaluator import evaluate_answer, get_correct_answer

st.title("AI Interview Preparation System")

# Upload Resume
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if uploaded_file is not None:
    
    # Save file temporarily
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    # Extract data
    text = extract_text_from_pdf("temp_resume.pdf")
    skills = extract_skills(text)
    email = extract_email(text)

    st.subheader("Extracted Information")
    st.write("Email:", email)
    st.write("Skills:", skills)

    # Generate questions
    questions = generate_questions(skills)

    st.subheader("Interview Questions")

    user_answers = []

    for q in questions:
        answer = st.text_input(q)
        user_answers.append((q, answer))

    # Evaluate button
    if st.button("Evaluate Answers"):
        st.subheader("Results")

        for q, ans in user_answers:
            correct = get_correct_answer(q)
            score, feedback = evaluate_answer(ans, correct)

            st.write(f"Question: {q}")
            st.write(f"Score: {score}/10")
            st.write(f"Feedback: {feedback}")
            st.write("---")