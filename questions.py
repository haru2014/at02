
from quiz import Quiz


def create_default_quizzes():
    return [
        Quiz(
            "Python에서 변수에 숫자 10을 저장하는 올바른 코드는?",
            ["x == 10", "x = 10", "10 = x", "x -> 10"],
            2
        ),

        Quiz(
            "Python에서 문자열을 나타내는 자료형은?",
            ["int", "str", "bool", "list"],
            2
        ),

        Quiz(
            "여러 개의 데이터를 순서대로 저장하는 자료형은?",
            ["int", "bool", "list", "str"],
            3
        ),

        Quiz(
            "조건에 따라 다른 코드를 실행하는 키워드는?",
            ["while", "if", "def", "return"],
            2
        ),

        Quiz(
            "Python에서 함수를 정의할 때 사용하는 키워드는?",
            ["class", "print", "for", "def"],
            4
        )
    ]


if __name__ == "__main__":
    quizzes = create_default_quizzes()

    print(f"기본 퀴즈 {len(quizzes)}개가 준비되었습니다.")

    for number, quiz in enumerate(quizzes, start=1):
        print(f"\n===== 퀴즈 {number} =====")
        quiz.display()
        print(f"정답 번호: {quiz.answer}")
