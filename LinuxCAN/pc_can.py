import can

class Can:
    def __init__(self, dev='can0'): # can.interface.Bus 객체 생성
        self.bus=can.interface.Bus(channel=dev,bustype='socketcan',bitrate=500000)

    def __del__(self): # Bus,shutdown()을 호출해 통신 중단
        self.bus.shutdown()
        
    def filter(self,id,mask=0x7FF): # id와 mask를 인자로 수신 필터 설정
        self.bus.set_filters([{'can_id':id,"can_mask":mask}]) # 딕셔너리의 'can_id'와 'can_mask'키에 대응하는 값으로 id와 mask를 설정한 후 리스트 객체에 포함에 bus.set_filters()의 인자로 전달
    

    def send(self,id,payload): # id와 payload를 인자로 Bus객체를 이용해 CAN 프레임 전송
        msg=can.Message(arbitration_id=id,data=payload,is_extended_id=False) # id와 payload로 can.Messafe 객체 생성
        self.bud.send(msg) # Message 객체를 Bus.send()인자로 전달해 CAN 버스에 프레임 전송

    def recv(self,timeout=0.0): # time_out을 인자로 Bus 객체를 통해 수신한 CAN 프레임 반환
        msg=self.bus.recv(timeout=timeout) # bus.recv()로 time_out시간동안 대기하며 수신한 데이터 반환
        # 반환 결과는 튜플로 id,dlc, payload
        # 시간 초과면 튜플로 none, none, none 반환
        if msg: 
            return(msg.arbitration_id,msg.dlc,list(msg.data))
        else:
            return(None,None,None)
