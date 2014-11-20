import rpyc

def Main():
	n = eval(input("Please enter a number: "))

	for x in range(3,n+1):
		if c.root.isPrime(x):
			print(x)


c = rpyc.connect("150.250.135.238", 12345)
Main()
