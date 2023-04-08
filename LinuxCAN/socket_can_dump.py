import sys
from socket_can import SocketCan

def main(dev):
    can=SocketCan(dev)

    while True:
        id,dlc,payload = can.recv()

        print('%s %X\t[%X]'%(dev,id,dlc),end='')
        for d in payload:
            print("%02X"%(d), end='')
        print()

if __name__ =='__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        pass