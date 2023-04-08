import can

class Can:
    def __init__(self, dev='can0'): # can.interface.Bus 객체 생성
        self.bus=can.interface.Bus(channel=dev,bustype='socketcan',bitrate=500000)

    def __del__(self):
        self.bus.shutdown()
        
    def filter(self,id,mask=0x7FF):
        self.bus.set_filters([{'can_id':id,"can_mask":mask}])

    def send(self,id,payload):
        msg=can.Message(arbitration_id=id,data=payload,is_extended_id=False)
        self.bud.send(msg)

    def recv(self,timeout=0.0):
        msg=self.bus.recv(timeout=timeout)
        if msg:
            return(msg.arbitration_id,msg.dlc,list(msg.data))
        else:
            return(None,None,None)
