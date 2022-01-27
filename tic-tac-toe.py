import random


class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(10)]
        self.game_over = False
        self.user_letter_choice = ""
        self.player_move = 0

    def game_loop(self):
        while not self.game_over:
            self.print_board()
            self.user_input()
            self.cpu_player_handler()
            free_space = len([i for i in self.board if i == " "])
            if free_space == 0:
                print("Tie! No one wins")
                self.game_over = True
            if self.check_winner("X"):
                self.print_board()
                print('Player X won!')
                self.game_over = True
            elif self.check_winner("O"):
                self.print_board()
                print('Player O won!')
                self.game_over = True

    def check_winner(self, player):
        return (self.board[7] == player and self.board[8] == player and self.board[9] == player) or (
                self.board[4] == player and self.board[5] == player and self.board[6] == player) or (
                self.board[1] == player and self.board[2] == player and self.board[3] == player) or (
                self.board[1] == player and self.board[4] == player and self.board[7] == player) or (
                self.board[2] == player and self.board[5] == player and self.board[8] == player) or (
                self.board[3] == player and self.board[6] == player and self.board[9] == player) or (
                self.board[1] == player and self.board[5] == player and self.board[9] == player) or (
                self.board[3] == player and self.board[5] == player and self.board[7] == player)

    def print_board(self):
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])

    def insert_letter(self, letter, position):
        self.board[position] = letter

    def check_if_space_is_free(self, position):
        return self.board[position] == ' '

    def user_letter(self):
        letter_input = input('Choose your letter ( X or O ): ').upper()
        self.user_letter_choice = letter_input
        print(f"You play as {letter_input}")

    def user_input(self):
        user_input = input("Choose your position (ex. X,6): ").upper()
        user_input_split = user_input.split(',')
        
        get_letter = user_input_split[0]
        get_position = int(user_input_split[1])
        if self.check_if_space_is_free(get_position):
            self.insert_letter(get_letter, get_position)
            self.player_move = 1
        else:
            print('')
            print("Position is taken!")
            print('')

    def cpu_player_handler(self):
        possible_moves = [x for x, letter in enumerate(self.board) if letter == ' ' and x != 0]
        corners = [1, 3, 7, 9]
        middle = 5
        leftovers = [2, 4, 6, 8]
        move = 0

        # When player chooses to play as X
        if self.user_letter_choice == "X" and self.player_move == 1:

            for i in possible_moves:

                # normal winning case
                if self.board[7] == "O" and self.board[8] == "O" and self.check_if_space_is_free(9) and move == 0:
                    self.insert_letter("O", 9)
                    move = 1
                    self.player_move = 0
                elif self.board[4] == "O" and self.board[5] == "O" and self.check_if_space_is_free(6) and move == 0:
                    self.insert_letter("O", 6)
                    move = 1
                    self.player_move = 0
                elif self.board[1] == "O" and self.board[2] == "O" and self.check_if_space_is_free(3) and move == 0:
                    self.insert_letter("O", 3)
                    move = 1
                    self.player_move = 0
                elif self.board[1] == "O" and self.board[4] == "O" and self.check_if_space_is_free(7) and move == 0:
                    self.insert_letter("O", 7)
                    move = 1
                    self.player_move = 0
                elif self.board[2] == "O" and self.board[5] == "O" and self.check_if_space_is_free(8) and move == 0:
                    self.insert_letter("O", 8)
                    move = 1
                    self.player_move = 0
                elif self.board[3] == "O" and self.board[6] == "O" and self.check_if_space_is_free(9) and move == 0:
                    self.insert_letter("O", 9)
                    move = 1
                    self.player_move = 0
                elif self.board[1] == "O" and self.board[5] == "O" and self.check_if_space_is_free(9) and move == 0:
                    self.insert_letter("O", 9)
                    move = 1
                    self.player_move = 0
                elif self.board[7] == "O" and self.board[5] == "O" and self.check_if_space_is_free(3) and move == 0:
                    self.insert_letter("O", 3)
                    move = 1
                    self.player_move = 0

                # backwards winning case
                elif self.board[9] == "O" and self.board[8] == "O" and self.check_if_space_is_free(7) and move == 0:
                    self.insert_letter("O", 7)
                    move = 1
                    self.player_move = 0
                elif self.board[6] == "O" and self.board[5] == "O" and self.check_if_space_is_free(4) and move == 0:
                    self.insert_letter("O", 4)
                    move = 1
                    self.player_move = 0
                elif self.board[3] == "O" and self.board[2] == "O" and self.check_if_space_is_free(1) and move == 0:
                    self.insert_letter("O", 1)
                    move = 1
                    self.player_move = 0
                elif self.board[7] == "O" and self.board[4] == "O" and self.check_if_space_is_free(1) and move == 0:
                    self.insert_letter("O", 1)
                    move = 1
                    self.player_move = 0
                elif self.board[8] == "O" and self.board[5] == "O" and self.check_if_space_is_free(2) and move == 0:
                    self.insert_letter("O", 2)
                    move = 1
                    self.player_move = 0
                elif self.board[9] == "O" and self.board[6] == "O" and self.check_if_space_is_free(3) and move == 0:
                    self.insert_letter("O", 3)
                    move = 1
                    self.player_move = 0
                elif self.board[9] == "O" and self.board[5] == "O" and self.check_if_space_is_free(1) and move == 0:
                    self.insert_letter("O", 1)
                    move = 1
                    self.player_move = 0
                elif self.board[3] == "O" and self.board[5] == "O" and self.check_if_space_is_free(7) and move == 0:
                    self.insert_letter("O", 7)
                    move = 1
                    self.player_move = 0

                # middle winning case
                elif self.board[9] == "O" and self.board[7] == "O" and self.check_if_space_is_free(8) and move == 0:
                    self.insert_letter("O", 8)
                    move = 1
                    self.player_move = 0
                elif self.board[6] == "O" and self.board[4] == "O" and self.check_if_space_is_free(5) and move == 0:
                    self.insert_letter("O", 5)
                    move = 1
                    self.player_move = 0
                elif self.board[3] == "O" and self.board[1] == "O" and self.check_if_space_is_free(2) and move == 0:
                    self.insert_letter("O", 2)
                    move = 1
                    self.player_move = 0
                elif self.board[7] == "O" and self.board[1] == "O" and self.check_if_space_is_free(4) and move == 0:
                    self.insert_letter("O", 4)
                    move = 1
                    self.player_move = 0
                elif self.board[8] == "O" and self.board[2] == "O" and self.check_if_space_is_free(5) and move == 0:
                    self.insert_letter("O", 5)
                    move = 1
                    self.player_move = 0
                elif self.board[9] == "O" and self.board[3] == "O" and self.check_if_space_is_free(6) and move == 0:
                    self.insert_letter("O", 6)
                    move = 1
                    self.player_move = 0
                elif self.board[9] == "O" and self.board[1] == "O" and self.check_if_space_is_free(5) and move == 0:
                    self.insert_letter("O", 5)
                    move = 1
                    self.player_move = 0
                elif self.board[3] == "O" and self.board[7] == "O" and self.check_if_space_is_free(5) and move == 0:
                    self.insert_letter("O", 5)
                    move = 1
                    self.player_move = 0

                # try to take the corners
                elif i in corners:
                    random_choice = random.choice(corners)
                    while move != 1 and self.check_if_space_is_free(random_choice):
                        self.insert_letter("O", random_choice)
                        move = 1
                        self.player_move = 0

                # try to take the middle
                elif i == middle:
                    while move != 1 and self.check_if_space_is_free(middle):
                        self.insert_letter("O", middle)
                        move = 1
                        self.player_move = 0

                # try to take the leftovers
                elif i in leftovers:
                    random_choice = random.choice(leftovers)
                    while move != 1 and self.check_if_space_is_free(random_choice):
                        self.insert_letter("O", random_choice)
                        move = 1
                        self.player_move = 0

        # When player chooses to play as O
        if self.user_letter_choice == "O" and self.player_move == 1:

            for i in possible_moves:

                # normal winning case
                if self.board[7] == "X" and self.board[8] == "X" and self.check_if_space_is_free(9) and move == 0:
                    self.insert_letter("X", 9)
                    move = 1
                    self.player_move = 0
                elif self.board[4] == "X" and self.board[5] == "X" and self.check_if_space_is_free(6) and move == 0:
                    self.insert_letter("X", 6)
                    move = 1
                    self.player_move = 0
                elif self.board[1] == "X" and self.board[2] == "X" and self.check_if_space_is_free(3) and move == 0:
                    self.insert_letter("X", 3)
                    move = 1
                    self.player_move = 0
                elif self.board[1] == "X" and self.board[4] == "X" and self.check_if_space_is_free(7) and move == 0:
                    self.insert_letter("X", 7)
                    move = 1
                    self.player_move = 0
                elif self.board[2] == "X" and self.board[5] == "X" and self.check_if_space_is_free(8) and move == 0:
                    self.insert_letter("X", 8)
                    move = 1
                    self.player_move = 0
                elif self.board[3] == "X" and self.board[6] == "X" and self.check_if_space_is_free(9) and move == 0:
                    self.insert_letter("X", 9)
                    move = 1
                    self.player_move = 0
                elif self.board[1] == "X" and self.board[5] == "X" and self.check_if_space_is_free(9) and move == 0:
                    self.insert_letter("X", 9)
                    move = 1
                    self.player_move = 0
                elif self.board[7] == "X" and self.board[5] == "X" and self.check_if_space_is_free(3) and move == 0:
                    self.insert_letter("X", 3)
                    move = 1
                    self.player_move = 0

                # backwards winning case
                elif self.board[9] == "X" and self.board[8] == "X" and self.check_if_space_is_free(7) and move == 0:
                    self.insert_letter("X", 7)
                    move = 1
                    self.player_move = 0
                elif self.board[6] == "X" and self.board[5] == "X" and self.check_if_space_is_free(4) and move == 0:
                    self.insert_letter("X", 4)
                    move = 1
                    self.player_move = 0
                elif self.board[3] == "X" and self.board[2] == "X" and self.check_if_space_is_free(1) and move == 0:
                    self.insert_letter("X", 1)
                    move = 1
                    self.player_move = 0
                elif self.board[7] == "X" and self.board[4] == "X" and self.check_if_space_is_free(1) and move == 0:
                    self.insert_letter("X", 1)
                    move = 1
                    self.player_move = 0
                elif self.board[8] == "X" and self.board[5] == "X" and self.check_if_space_is_free(2) and move == 0:
                    self.insert_letter("X", 2)
                    move = 1
                    self.player_move = 0
                elif self.board[9] == "X" and self.board[6] == "X" and self.check_if_space_is_free(3) and move == 0:
                    self.insert_letter("X", 3)
                    move = 1
                    self.player_move = 0
                elif self.board[9] == "X" and self.board[5] == "X" and self.check_if_space_is_free(1) and move == 0:
                    self.insert_letter("X", 1)
                    move = 1
                    self.player_move = 0
                elif self.board[3] == "X" and self.board[5] == "X" and self.check_if_space_is_free(7) and move == 0:
                    self.insert_letter("X", 7)
                    move = 1
                    self.player_move = 0

                # middle winning case
                elif self.board[9] == "X" and self.board[7] == "X" and self.check_if_space_is_free(8) and move == 0:
                    self.insert_letter("X", 8)
                    move = 1
                    self.player_move = 0
                elif self.board[6] == "X" and self.board[4] == "X" and self.check_if_space_is_free(5) and move == 0:
                    self.insert_letter("X", 5)
                    move = 1
                    self.player_move = 0
                elif self.board[3] == "X" and self.board[1] == "X" and self.check_if_space_is_free(2) and move == 0:
                    self.insert_letter("X", 2)
                    move = 1
                    self.player_move = 0
                elif self.board[7] == "X" and self.board[1] == "X" and self.check_if_space_is_free(4) and move == 0:
                    self.insert_letter("X", 4)
                    move = 1
                    self.player_move = 0
                elif self.board[8] == "X" and self.board[2] == "X" and self.check_if_space_is_free(5) and move == 0:
                    self.insert_letter("X", 5)
                    move = 1
                    self.player_move = 0
                elif self.board[9] == "X" and self.board[3] == "X" and self.check_if_space_is_free(6) and move == 0:
                    self.insert_letter("X", 6)
                    move = 1
                    self.player_move = 0
                elif self.board[9] == "X" and self.board[1] == "O" and self.check_if_space_is_free(5) and move == 0:
                    self.insert_letter("X", 5)
                    move = 1
                    self.player_move = 0
                elif self.board[3] == "X" and self.board[7] == "X" and self.check_if_space_is_free(5) and move == 0:
                    self.insert_letter("X", 5)
                    move = 1
                    self.player_move = 0

                # try to take the corners
                elif i in corners:
                    random_choice = random.choice(corners)
                    while move != 1 and self.check_if_space_is_free(random_choice):
                        self.insert_letter("X", random_choice)
                        move = 1
                        self.player_move = 0

                # try to take the middle
                elif i == middle:
                    while move != 1 and self.check_if_space_is_free(middle):
                        self.insert_letter("X", middle)
                        move = 1
                        self.player_move = 0

                # try to take the leftovers
                elif i in leftovers:
                    random_choice = random.choice(leftovers)
                    while move != 1 and self.check_if_space_is_free(random_choice):
                        self.insert_letter("X", random_choice)
                        move = 1
                        self.player_move = 0


ttt = TicTacToe()
ttt.user_letter()
ttt.game_loop()
