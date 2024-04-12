import random
class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Rules:")
        print("- Answer multiple-choice questions by entering the corresponding letter (A, B, C, or D).")
        print("- Let's see how well you know the topic!\n")
    def load_quiz_questions(self):
        random.shuffle(self.questions)
    def present_quiz_questions(self):
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question['question']}")
            if 'choices' in question:
                for choice in question['choices']:
                    print(choice)
            user_answer = input("Your answer: ").strip().upper()
            if 'answer' in question:
                if user_answer == question['answer']:
                    print("Correct!")
                    self.score += 1
                else:
                    print("Incorrect!")
                    print("Correct answer:", question['answer'])
            else:
                if user_answer == question['expected_answer']:
                    print("Correct!")
                    self.score += 1
                else:
                    print("Incorrect!")
                    print("Correct answer:", question['expected_answer'])
            print()
    def display_final_results(self):
        print("Quiz Completed!")
        print("Your Final Score:", self.score)
    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        return choice == 'yes'

def main():
    questions = [
        {
            'question': "What is the capital of France?",
            'choices': ["A) London", "B) Paris", "C) Rome", "D) Berlin"],
            'answer': "B"
        },
        {
            'question': "What is the largest planet in our solar system?",
            'choices': ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
            'answer': "B"
        },
        {
            'question': "What is the powerhouse of the cell?",
            'choices': ["A) Nucleus", "B) Mitochondria", "C) Ribosome", "D) Golgi apparatus"],
            'answer': "B"
        },
        {
            'question': "Which country is known as the Land of the Rising Sun?",
            'choices': ["A) China", "B) Japan", "C) South Korea", "D) Thailand"],
            'answer': "B"
        },
        {
            'question': "What is the chemical symbol for water?",
            'choices': ["A) H2O", "B) O2", "C) CO2", "D) H2SO4"],
            'answer': "A"
        }
    ]
    game = QuizGame(questions)
    game.display_welcome_message()

    play_again = True
    while play_again:
        game.load_quiz_questions()
        game.present_quiz_questions()
        game.display_final_results()
        play_again = game.play_again()

if __name__ == "__main__":
    main()

