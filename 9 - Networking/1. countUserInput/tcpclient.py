import socket
import pickle
import sys
import traceback


def main():
    host = ''
    port = 8888
    s = socket.socket()

    try:
        s.connect((host, port))
    except:
        print('Connection error' + str(sys.exc_info()))
        traceback.print_exc()
        sys.exit()

    print('Enter \'q\' to exit')

    _input = input('-> ')
    while _input != 'q':

        data = pickle.dumps(list(_input))
        s.sendall(data)

        data = s.recv(1024).decode('utf-8')
        print("Returned Sum: " + data)

        _input = input('-> ')

    s.close()


if __name__ == '__main__':
    main()


