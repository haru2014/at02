
from questions import create_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        correct_count = 0
        total = len(self.quizzes)

        print(f"\n퀴즈를 시작합니다! 총 {total}문제")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n===== 문제 {number} =====")
            quiz.display()

            while True:
                user_input = input("정답 번호 (1~4): ").strip()

                if not user_input:
                    print("정답 번호를 입력하세요.")
                    continue

                try:
                    user_answer = int(user_input)
                except ValueError:
                    print("숫자를 입력해주세요.")
                    continue

                if user_answer < 1 or user_answer > 4:
                    print("1~4 사이의 숫자를 입력하세요.")
                    continue

                break

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        score = round(correct_count / total * 100)

        print("\n==============================")
        print(f"결과: {total}문제 중 {correct_count}문제 정답")
        print(f"최종 점수: {score}점")
        print("==============================")
