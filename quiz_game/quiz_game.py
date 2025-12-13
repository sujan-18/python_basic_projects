class Question: #defining class name 

    def __init__(self, question_text, options, correct_answer):  # defining constructure with paramater
        self.question_text = question_text 
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer): #defining function to check the user input
        return user_answer.lower() == self.correct_answer.lower()

filename='questions.txt'

def load_questions_from_file(filename):
    questions = []

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read().strip()

    blocks = content.split('---')

    for block in blocks:
        if not block.strip():
            continue

        data = {}
        lines = block.strip().split('\n')

        for line in lines:
            key, value = line.split('=', 1)
            data[key.strip()] = value.strip()

        question = Question(
            question_text=data['question'],
            options={
                'a': data['a'],
                'b': data['b'],
                'c': data['c'],
                'd': data['d']
            },
            correct_answer=data['answer']
        )

        questions.append(question)

    return questions

import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("\n🎯 Welcome to the Quiz Game")
        random.shuffle(self.questions)

        for index, question in enumerate(self.questions, start=1):
            print(f"\nQ{index}: {question.question_text}")

            for key, value in question.options.items():
                print(f" {key}) {value}")

            user_answer = input("Your answer (a/b/c/d): ").lower()

            if question.check_answer(user_answer):
                print("✔ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! Correct answer is {question.correct_answer}")

        print("\n📊 Final Score:", self.score, "/", len(self.questions))


questions = load_questions_from_file(filename)

quiz = Quiz(questions)
quiz.start()
