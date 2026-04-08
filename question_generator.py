def generate_questions(skills):
    
    questions_db = {
        "python": [
            "What is OOP in Python?",
            "What are decorators in Python?",
            "Explain list vs tuple."
        ],
        
        "machine learning": [
            "What is overfitting?",
            "Difference between supervised and unsupervised learning?",
            "What is a model?"
        ],
        
        "sql": [
            "What is JOIN?",
            "Difference between WHERE and HAVING?",
            "What is normalization?"
        ]
    }

    questions = []

    for skill in skills:
        if skill in questions_db:
            questions.extend(questions_db[skill])

    return questions