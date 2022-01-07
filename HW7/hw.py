class Judge:
    def __init__(self, answer: str) -> None:
        """
        Set the answer as the attribute of Judge
        answer: (int) the final answer
        """
        self.answer = answer


    def guess(self, num: str) -> bool:
        """
        Method that guess the number, it'll print info that shows:
            Your guess is ...; the result is xAxB
            e.g.: Your guess is 0123; the result is 0A1B
        num: the number that it guessed
        return: whether the player guess the correct answer
        """
        count_A = 0
        count_B = 0
        for i in range(len(num)):
            if num[i] == self.answer[i]:
                count_A += 1
            for j in range(len(self.answer)):
                if i == j:
                    continue
                if num[i] == self.answer[j]:
                    count_B += 1
        s = 'Your guess is ' + str(num) + '; the result is ' + str(count_A) + 'A' + str(count_B) + 'B'
        print(s)
        return count_A == len(num)


def read_input(guess_len: int) -> str:
    """
    Function that read player's guess.
    guess_len: length the the player should guess. it would be same as the length of answer
    return: the valid string guessed by player

    You should show the hint message:
        "Enter your guess:\n"
    If the player's guess is invalid, you should print:
        "Invalid, please enter your guess again:\n"
    Note: a valid guess means contain only guess_len non-repetitive integer range from 0~9
    """
    reply = input("Enter your guess:\n")
    while True:
        check = 0
        if len(reply) != guess_len:
            reply = input("Invalid, please enter your guess again:\n")
            continue
        for i in range(guess_len):
            if str.isdigit(reply) == False:
                check = 1
                break
            for j in range(guess_len):
                if j == i:
                    continue
                if reply[i] == reply[j]:
                    check = 1
        if check == 1:
            reply = input("Invalid, please enter your guess again:\n")
            continue
        break
    return reply



def enter_answer() -> str:
    """
    Function that enter the answer, you can assume that the answer must be valid.
    """
    return input()