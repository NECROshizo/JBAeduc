# write your code here
def check(x, y, oper):
    msg = ''
    if all([is_one_digit(x), is_one_digit(y)]):
        msg += msg_6
    if all([x == 1 or y == 1, oper == '*']):
        msg += msg_7
    if all([x == 0 or y == 0, oper in ['*', '-', '+']]):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def is_one_digit(x):
    output = False
    if all([x > -10, x < 10, x.is_integer()]):
        output = True
    return output


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def division(a, b):
    # if b == 0:
    #     print(msg_3)
    #     return
    return a / b


metod = {'+': plus, '-': minus, '*': multi, '/': division}
memory, flag = '0', True

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_dict = {
    10: "Are you sure? It is only one digit! (y / n)",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
    12: "Last chance! Do you really want to embarrass yourself? (y / n)"
}

while flag:
    print(msg_0)
    x, oper, y = input().split()

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    if not all([x.replace('.', '', 1).isdigit(), y.replace('.', '', 1).isdigit()]):
        print(msg_1)
    elif oper not in ['+', '-', '*', '/']:
        print(msg_2)
    elif oper == '/' and float(y) == 0:
        check(float(x), float(y), oper)
        print(msg_3)
    else:
        check(float(x), float(y), oper)

        result = metod[oper](float(x), float(y))
        print(result)

        flag_1 = True
        while flag_1:
            print(msg_4)
            answer = input()
            if 'y' == answer:
                if is_one_digit(result):
                    msg_index = 10
                    while msg_index < 13:
                        print(msg_dict[msg_index])
                        answer = input()
                        if 'y' == answer:
                            msg_index += 1
                        elif 'n' == answer:
                            flag_1 = False
                            break
                    else:
                        memory = str(result)
                        flag_1 = False
                else:
                    memory = str(result)
                    flag_1 = False
            elif 'n' == answer:
                flag_1 = False

        while True:
            print(msg_5)
            answer = input()
            if 'y' == answer:
                break
            elif 'n' == answer:
                flag = False
                break
