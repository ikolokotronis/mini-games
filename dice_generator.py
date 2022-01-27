import random


class DiceGenerator:
    def __init__(self):
        pass

    @staticmethod
    def welcome():
        print('Welcome to dice roll generator!')
        print('-----------')
        print('Possible dices: D3, D4, D6, D8, D10, D12, D20, D100')
        print('-----------')
        print('Add an x number before your dice of choice to throw your dice x times')
        print('-----------')
        print('Add + x or - x next to your dice of choice to add x to the result or subtract x from the result ')
        print('-----------')
        print('Example: 2D6+10 throws a standard six-sided dice two times and adds 10 to the result')
        print('-----------')
        print('Press enter to continue')
        input()

    @staticmethod
    def possible_dices():
        dices = [

            "D100",

            "D20",

            "D12",

            "D10",

            "D8",

            "D6",

            "D4",

            "D3"

        ]
        return dices

    def dice_handler(self):
        dice = self.get_dice()
        if "+" in dice[1] and dice[0] == "":
            plus_split = dice[1].split("+")
            dice_type = int(plus_split[0])
            addition = int(plus_split[1])
            result = random.randint(1, dice_type) + addition
            print(result)
        elif "+" in dice[1] and dice[0] != "":
            plus_split = dice[1].split("+")
            dice_type = int(plus_split[0])
            addition = int(plus_split[1])
            multiplier = int(dice[0])
            dice_roll = random.randint(1, dice_type)
            result = (dice_roll * multiplier) + addition
            print(result)
        elif "-" in dice[1] and dice[0] == "":
            minus_split = dice[1].split("-")
            dice_type = int(minus_split[0])
            subdivision = int(minus_split[1])
            dice_roll = random.randint(1, dice_type)
            result = dice_roll - subdivision
            print(result)
        elif "-" in dice[1] and dice[0] != "":
            minus_split = dice[1].split("-")
            dice_type = int(minus_split[0])
            subdivision = int(minus_split[1])
            multiplier = int(dice[0])
            dice_roll = random.randint(1, dice_type)
            result = dice_roll * multiplier - subdivision
            print(result)
        elif dice[0] != "":
            dice_type = int(dice[1])
            multiplier = int(dice[0])
            dice_roll = random.randint(1, dice_type)
            result = dice_roll * multiplier
            print(result)
        elif dice[0] == "":
            dice_type = int(dice[1])
            result = random.randint(1, dice_type)
            print(result)

    def get_dice(self):
        right_input = 0
        while right_input == 0:
            user_input = input('Choose your dice: ').upper()
            for dice in self.possible_dices():
                if dice in user_input:
                    user_input_split = user_input.split('D')
                    right_input = 1
                    return user_input_split
            else:
                print('Wrong input!')
                continue


dg = DiceGenerator()
dg.welcome()
dg.dice_handler()
