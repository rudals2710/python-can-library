import socket
import struct
class SocketCan:
    def __init__(self,dev):
        self.s =socket.socket(socket.AF_CAN, socket.SOCK_RAW,socket.CAN_RAW)
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.s.bind((dev,))

    def __del__(self):
        self.s.close()

    def send(self,id,payload):
        frame=struct.pack("=IB3x8s",id,len(payload),data.ljust(8,b'\x00')) #kernel frame 으로 바꿔 send
        self.s.send(frame)

    def recv(self):
        frame,addr=self.s.recvfrom(struct.calcsize("=IB3x8s")) # rexvfrom을 이용해서 구조체 길이만큼 kernel로 가져옴
        id,dlc,payload=struct.unpack("=IB3x8s",frame)
        return(id,dlc,list(payload[:can_dlc]))
