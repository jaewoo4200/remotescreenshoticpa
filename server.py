# 제작자 : 20614 이재우
# 이 프로그램은 원격으로 상대방의 컴퓨터에 접속하여 명령 실행 상태로 만든 후, 스크린샷 명렁어를 입력하여 상대방의 현재 상황을 파악하고, 사진 파일을 원격으로
# 불러들어와 볼 수 있게 할 수 있습니다. 간단하게 말하자면, 원격 접속을 통하여 상대의 컴퓨터 상황을 모니터링 할 수 있습니다.
# 이 프로그램은 원격 접속을 통하여 상대방의 컴퓨터의 문제점을 파악하거나, 불법적인 행동을 미연에 방지하게 하는 역할을 수행할 수 있습니다.
# 제 깃허브 페이지에 올려놓았으므로 이 주소로 들어가시면 볼 수 있습니다.
# https://github.com/jaewoo4200/remotescreenshoticpa/
# 이 프로그램은 중계서버(relay server)를 가지고 있지 않기 때문에 TeamViewer와 같이 아주 멀리 떨어진 환경에서는 작동하지 않으며,
# 같은 공유기 안에 서버 컴퓨터와 클라이언트 컴퓨터가 연결되어야지만 가능합니다.
# 이 프로그램의 테스트 환경은 노트북(제 맥북프로_macOS 10.14, 윈도우 10)기준으로 진행되었습니다.
# 이 프로그램은 서버 프로그램입니다.

# Made by Drony420
# This program can remotely connect to other person's computer, placing it into the command-running state and
# executes screenshots script. It can monitor the client computer's current situation, retrieve and view picture
# files remotely. As a simple word, you can monitor your client's computer's situation over a remote connection.
# Remote access allows this program to identify problems on the other person's computer or to prevent illegal behavior.
# This program is a server program.

# 참고 출처 / Reference: http://yujuwon.tistory.com/entry/파이썬-외부-실행-결과-저장하기
# 참고 출처 / Reference : https://realpython.com/python-sockets/
# 참고 출처 / Reference : https://docs.python.org/3.7/library/socket.html
# 참고 출처 / Reference : https://soooprmx.com/archives/8737
# 참고 출처 / Reference : http://slays.tistory.com/45
# 참고 출처 / Reference : https://docs.python.org/3.4/library/socketserver.html

import socket
import sys


# 소켓 생성(Creating socket)
def create_socket():
    try:
        global host
        global port
        global s
        host = str(host_input)
        # host = '192.168.0.7'
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as error_msg:
        print("소켓 생성 에러 / Error has occurred while creating socket." + str(error_msg))


# 소켓 바인딩 및 클라이언트 연결 대기(Binding socket and waiting for the connection of client)
def bind_socket():
    try:
        global host
        global port
        global s
        print("소켓을 포트에 바인딩하는 중 / Binding socket to the port " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as error_msg:
        print("소켓 바인딩 에러 / Error has occurred while binding socket " + str(error_msg))
        print("\n")
        print("재시도 중... / Retrying...")
        bind_socket()


# 클라이언트와 연결(Establishing a connection with client)
def accept_socket():
    conn, address = s.accept()
    print("연결 성공 / Connection successfully established")
    print("IP : " + address[0])
    print("Port : " + str(address[1]))
    send_command(conn)
    conn.close()


# 명령 전송(Sending commands)
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            response_client = str(conn.recv(2048), "utf-8")
            print(response_client, end="")


# 메인 함수(Main)
def main():
    create_socket()
    bind_socket()
    accept_socket()


print('서버 프로그램 구동 시작')
host_input = input('접속 서버의 아이피를 입력하세요(ex. 192.168.0.7) : ')
main()
