import sys
from socket_can import SocketCan

def main(dev): 
    can=SocketCan(dev)

    while True:
        frame=input()

        try:
            id,payload=frame.split('#',1)
        except ValueError:
            print("invalied seperator")
            continue
        I=len(payload)
        if I%2 !=0 or I>16:
            print("hexadecimal by 2 digits or more the 8 byte")
            continue
        payload=bytes([int(payload[i:i+2],16) for i in range(0,I,2)])
        can.send(int(id,16),payload)
if __name__=='__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        pass