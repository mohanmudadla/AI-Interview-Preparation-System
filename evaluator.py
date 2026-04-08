from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_answer(user_answer, correct_answer):
    
    vectorizer = TfidfVectorizer()
    
    vectors = vectorizer.fit_transform([user_answer, correct_answer])
    
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    
    score = round(similarity * 10, 2)
    
    if score > 8:
        feedback = "Excellent answer"
    elif score > 5:
        feedback = "Good answer, but can improve"
    else:
        feedback = "Needs improvement"
    
    return score, feedback


def get_correct_answer(question):
    
    answers_db = {
        "What is OOP in Python?": "OOP is object oriented programming including inheritance polymorphism encapsulation",
        
        "What are decorators in Python?": "Decorators are functions that modify the behavior of other functions",
        
        "Explain list vs tuple.": "List is mutable whereas tuple is immutable",
        
        "What is overfitting?": "Overfitting is when model performs well on training data but poorly on new data"
    }
    
    return answers_db.get(question, "")