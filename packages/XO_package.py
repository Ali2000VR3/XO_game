from os import system
from colorama import init, Fore, Back, Style
init()
winnerStat = (
    (0, 1, 2), (0, 3, 6), (0, 4, 8),
    (3, 4, 5), (1, 4, 7), (2, 4, 6),
    (6, 7, 8), (2, 5, 8)
)


class XO:
    def __init__(self) -> None:
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.player = 'O'

    def chack(self, index: int) -> bool:
        if self.board[index-1] != 'X' and self.board[index-1] != 'O':
            return True
        return False

    def move(self, index: int) -> bool:
        if self.chack(index):
            self.board[index-1] = self.player
            self.show_board()
            return True
        else:
            self.show_board()
            self.massage(f'room [{index}] is full!')

    def massage(self, msg: str):
        print('\n', '-'*20)
        print(Fore.GREEN + msg.center(20) + Fore.RESET)
        print('', '-'*20, '\n')

    def chack_winner(self):
        for win in winnerStat:
            if self.board[win[0]] == 'O' and self.board[win[1]] == 'O' and self.board[win[2]] == 'O':
                return True, 'O'
            if self.board[win[0]] == 'X' and self.board[win[1]] == 'X' and self.board[win[2]] == 'X':
                return True, 'X'
        return False, ''

    def select_room(self):
        while True:
            try:
                self.massage('Player ' + self.player)
                self.massage('Please select your choice?')
                room = int(input('Select? (0 for exit): '))
                if room == 0:
                    return 'exit'
                if room > 9 or room < 1:
                    raise 'error'
                return room
            except:
                system('cls')
                self.show_board()
                self.massage('Please select valid room!')
                continue

    def show_board(self):
        system('cls')
        print(
            f'''
                -----------------
                | [{self.board[0]}]  [{self.board[1]}]  [{self.board[2]}] |
                -----------------
                | [{self.board[3]}]  [{self.board[4]}]  [{self.board[5]}] |
                -----------------
                | [{self.board[6]}]  [{self.board[7]}]  [{self.board[8]}] |
                -----------------  
            '''
        )
