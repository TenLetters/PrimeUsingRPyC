#title		:pythonPrimes.py
#author		:Alex Ciaramella
#date		:10/22/14
#usage		:python pythonPrimes.py
import rpyc
import logging
from math import sqrt

class MyService(rpyc.Service):

	def on_connect(self):
		pass

	def on_disconnect(self):
		pass

	#isPrime(x):
	#	@param: an integer
	#	@return: True if the parameter is prime
	#		 False if the parameter is composite
	def exposed_isPrime(self, x):

		lastDivisor = int(sqrt(x))

		#loop from 2 to the last possible divisor
		for i in range(2, lastDivisor+1):

		#if x  is evenly divisible(no remainder)
		#by any number i < x, then it is not prime
		#therefore return false 
			if x%i == 0:
				return False
	#x must only be evenly divisble by itself and 1
	#and must be prime
	#therefore return True 
		return True

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	log = logging.getLogger("myLogger")
	from rpyc.utils.server import ThreadedServer
	t = ThreadedServer(MyService,hostname = 'localhost',  port = 12345)
	t.start()
