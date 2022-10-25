import time

class nt_struct:
    

    def __init__(self, slt_time, mx_time):
        """
        args : 
            slt_time (int) : Slot time 
            mx_time (int) : max time
        """
        self.tp = 10 
        self.slt_time = slt_time
        self.cur_time = 0
        self.tt = 15
        self.mx_time = mx_time
        self.collision_cnt = 0


    def run(self, nd1, nd2):
        """
        args:
          nd1 (node object) : Node1
          nd2 (node object) : Node2
        """
        self.pack_trans(nd1, nd2)
        self.cur_time += 1
        if self.cur_time  == self.mx_time: 
            self.disp_stat()

    def pack_trans(self, nd1, nd2):
        """
            This method decides which node to be transmitted and checks the backoff time
            for that node if backoff time for any node is 0, then call for transmitation of the
            node
        args:
          nd1 (node object) : Node1
          nd2 (node object) : Node2
        """
        nd1.opt(self)
        nd2.opt(self)
        self.coll_detect(nd1, nd2)

        print(self.cur_time)
        print("\n Status of the first Node : ", nd1.status)
        print("\n Status of the second Node : ", nd2.status)
        print("--------------------------------------------")
        print("--------------------------------------------")
        

    def coll_detect(self, nd1, nd2):
        """
        Method used to detect whether there is a collision detection between node 1 and node 2

        args: 
            nd1 (node object) :  Node 1
            nd2 (node object) :  Node 2

        """
        if nd1.status == "Transmission in progress"  and nd2.status == "Transmission in progress":
            self.collision_cnt += 1
        nd1.stp_trans("coll")
        nd2.stp_trans("coll")

    def disp_stat(self):
        print("\n Total packets that have been transmitted from A : ", nd1.pck_cnt)
        print("\n Total packets that have been transmitted from B : ", nd2.pck_cnt)
        print("\n Total number of collisions that have been detected between nodes : ", self.collision_cnt)
        print("\n The average throughput generated from end A to end B :")
        print("\n The average throughput generated from end B to end A :")
        print("\n Simulated time period for this collision : ", self.cur_time)
