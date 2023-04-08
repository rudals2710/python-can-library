# Linux CAN 통신 #

### python-can 라이브러리 ###

수신 버퍼 관리, 필터 추상화, 스레드 안정성 지원 -> 소켓 모듈 대신 권장
리눅스와 윈도우 운영체제 지원
- 리눅스 : 커널에서 제공하는 SocketCAN 사용
- 윈도우 : CAN 컨트롤러 드라이버 설치 필요


설치
```python
sudo pip install python-can
```

모듈 로드
```python
import can
```
클래스
- can.interface.Bus : CAN 버스에 대한 추상화 제공
```python
bus=can.interfaces.Bus(channel='인터페이스 이름', bustype='socketcan', bitrate=500000)
```
- can.Message : CAN 메시지에 대한 추상화 제공
``` python
msg = can.Message(arbitration_id = 0x200 data=[0x10, 0x20, 0x30, 0x40] is_extended_id=False)
```

CAN 프레임 수신
