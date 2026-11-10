
from questions import create_default_quizzes


class QuizGame:
    
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.best_correct = None
        self.best_total = None


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

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.best_correct = correct_count
            self.best_total = total
            print("\n새로운 최고 점수를 기록했습니다!")


        print("\n==============================")
        print(f"결과: {total}문제 중 {correct_count}문제 정답")
        print(f"최종 점수: {score}점")
        print("==============================")

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")

        while True:
            question = input("문제를 입력하세요: ").strip()

            if question:
                break

            print("문제 내용을 입력해주세요.")

        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"선택지 {number}: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("선택지를 입력해주세요.")

        while True:
            user_input = input("정답 번호 (1~4): ").strip()

            try:
                answer = int(user_input)
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            if answer < 1 or answer > 4:
                print("1~4 사이의 숫자를 입력하세요.")
                continue

            break

        from quiz import Quiz

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("\n퀴즈가 추가되었습니다!")
        print(f"현재 퀴즈 수: {len(self.quizzes)}개")

    def list_quizzes(self):
        print("\n==============================")
        print("       등록된 퀴즈 목록")
        print("==============================")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"전체 퀴즈: {len(self.quizzes)}개")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{number}] {quiz.question}")

        print("\n==============================")

    def show_score(self):
        print("\n==============================")
        print("       최고 점수 확인")
        print("==============================")

        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")
            print(
                f"정답 기록: {self.best_total}문제 중 "
                f"{self.best_correct}문제 정답"
            )

        print("==============================")
