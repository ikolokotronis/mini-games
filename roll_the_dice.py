import random

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

print('Choose your parameters')

user_input = input('Input: ').upper()

POSSIBLE_DICES = (

    "D100",

    "D20",

    "D12",

    "D10",

    "D8",

    "D6",

    "D4",

    "D3"

)


def dice_generator():
    """
    Calculate dice roll from dice pattern.(based on user_input)

    :param str user_input: dice pattern ex. '3D10-5'

    :rtype: int,str
    :return: dice roll value for proper dice pattern, 'Wrong Input'
    """
    for dice in POSSIBLE_DICES:
        if dice in user_input:
            try:
                dice_split = user_input.split('D')
                if "+" in dice_split[1] and dice_split[0] is "":
                    plus_split = dice_split[1].split("+")
                    dice_type = int(plus_split[0])
                    addition = plus_split[1]
                    addition = int(addition)
                    dice_roll = random.randint(1, dice_type)
                    mainresult = dice_roll + addition
                    return mainresult
                elif "+" in dice_split[1] and dice_split[0] is not "":
                    plus_split = dice_split[1].split("+")
                    dice_type = int(plus_split[0])
                    addition = plus_split[1]
                    addition = int(addition)
                    multiplier = int(dice_split[0])
                    dice_roll = random.randint(1, dice_type)
                    mainresult = dice_roll * multiplier
                    return mainresult + addition
                elif "-" in dice_split[1] and dice_split[0] is "":
                    minus_split = dice_split[1].split("-")
                    dice_type = int(minus_split[0])
                    subdivision = minus_split[1]
                    subdivision = int(subdivision)
                    dice_roll = random.randint(1, dice_type)
                    mainresult = dice_roll - subdivision
                    return mainresult
                elif "-" in dice_split[1] and dice_split[0] is not "":
                    minus_split = dice_split[1].split("-")
                    dice_type = int(minus_split[0])
                    subdivision = minus_split[1]
                    subdivision = int(subdivision)
                    multiplier = int(dice_split[0])
                    dice_roll = random.randint(1, dice_type)
                    mainresult = dice_roll * multiplier - subdivision
                    return mainresult
                elif dice_split[0] is not "":
                    dice_type = int(dice_split[1])
                    multiplier = int(dice_split[0])
                    dice_roll = random.randint(1, dice_type)
                    mainresult = dice_roll * multiplier
                    return mainresult
                elif dice_split[0] is "":
                    dice_type = int(dice_split[1])
                    dice_roll = random.randint(1, dice_type)
                    mainresult = dice_roll
                    return mainresult
            except ValueError:
                return 'Wrong input!'
    else:
        return 'No such dice!'

print(dice_generator())