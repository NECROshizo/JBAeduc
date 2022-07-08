import sys
import os
import re
import ast


def true_path(path: str):
    # print(path)
    if os.path.isabs(path):
        if path.find('.py') != -1:
            return [path]
        return list_path(path)
    if path[0] not in ['/', '\\']:
        path = '/' + path
    if path.find('.py') != -1:
        return [os.path.join(os.getcwd() + path)]
    return list_path(os.path.join(os.getcwd() + path))


def list_path(path: str) -> list:
    list_file = []
    for dir in os.listdir(path):
        # print(dir)
        item_path = os.path.join(path, dir)

        if os.path.isdir(item_path):
            list_file = list_path(item_path)

        elif dir.find('.py') != -1:
            list_file.append(item_path)
    return sorted(list_file)


def len_long(num: int, line: str, path: str):
    if len(line.strip()) > 79:
        print(f'{os.path.relpath(path)}: Line {num}: S001 Too long')


def multiple_four(num: int, line: str, path: str):
    if (len(line) - len(line.lstrip())) % 4 and line.rstrip():
        print(f'{os.path.relpath(path)}: Line {num}: S002 Indentation is not a multiple of four')


def unnecessary_semicolon(num: int, line: str, path: str):
    if line.rstrip():
        if line.find('#') == -1:
            if line.rstrip()[-1] == ';':
                print(f'{os.path.relpath(path)}: Line {num}: S003 Unnecessary semicolon')
        else:
            line_list = line.split('#')
            if line_list[0].rstrip() and line_list[0].rstrip()[-1] == ';':
                print(f'{os.path.relpath(path)}: Line {num}: S003 Unnecessary semicolon')


def spaces_comments(num: int, line: str, path: str):
    if line.find('#') != -1:
        line_list = line.split('#')
        if line_list[0].rstrip() and (len(line_list[0]) - len(line_list[0].rstrip())) != 2:
            print(f'{os.path.relpath(path)}: Line {num}: S004 At least two spaces required before inline comments')


def to_do(num: int, line: str, path: str):
    if line.find('#') != -1:
        if 'todo' in line.lower():
            print(f'{os.path.relpath(path)}: Line {num}: S005 TODO found')


def two_blank_lines(num: int, line: str, path: str):
    global blank
    if not line.rstrip():
        blank += 1
    else:
        if blank > 2:
            print(f'{os.path.relpath(path)}: Line {num}: S006 More than two blank lines used before this line')
        blank = 0
    return blank


def many_spaces(num: int, line: str, path: str):
    constr = None
    if 'def' in line.split('#')[0]:
        constr = 'def'
    elif 'class' in line.split('#')[0]:
        constr = 'class'
    if constr and re.match('\A' + constr + ' {2,}.', line.lstrip()):
        print(f"{os.path.relpath(path)}: Line {num}: S007 Too many spaces after '{constr}'")


def camel_case(num: int, line: str, path: str):
    if 'class' in line.split('#')[0] and not re.match('\Aclass +[A-Z][a-z][a-zA-z]*[:\(]', line.lstrip()):
        print(f"{os.path.relpath(path)}: Line {num}: S008 Class name 'user' should use CamelCase")


def function_name(num: int, line: str, path: str):
    if 'def' in line.split('#')[0] and not re.match('\Adef +[_a-z0-9]+\(', line.lstrip()):
        print(f"{os.path.relpath(path)}: Line {num}: S009 Function name 'Print2' should use snake_case")


def argument_name(num: int, line: str, path: str, tree):
    if 'def' in line.split('#')[0]:
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in line.split('#')[0]:
                for x in node.args.args:
                    if not re.match('[_a-z0-9]+', x.arg):
                        print(f"{os.path.relpath(path)}: Line {num}: S010 Argument name '{x.arg}' should be snake_case")
                        break


def variable_in_function(num: int, line: str, path: str, tree):
    if line.rstrip():
        var_list = []
        var = line.lstrip().split()[0]
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # print(ast.dump(node.body[0]))
                # print(ast.dump(node.body[1]))
                var_list += [x.targets[0].id for x in node.body if
                             isinstance(x, ast.Assign) and isinstance(x.targets[0], ast.Name)]
        if var in var_list and not re.match('[_a-z][_a-z0-9]+', var):
            print(f"{os.path.relpath(path)}: Line {num}: S011 Variable '{var}' in function should be snake_case")


def argument_is_mutable(num: int, line: str, path: str, tree):
    if 'def' in line.split('#')[0]:
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in line.split('#')[0]:
                for arg in node.args.defaults:
                    if type(arg) != ast.Constant:
                        print(f"{os.path.relpath(path)}: Line {num}: S012 The default argument value is mutable.")
                        break


args = sys.argv
file_l = true_path(args[1])

# path = r'test\test_1.py'
# path = '/one/test2.py'
# path = 'one'
# path = 'test.py'
# print()
# file_l = true_path(path)

for file_py in file_l:
    blank = 0
    with open(file_py, 'r') as f:
        all_text = f.read()
        tree = ast.parse(all_text)
        # print(*[ast.dump(y) for y in fun], sep='\n')
        # print(*[ast.name for x in ast.walk(tree)], sep='\n')
        # key=dict()
        # for node in ast.walk(tree):
        #     print(ast.dump(node))
        #     if isinstance(node, ast.FunctionDef):
        #         print([node.args.args[node.args.defaults.index(x)].arg for x in node.args.defaults if type(x) != ast.Constant])
        #
        #         key.setdefault(node.name, [x.arg for x in node.args.args])
        # print(key)
        for num, line in enumerate(all_text.split('\n'), start=1):
            # print(line)
            len_long(num, line, file_py)
            multiple_four(num, line, file_py)
            unnecessary_semicolon(num, line, file_py)
            spaces_comments(num, line, file_py)
            to_do(num, line, file_py)
            two_blank_lines(num, line, file_py)
            many_spaces(num, line, file_py)
            camel_case(num, line, file_py)
            function_name(num, line, file_py)
            argument_name(num, line, file_py, tree)
            variable_in_function(num, line, file_py, tree)
            argument_is_mutable(num, line, file_py, tree)
