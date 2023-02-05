import socket
import sys

def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    server_address = './socket_file'
    buffer_size = 1024

    try:
        sock.connect(server_address)
        print('Connected')
    except socket.error as err:
        print(err)
        sys.exit(1)

    while True:
        # データ送信
        message = input('To server: ')
        sock.sendall(message.encode())

        # データ受信
        data = sock.recv(buffer_size)
        data_str = data.decode('utf-8')
        print('From server: ' + data_str)

        # 切断コマンド
        if message == 'exit':
            sock.close()
            print('Disconnected')
            break

if __name__ == '__main__':
    main()