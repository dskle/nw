# -*- coding: utf8 -*-
# 소켓 라이브러리 로딩
import socket
import threading

def handler(client, address):
    #while True:
    # 접속 승인 요청
        #client, address = s.accept()
        #print "[+] new connection from %s(%d)" % (address[0], address[1])
    # 서버가 끊기지않게 하는법
    while True:
        try:
            # 클라이언트가 전송한 데이터 수신
            data = client.recv(1024)
        except:
            print "Exception!"
            break
        if not data:
            # 데이터를 보내지 않은 클라이언트 연결 종료
            client.close()
            break
        print "address %s send data %s" % ( address[0], data)
        # 수신 데이터를 클라이언트에 전송
        client.send(data)

# 서버 정보
# *로 표현하는 경우도 있다 (와일드 카드)
info = ("0.0.0.0", 9999)
# 소켓 생성
s = socket.socket()
# 9999번 포트 바인딩
s.bind(info)
# 바인딩 포트 리스닝
s.listen(5)
while True:
    # 접속 승인 요청
    client, address = s.accept()
    print "[+] new connection from %s(%d)" % (address[0], address[1])
    th = threading.Thread(target=handler, args=(client, address))
    th.start()
