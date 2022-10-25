import numpy as np
from pckt_struct import pck

class nd_struct:
   
       def __init__(self, idx, lamb):
            self.idx = idx
            self.lambval = lamb
            self.packet = None
            self.status = "Ready for transmission"
            self.bck_offline = 0
            self.trans_init_time = 0
            self.pck_cnt = 1 


       def trans_st(self, curr_time):
          self.status = "Transmission in progress"
          self.packet = pck(self.pck_cnt)
          self.pck_cnt += 1
          self.trans_init_time = curr_time

       def re_trans(self, curr_time):
            self.status = "Transmission in progress"
            self.trans_init_time = curr_time 

       def stp_trans(self, reason="Ready for transmission"):
            self.status = reason

       def check_avail(self):
            return np.random.poisson(self.lambval) == 1

       def call_back_time(self, nw):
            self.packet.incr_coll()
            high_val = (2**self.packet.coll_cnt) - 1
            if high_val > 8:
                high_val = 8 
            self.bck_offline = nw.curr_time + (np.random.randint(0, high=high_val) * nw.slt_time)
            print("Node ", self.idx, "Packet idx ", self.packet.idx,  "Packet collision count = ", self.packet.coll_cnt, \
                    "backoff = ", self.bck_offline)


       def operator(self, nw):
            if self.status == 'Ready for transmission' and self.check_avail():
                self.trans_st(nw.curr_time)
            elif self.status == 'Transmission in progress':
                if self.trans_init_time + nw.tt + nw.tp  < nw.curr_time:
                    self.status == 'Ready for transmission'
                    self.trans_init_time = 0
            elif self.status == 'Collision detected':
                self.call_back_time(nw)
                self.status = 'Waiting'
            elif self.status == 'Waiting' and self.bck_offline <= nw.curr_time:
                self.re_trans(nw.curr_time)

