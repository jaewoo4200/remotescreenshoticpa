# 제작자 : 20614 이재우
# 이 프로그램은 원격으로 상대방의 컴퓨터에 접속하여 명령 실행 상태로 만든 후, 스크린샷 명렁어를 입력하여 상대방의 현재 상황을 파악하고, 사진 파일을 원격으로
# 불러들어와 볼 수 있게 할 수 있습니다. 간단하게 말하자면, 원격 접속을 통하여 상대의 컴퓨터 상황을 모니터링 할 수 있습니다.
# 이 프로그램은 원격 접속을 통하여 상대방의 컴퓨터의 문제점을 파악하거나, 불법적인 행동을 미연에 방지하게 하는 역할을 수행할 수 있습니다.
# 제 깃허브 페이지에 올려놓았으므로 이 주소로 들어가시면 볼 수 있습니다.
# https://github.com/jaewoo4200/remotescreenshoticpa/
# 이 프로그램은 중계서버(relay server)를 가지고 있지 않기 때문에 TeamViewer와 같이 아주 멀리 떨어진 환경에서는 작동하지 않으며,
# 같은 공유기 안에 서버 컴퓨터와 클라이언트 컴퓨터가 연결되어야지만 가능합니다.
# 이 프로그램의 테스트 환경은 노트북(제 맥북프로_macOS 10.14, 윈도우 10)기준으로 진행되었습니다.
# 이 프로그램은 클라이언트의 화면 캡쳐 프로그램입니다.

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

# 이 프로그램은 실행하기 전, pip install image를 입력하여야지만 실행 가능합니다.

from PIL import ImageGrab
screenshot = ImageGrab.grab()
savefile = 'sc.jpg'
screenshot.save(savefile)
