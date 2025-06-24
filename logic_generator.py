def generate_questions(text):
    return [
        "What is the main problem the assistant solves?",
        "How does the assistant justify its answers?",
        "What input formats are supported by the assistant?"
    ]

def evaluate_answers(text, user_answers):
    correct_answers = generate_questions(text)
    feedback = []
    for idx, ans in enumerate(user_answers):
        ref = "This relates to section discussing: " + correct_answers[idx]
        feedback.append({"your_answer": ans, "feedback": "Good attempt.", "justification": ref})
    return feedback
