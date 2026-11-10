
from game import QuizGame


def show_menu():
    print("\n==============================")
    print("      PyQuest 퀴즈 게임")
    print("==============================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("==============================")


def main():
    game = QuizGame()

    try:
        while True:
            show_menu()
            choice = input("번호를 선택하세요: ").strip()

            if choice == "1":
                game.play_quiz()

            elif choice == "2":
                game.add_quiz()

            elif choice == "3":
                game.list_quizzes()

            elif choice == "4":
                print("점수 확인 기능 준비 중")

            elif choice == "5":
                print("게임을 종료합니다.")
                break

            else:
                print("1~5번 중에서 선택하세요.")

    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 안전하게 종료합니다.")


if __name__ == "__main__":
    main()
