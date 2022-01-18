import random

print('Try to guess the number (1-100)')
print('Press enter to continue')
input()


def main_function():
    """
    Get number from user via input
    Try until the number is proper(int)
    :rtype: int
    :return: given number as int
    """
    winning_number = random.randint(1, 100)
    attempts_count = 0
    while True:
        if attempts_count == 10:
            print('You lost!')
            break
        try:
            user_input_number = int(input('Guess the number: '))
            if user_input_number > 100:
                print('Number cannot be bigger than 100!')
                continue
            elif user_input_number < 0:
                print('Number cannot be smaller than 0!')
                continue
        except ValueError:
            print('This is not a number!')
            continue
        if user_input_number < winning_number:
            print('Too small!')
            attempts_count += 1
            continue
        elif user_input_number > winning_number:
            print('Too big!')
            attempts_count += 1
            continue
        elif user_input_number == winning_number:
            return 'You win!'
    return 'Game over'


if __name__ == '__main__':

    print(main_function())
