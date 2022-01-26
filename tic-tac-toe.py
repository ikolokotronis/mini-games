
class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(10)]
        self.game_over = False

    def game_loop(self):
        while self.game_over == False:
            self.print_board()
            self.user_input()
            if self.isWinner("X"):
                self.print_board()
                print('Player X won!')
                self.game_over = True
            elif self.isWinner("O"):
                self.print_board()
                print('Player O won!')
                self.game_over = True

    def isWinner(self, player):
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

    def user_input(self):
        user_input = input("Choose your position (ex. X,6): ").upper()
        user_input_split = user_input.split(',')
        
        get_letter = user_input_split[0]
        get_position = int(user_input_split[1])
        if self.check_if_space_is_free(get_position):
            self.insert_letter(get_letter, get_position)
        else:
            print('')
            print("Position is taken!")
            print('')


ttt = TicTacToe()
ttt.game_loop()

