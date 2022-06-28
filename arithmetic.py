import random as r


def calculation(a, b=2, sign='**'):
    def plus(a, b):
        return a + b

    def minus(a, b):
        return a - b

    def multi(a, b):
        return a * b

    def degree(a, b):
        return a ** b

    metod = {'+': plus, '-': minus, '*': multi, '**': degree}

    return metod[sign](a, b)


def correct_format(a=-10 ** 5, b=10 ** 5):
    while True:
        try:
            user_input = int(input())
            assert user_input >= a and user_input <= b
            break
        except (ValueError, AssertionError):
            print('Incorrect format.')
    return user_input


def test(lvl: int, count: int = 5) -> int:
    def one():
        a, b, sign = r.randint(2, 9), r.randint(2, 9), r.choice(['+', '-', '*'])
        print(f'{a} {sign} {b}')
        return calculation(a, b, sign)

    def two():
        a = r.randint(11, 29)
        print(a)
        return calculation(a)

    lvl_type = {1: one, 2: two}
    correct = 0

    for _ in range(count):
        solution = lvl_type[lvl]()
        solution_user = correct_format()
        if solution_user == solution:
            print('Right!')
            correct += 1
        else:
            print('Wrong!')
    return correct


def write_file(correct, lvl, description):
    print('What is your name?')
    name = input()
    with open('results.txt', 'a') as f:
        print(f'{name}: {correct}/5 in level {lvl} ({description}).', file=f)
    print('The results are saved in "results.txt".')

lvl_description = {1: 'simple operations with numbers 2-9', 2: 'integral squares 11-29'}

print('Which level do you want? Enter a number:')
print(' - '.join(map(str, list(lvl_description.items())[0])))
print(' - '.join(map(str, list(lvl_description.items())[1])))
lvl = correct_format(1, 2)
correct = test(lvl)
print(f'Your mark is {correct}/5 Would you like to save the result? Enter yes or no.')
if input() in ['yes', 'YES', 'y', 'Yes']:
    write_file(correct, lvl, lvl_description[lvl])
