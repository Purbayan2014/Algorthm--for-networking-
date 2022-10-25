class pck:
	def __init__(self, idx, sz=1000):
		self.idx = idx
		self.sz = sz
		self.coll_cnt = 0
	
	def incr_coll(self):
		self.coll_cnt += 1

