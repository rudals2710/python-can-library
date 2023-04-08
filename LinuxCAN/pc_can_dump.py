import sys
from pc_can import Can
def main(dev):
    can=Can(dev)
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
