import itertools
import string
import time
import math
import multiprocessing as mp

class bruteForce:
	def __init__(self):
		self.charList = 'abcdefghijklmnopqrstuvwxyz'
		self.password = 'qwerty'
		self.password_length = len(self.password)
		self.limit = math.pow(len(self.charList),self.password_length)/26
		self.startedTime = time.clock()

	def check_password(self,item):
		item = ''.join(item)
		# print(item)
		# self.writeInFile(item)
		if item == self.password:
			print('result:'+item)
			return True
		return False

	def writeInFile(self,item):
		with open('out','a') as f:
				f.write(item+'\n')

	def doWork(self,charList):
		# print(current_thread().name)
		combinations = itertools.islice(itertools.product(charList,repeat =self.password_length),int(self.limit))
		for combination in combinations:
			# print(combination)
			if self.check_password(combination):
				print(time.clock()-self.startedTime)


			
	def startThreads(self):
		for i in range(1,len(self.charList)+1):
			if i == 1:
				t = mp.Process(target=self.doWork,args=(self.charList,))
			else:
				t = mp.Process(target=self.doWork,args=(self.charList[i-1:] + self.charList[:i-1],))
			# self.charList = self.charList[1:] + self.charList[:1]
			t.start()

# start = time.clock()
tool = bruteForce()
tool.startThreads()
# print(time.clock()-start)
# print('generari:'+str(tool.totalCombinations))
# print('limita:'+str(tool.limit))