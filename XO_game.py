from packages.XO_package import XO

board = XO()

player = 'O'

board.show_board()
x = 1
while True:
    for i, item in enumerate(board.board):
        if board.chack(i):
            break
    else:
        board.massage('this game has not winner!')
        break
    if board.chack_winner()[0]:
        board.massage('Player ' + board.chack_winner()[1] + ' won')
        break
    room = board.select_room()
    if room == 'exit':
        board.massage('exit in game with player -> ' + board.player)
        break
    if board.move(room):
        if board.player == 'X':
            board.player = 'O'
        else:
            board.player = 'X'

    x += 1