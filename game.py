

import json
from pathlib import Path

from quiz import Quiz
from questions import create_default_quizzes



class QuizGame:
    
    
    def __init__(self):
        self.state_file = Path(__file__).resolve().parent / "state.json"

        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.best_correct = None
        self.best_total = None

        self.load_state()



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
        self.save_state()
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

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
            "best_correct": self.best_correct,
            "best_total": self.best_total
        }

        try:
            with self.state_file.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return True

        except (OSError, TypeError) as error:
            print(f"데이터 저장 오류: {error}")
            return False

    def load_state(self):
        try:
            with self.state_file.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("JSON 데이터 형식이 올바르지 않습니다.")

            raw_quizzes = data["quizzes"]

            if not isinstance(raw_quizzes, list):
                raise ValueError("퀴즈 목록 형식이 올바르지 않습니다.")

            loaded_quizzes = []

            for item in raw_quizzes:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 항목 형식 오류")

                question = item["question"]
                choices = item["choices"]
                answer = item["answer"]

                if not isinstance(question, str) or not question.strip():
                    raise ValueError("문제 내용 오류")

                if (
                    not isinstance(choices, list)
                    or len(choices) != 4
                    or not all(isinstance(c, str) and c.strip() for c in choices)
                ):
                    raise ValueError("선택지 형식 오류")

                if type(answer) is not int or not 1 <= answer <= 4:
                    raise ValueError("정답 번호 오류")

                loaded_quizzes.append(Quiz(question, choices, answer))

            score = data.get("best_score")
            correct = data.get("best_correct")
            total = data.get("best_total")

            if score is None:
                if correct is not None or total is not None:
                    raise ValueError("점수 기록 형식 오류")
            else:
                if type(score) is not int or not 0 <= score <= 100:
                    raise ValueError("최고 점수 형식 오류")

                if (
                    type(correct) is not int
                    or type(total) is not int
                    or total < 1
                    or not 0 <= correct <= total
                ):
                    raise ValueError("정답 기록 형식 오류")

            self.quizzes = loaded_quizzes
            self.best_score = score
            self.best_correct = correct
            self.best_total = total

            print(f"저장된 데이터 불러오기 완료! 퀴즈 {len(self.quizzes)}개")

        except FileNotFoundError:
            print("첫 실행입니다. 기본 퀴즈를 사용합니다.")
            self.save_state()

        except (OSError, UnicodeError, ValueError, KeyError, TypeError) as error:
            print(f"파일 불러오기 오류: {error}")
            print("기본 퀴즈 데이터로 복구합니다.")

            self.quizzes = create_default_quizzes()
            self.best_score = None
            self.best_correct = None
            self.best_total = None
            self.save_state()
