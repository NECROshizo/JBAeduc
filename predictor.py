from random import randint


def string_equl(period: int = 100) -> str:
    str_equl = ''
    while len(str_equl) <= period:
        print('Print a random string containing 0 or 1:')
        str_equl += ''.join(filter(lambda x: x in ['0', '1'], list(input())))
        if len(str_equl) < period:
            print(f'Current data length is {len(str_equl)}, {period - len(str_equl)} simbols left')
    print('Final data string:\n' + str_equl)
    return str_equl


def make_equl(string: str, dict_triad: dict = dict()) -> dict:
    # dict_triad = dict()
    # for string in args:
    for a, b, c, n in zip(string[:-3], string[1:-2], string[2:-1], string[3:]):
        if int(n):
            dict_triad.setdefault(a + b + c, [0, 0])[1] += 1
        else:
            dict_triad.setdefault(a + b + c, [0, 0])[0] += 1
    return dict_triad


def string_prediction(equl: dict, italon: str, ) -> str:
    prediction = ''.join([str(randint(0, 1)) for _ in range(3)])

    for ch in range(3, len(italon)):
        basa = equl.get(italon[ch - 3:ch])
        if basa and basa[0] != basa[1]:
            prediction += str(basa.index(max(basa)))
        else:
            prediction += str(randint(0, 1))
    return prediction


def compar_string(one_str: str, two_str: str) -> int:
    won = 0
    for one, two in zip(one_str[3:], two_str[3:]):
        if one == two:
            won += 1
    print('prediction:')
    print(two_str)
    print(
        f'Computer guessed right {won} out of {len(one_str[3:])} symbols ({round(won * 100 / (len(one_str) - 3), 2)}%)')
    return len(one_str[3:]) - 2*won


def game_predictor(dict_equil: dict) -> None:
    cash = 1000
    print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
    print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')
    while True:
        print('Print a random string containing 0 or 1:')
        user_in = input()
        if user_in == 'enough':
            break
        user_string = ''.join([i for i in user_in if i in ['0', '1']])
        comp_string = string_prediction(dict_equil,user_string)
        profit = compar_string(user_string, comp_string)
        cash += profit
        dict_equil = make_equl(string_in, dict_equil)
        print(f'Your balance is now ${cash}')
    print('Game over!')

string_in = string_equl()
# string_in = '010100100101010101000010001010101010100100100101001011010001011111100101010100011001010101010010001001010010011'
uq_dict = make_equl(string_in)
game_predictor(uq_dict)

