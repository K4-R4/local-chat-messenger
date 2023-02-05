import faker
import os
import socket

def main():
    fake = faker.Faker()
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    server_address = './socket_file'
    buffer_size = 1024

    # ファイルが既に存在しないことを確認する
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    # ソケットをアドレスに紐付ける
    print('Starting up on {}'.format(server_address))
    sock.bind(server_address)

    sock.listen(1)

    # クライアントからの接続を処理する
    while True:
        connection, client_address = sock.accept()
        print('Connected with client')

        while True:
            try:
                # データの受信
                data = connection.recv(buffer_size)
                data_str = data.decode('utf-8')
                print('From client: ' + data_str)

                # データの送信
                response = fake.text()
                connection.sendall(response.encode())
            except BrokenPipeError:
                connection.close()
                sock.close()
                break

            # 切断コマンド
            if data_str == 'exit':
                connection.close()
                print('Disconnected')
                break

if __name__ == '__main__':
    main()