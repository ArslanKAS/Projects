class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list

    def still_have_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q.{self.question_no} {current_question.question}, (True/False)? ")
        self.check_answer(ans,current_question.correct_answer.lower())


    def check_answer(self,user_answer,correct_answer):

        if user_answer == correct_answer :
            print("Hurray! you got it right")
            self.score += 1
        else:
            print("Dude you're so wrong. Go and learn..")

        print(f"The correct answer is: {correct_answer.upper()}")
        print(f"Your score: {self.score}/{self.question_no}\n")



