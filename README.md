# Local Chat Messenger

## __概要__
TCP通信を用いてサーバー・クライアント間でデータの送受信を行います。<br>
サーバー側ではクライアント側の入力を受信・表示し、それに返信します。<br>
クライアント側で入力を行い、サーバー側からの返信を受信・表示します。<br>
クライアント側で`exit`を入力すると接続を切断します。

### server
![image](https://user-images.githubusercontent.com/106866329/216813728-dec64c25-9c6d-4a98-a50e-c2ed8f97f4a1.png)
### client
![image](https://user-images.githubusercontent.com/106866329/216813677-c193bdef-a98b-4fa0-bdf1-134b48a328ca.png)

## __必要条件__
```
pip install -r requirements.txt
```

## __使い方__
### server
```
python3 server.py
```
### client
```
python3 client.py
```

## __参考__
[PythonソケットによるTCP通信入門](https://nayutari.com/python-socket#%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%81%B8%E5%8D%98%E7%99%BA%E9%80%9A%E4%BF%A1)<br>
[PythonでUnixドメインソケットを使って通信する](https://tokibito.hatenablog.com/entry/20150927/1443286053)<br>
[サーバー・クライアント間でのデータ送信・受信方法](https://office54.net/python/app/python-data-socket#section2)