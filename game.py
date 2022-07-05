from random import randint


def name_turn(names_list, f_index):
    row = f_index
    while True:
        yield names_list[row % 2]
        row += 1


def start_pencil():
    print('How many pencils would you like to use:')
    while True:
        try:
            result = int(input())
            assert result >= 0
        except (ValueError, AssertionError):
            print('The number of pencils should be numeric')
        else:
            if result != 0:
                return result
            else:
                print('The number of pencils should be positive')


def start_player(names_list):
    print(f'Who will be the first ({names_list[0]}, {names_list[1]}):')
    while True:
        try:
            result = input()
            assert result in names_list
        except AssertionError:
            print(f'Choose between {names_list[0]} and {names_list[1]}')
        else:
            return result


def put_pensil(rest_pencils):
    while True:
        try:
            result = int(input())
            assert result in [1, 2, 3]
        except (ValueError, AssertionError):
            print("Possible values: '1', '2' or '3'")
        else:
            if result > rest_pencils:
                print('Too many pencils were taken')
            else:
                return result


def game_bot(pencil, player_turn):
    while pencil > 0:
        print('|' * pencil)
        player = next(player_turn)
        print(f"{player}'s turn:")
        if player == 'Jack':
            put = pencil % 4 - 1
            if pencil == 1:
                put = 1
            elif put == 0:
                put = randint(1, 3)
            elif put < 0:
                put = 3
            print(put)
            pencil -= put
        else:
            pencil -= put_pensil(pencil)
    return f'{next(player_turn)} won!'


names = ['John', 'Jack']
pencils = start_pencil()
first = start_player(names)
turn = name_turn(names, names.index(first))
print(game_bot(pencils, turn))
