# https://realpython.com/python-sockets/
# https://stackoverflow.com/questions/38412887/how-to-send-a-list-through-tcp-sockets-python
# https://docs.python.org/2/library/pickle.html
# https://www.pythoncentral.io/how-to-pickle-unpickle-tutorial/

import socket
import pickle


def main():
    host = ''
    port = 8888

    s = socket.socket()
    s.bind((host,port))

    s.listen(10)
    c, addr = s.accept()

    print('Connection from : ', addr)

    while True:
        data = pickle.loads(c.recv(2014))
        if not data:
            break

        _sum = 0
        for i in range(0,len(data)):
            _sum += data[i]

        c.sendall(str(_sum).encode('utf-8'))

    c.close()


if __name__ == '__main__':
    main()
