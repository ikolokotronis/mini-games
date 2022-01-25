import random


class LotterySimulator:

    def __init__(self):
        self.chosen_numbers = []
        self.winning_numbers = []

    def user_number(self):
        """
        Get number from user
        Try until user gives proper number

        :rtype: int
        :return: given number as int
        """
        number_count = 0
        while number_count < 6:
            try:
                number_count += 1
                user_input = int(input(f'Number {len(self.chosen_numbers) + 1}: '))
            except ValueError:
                print('This is not a number!')
                continue
            return user_input

    def get_numbers(self):
        """
        Get six different numbers between 1 and 49

        :rtype:list
        :return: list with 6 numbers provided by user
        """
        while len(self.chosen_numbers) < 6:
            number = self.user_number()
            if number not in self.chosen_numbers and 49 > number > 0:
                self.chosen_numbers.append(number)
            elif number in self.chosen_numbers:
                print('Number already picked')
            elif number > 49:
                print('Number too high!')
            elif number < 0:
                print('Number too small!')

    def print_user_numbers(self):
        """
             Print given numbers with ascending order.
                """
        sorted_user_numbers = sorted(self.chosen_numbers)
        print(f"Your numbers: {sorted_user_numbers}")
        print('')

    def print_winning_numbers(self):
        """
        Shuffle 49 random numbers and print first six numbers.
        """
        print('Press enter to get the result!')
        input()
        print('')
        lotto_numbers = list(range(1, 49))
        random.shuffle(lotto_numbers)
        self.winning_numbers = lotto_numbers[:6]

        print(f"Winning numbers: {self.winning_numbers}")
        print('')

    def lotto(self):
        """
        Compare user numbers with random shuffled numbers and print the result.
        """

        hits = 0
        for user_number in self.chosen_numbers:
            if user_number in self.winning_numbers:
                hits += 1
        print('-------------------------')
        print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")
        print('-------------------------')


ls = LottoSimulator()

ls.get_numbers()
ls.print_user_numbers()
ls.print_winning_numbers()
ls.lotto()
