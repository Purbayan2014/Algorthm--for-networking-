from nd_struct import nd_struct
from net_struct import nt_struct
import time

slt_time = 10
l = 5
mx_time = int(input('Enter the max time : '))
pt1 = nt_struct(slt_time, mx_time)
nd1 = nd_struct(1, l/slt_time)
nd2 = nd_struct(2, l/slt_time)
while(1):
  pt1.run(nd1, nd2)
  time.sleep(1)
