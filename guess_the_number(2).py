def main_function():
    """
    Return proper value provided by user.

    :rtype: str

    :return: value provided by user from ["too small", "too big", "you won"]

    """
    print('Think of a number from 0 to 1000 and i will try to guess it within max. 10 attempts')
    print('If the number is too big type: "too much"')
    print('If the number is too small type: "too low"')
    print('If I guessed type: "you won"')
    print("Press 'Enter' to continue")
    input()
    min_number = 0
    max_number = 1000
    user_input_values = ['you won', 'too much', 'too low']
    while True:
        guess = int((max_number-min_number)/2)+min_number
        print(f"I guess {guess}")
        user_answer = str(input('Answer: ')).lower()
        if user_answer == 'you won':
            return 'I won!'
        elif user_answer == 'too much':
            max_number = guess
        elif user_answer == 'too low':
            min_number = guess
        elif user_answer not in user_input_values:
            print("Wrong input!")
            continue
    return 'You won!'


if __name__ == '__main__':

    print(main_function())
