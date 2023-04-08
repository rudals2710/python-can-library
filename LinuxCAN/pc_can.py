import can

class Can:
    def __init__(self, dev='can0'):
        self.bus=can.interface.Bus(channel=dev,bustype='socketcan',bitrate=500000)

    def filter(self,id,mask=0x7FF):
        self.bus.shutdown()

    def send(self,id,payload):
        msg=can.Message(arbitration_id=id,data=payload,is_extended_id=False)
        self.bud.send(msg)

    def recv(self,timeout=0.0):
        msg=self.bus.recv(timeout=timeout)
        if msg:
            return(msg.arbitration_id,msg.dlc,list(msg.data))
        else:
            return(None,None,None)