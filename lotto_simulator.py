import random
print('Choose your six numbers! (1-49)')

numbers = []


def user_input_number():
    """
    Get number from user
    Try until user gives proper number

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            user_input = int(input(f'Number {len(numbers)+1}: '))
        except ValueError:
            print('This is not a number!')
            continue
        return user_input


def get_numbers():
    """
    Get six different numbers between 1 and 49

    :rtype:list
    :return: list with 6 numbers provided by user
    """
    while len(numbers) < 6:
        number = user_input_number()
        if number not in numbers and 49 > number > 0:
            numbers.append(number)
        elif number in numbers:
            print('Number already picked')
        elif number > 49:
            print('Number too high!')
        elif number < 0:
            print('Number too small!')
    return numbers


sorted_user_numbers = sorted(get_numbers())
print(f"Your numbers: {sorted_user_numbers}")
print('')
"""
Print given numbers with ascending order.
"""

print('Press enter to get the result!')
input()
print('')
lotto_numbers = list(range(1, 49))
random.shuffle(lotto_numbers)
six_lotto_numbers = lotto_numbers[:6]

print(f"Winning numbers: {six_lotto_numbers}")
print('')
"""
Shuffle 49 random numbers and print first six numbers.
"""


def lotto():
    """
    Compare user numbers with random shuffled numbers and print the result.
    """

    hits = 0
    for user_number in sorted_user_numbers:
        if user_number in six_lotto_numbers:
            hits += 1
    print('-------------------------')
    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")
    print('-------------------------')


if __name__ == '__main__':
    lotto()
