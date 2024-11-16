class Quiz:

    def __init__(self):

        self.questions = [
            {
                "question": "What is the primary goal of Artificial Intelligence?",
                "options": "A) To perform mathematical calculations\nB) To think like a human\nC) To perform tasks that normally require human intelligence\nD) To play games",
                "answer": "C"
            },
            {
                "question": "In supervised learning, the model is trained using which type of data?",
                "options": "A) Labeled data\nB) Unlabeled data\nC) Semi-labeled data\nD) Noisy data",
                "answer": "A"
            },
            {
                "question": "What is a neural network in the context of AI?",
                "options": "A) A type of data storage\nB) A framework to model complex patterns using layers of nodes\nC) A method of calculating accuracy\nD) An alogrithm for sorting data",
                "answer": "B"
            },
            {
                "question": "Which algorithm is commonly used for classification tasks?",
                "options": "A) K-Nearest Neighbors(KNN)\nB) Linear Regression\nC) Support Vector Machines(SVM)\nD) Both A and C",
                "answer": "D"
            },
            {
                "question": "What is a common metric to evaluate a classification model's performance?",
                "options": "A) Mean Squared Error\nB) Accuracy\nC) Correlation\nD) Distance",
                "answer": "B"
            }
        ]

        self.score = 0

    def start_quiz(self):
        print("--------------------Welcome to the AI Quiz!--------------------")
        for i,ques in enumerate(self.questions,1):
            print(f"Question {i}: {ques['question']}")
            print(ques["options"])
        
            answer = input("Your Answer : ").upper()

            if answer == ques['answer']:
                print("Correct Answer")
                self.score +=2

            else:
                print("Wrong Answer")
                self.score -= 0.5

        print(f"\t\t\tYour Final Score is {self.score} out of 10")

quiz = Quiz()
quiz.start_quiz()