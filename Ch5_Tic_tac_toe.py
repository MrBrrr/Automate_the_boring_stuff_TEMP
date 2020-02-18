
toeBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])


def get_coordinate(user_name, board):
    while 1:
        print('User (' + user_name + ') - your move: ')
        try:
            coordinate = str(input())
            if coordinate not in board.keys():
                print( 'Proper coordinates are: '+ str(board.keys()) )
                continue
            else:
                if board[coordinate] == ' ':
                    break
                else:
                    print('Already used')
                    print_board(board)
                    continue
        except NameError:
            print( 'Proper coordinates are: ' + str(board.keys()))
            continue
        
    toeBoard[coordinate] = user_name


for i in range(0, 9):
    get_coordinate('O', toeBoard)
    print_board(toeBoard)
    get_coordinate('X', toeBoard)
    print_board(toeBoard)
    

# spr czy pole jest juz uzupelnione przez innego gracza
# dodaj opcje wygranej
