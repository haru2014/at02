
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print("\n문제:", self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }


if __name__ == "__main__":
    sample = Quiz(
        "Python에서 문자열을 나타내는 자료형은?",
        ["int", "str", "list", "bool"],
        2
    )

    sample.display()

    print("2번을 선택하면:", sample.check_answer(2))
    print("1번을 선택하면:", sample.check_answer(1))
