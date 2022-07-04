import json
import re


def post_verification_busstop(structure, referens, *args):
    for item in args:
        for bus in structure[referens].keys():
            if bus not in list(structure[item].keys()):
                return bus
            elif len(structure[item][bus]) != 1:
                return bus
    return None


def sum_sets(li):
    result = set()
    for item in li:
        result.update(item)
    return sorted(list(result))


def intersection_sets(li):
    result = set()
    queue = li[:]
    while queue:
        var = queue.pop()
        for target in queue:
            result.update(var & target)
    return sorted(list(result))


def time_compare(first, second):
    first_hour, first_minutes = map(int, first.split(':'))
    second_hour, second_minutes = map(int, second.split(':'))
    if first_hour < second_hour:
        return True
    elif first_hour == second_hour and first_minutes < second_minutes:
        return True
    else:
        return False


# with open('base.json') as f:
#     # with open('base2.json') as f:
#     base_date = json.load(f)
# json_str = '[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street Str.", "next_stop" : "11", "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : 9, "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  {"bus_id" : 128, "stop_id" : "five", "stop_name" : "Bourbon street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  {"bus_id" : "", "stop_id" : "", "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : 23.9, "a_time" : 8},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : "", "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : 34.6, "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : "eleven", "stop_id" : 16, "stop_name" : "Sunset Boullevard", "next_stop" : 17.4, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska St.", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Av.", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : 3, "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : "21", "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : 13.01},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "FF", "a_time" : ""},  {"bus_id" : "", "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]'
# json_str = '[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "abbey Road", "next_stop" : 5, "stop_type" : "FF", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "two"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street Str.", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "39:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:95"},  {"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08.13"},  {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "d", "a_time" : "08:16"},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08;44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boullevard", "next_stop" : 17, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "o", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "s", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska St.", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:76"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Av.", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00:00"},  {"bus_id" : 1024, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]'
json_str = input()
base_date = json.loads(json_str)

date_structure: dict = {"bus_id": {'type': int, 'other': 'required', 'format_': None},
                        "stop_id": {'type': int, 'other': 'required', 'format_': None},
                        "stop_name": {'type': str, 'other': 'required',
                                      'format_': r'\A([A-Z][a-z]* ){1,3}(Avenue|Street|Boulevard|Road)$'},
                        "next_stop": {'type': int, 'other': 'required', 'format_': None},
                        "stop_type": {'type': str, 'other': None, 'format_': r'\b(S|O|F){1}\b'},
                        "a_time": {'type': str, 'other': 'required', 'format_': r'\A(([0-1]\d)|(2[0-4])):[0-5]\d$'}}

# err_date: dict = {'bus_id': 0,
#                   'stop_id': 0,
#                   'stop_name': 0,
#                   'next_stop': 0,
#                   'stop_type': 0,
#                   'a_time': 0
#                   }
# flag = True
# time_bus_stopped: dict = dict()
# error_line: dict = dict()
line_bus_structure: dict = {'Start stops': {}, 'All stops': {}, 'Finish stops': {}, 'On-demand': {}}

for item_base in base_date:
    # if item_base['bus_id'] not in error_line.keys():
    for key, value in item_base.items():
        if type(value) != date_structure[key]['type'] or \
                (date_structure[key]['other'] and value == '') or \
                (date_structure[key]['format_'] and (
                        not re.search(date_structure[key]['format_'], value) and value != '')):
            # right = False
            break
        else:
            # right = True
            # else:
            #     if right:
            # f_time = time_bus_stopped.setdefault(item_base['bus_id'], '00:00')
            # s_time = item_base['a_time']
            # if time_compare(f_time,s_time):
            #     time_bus_stopped[item_base['bus_id']] = s_time
            # else:
            #     error_line.setdefault(item_base['bus_id'],item_base['stop_name'])
            # проверка линий остановок
            if key == "stop_type":
                if value == 'S':
                    line_bus_structure['Start stops'].setdefault(item_base['bus_id'], set()).add(item_base['stop_name'])
                elif value == 'F':
                    line_bus_structure['Finish stops'].setdefault(item_base['bus_id'], set()).add(
                        item_base['stop_name'])
                elif value == 'O':
                    line_bus_structure['On-demand'].setdefault(item_base['bus_id'], set()).add(item_base['stop_name'])

                line_bus_structure['All stops'].setdefault(item_base['bus_id'], set()).add(item_base['stop_name'])
        # if not flag:
        #     print(f'There is no start or end stop for the line: {bus}.')
        #     break
        # line_bus.setdefault(item_base['bus_id'],set()).add(item_base['stop_name'])

    # otlad
    # print('=======================================================')
    # print(item_basa, '\n', 'stop_name =', err_date['stop_name'], 'stop_type=', err_date['stop_type'], 'a_time=',
    #       err_date['a_time'])
    # print(item_base['stop_name'],item_base['stop_type'], item_base['a_time'], '\n', 'stop_name =', err_date['stop_name'],
    #       'stop_type=', err_date['stop_type'], 'a_time=', err_date['a_time'])
    # print(item_base['stop_name'], '\n', 'stop_name =', err_date['stop_name'])
    # print(item_base['stop_type'], '\n', 'stop_type=', err_date['stop_type'])





# 1==================================================================
# print(f'Type and required field validation: {sum(err_date.values())} errors')
# print(*[f'{i}: {j}' for i, j in err_date.items()], sep='\n')

# 2==================================================================
# promo_result = {'stop_name':err_date['stop_name'],'stop_type':err_date['stop_type'], 'a_time':err_date['a_time']}
# print(f'Format validation: {sum(promo_result.values())} errors')
# print(*[f'{i}: {j}' for i, j in promo_result.items()], sep='\n')

# 3==================================================================
# print(f'Line names and number of stops:')
# print(*[f'bas_id: {key}, stops: {len(value)}' for key, value in line_bus.items()], sep='\n')

# 4==================================================================
# bus = post_verification_busstop(line_bus_structure, 'All stops', 'Start stops', 'Finish stops')
# if bus:
#     print(f'There is no start or end stop for the line: {bus}.')
# else:
#     start = sum_sets(line_bus_structure['Start stops'].values())
#     print(f"Start stops: {len(start)} {start}")
#     transfer = intersection_sets(list(line_bus_structure['All stops'].values()))
#     print(f"Start stops: {len(transfer)} {transfer}")
#     finish = sum_sets(line_bus_structure['Finish stops'].values())
#     print(f"Finish stops: {len(finish)} {finish}")

# 5==================================================================
# print('Arrival time test:')
# if error_line:
#     for key,value in error_line.items():
#         print(f'bus_id line {key}: wrong time on station {value}')
# else:
#     print('OK')

#6==================================================================
transfer = intersection_sets(list(line_bus_structure['All stops'].values()))
start = sum_sets(line_bus_structure['Start stops'].values())
finish = sum_sets(line_bus_structure['Finish stops'].values())
result = sorted(list(set(transfer+start+finish)&set(sum_sets(line_bus_structure['On-demand'].values()))))
print('On demand stops test:')
if result:
    print(f'Wrong stop type: {result}')
else:
    print('OK')