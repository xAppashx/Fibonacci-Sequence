

def Fibonacci(n):
	Value1 = 1
	Value2 = 1
	Value3 = 0
	
	if (n >= 1):
		print(1)
	#
	
	if (n >= 2):
		print(1)
	#
	
	if (n > 2):
		for Loop in range(n - 2):
			Value3 = Value1 + Value2
			Value1, Value2 = Value2, Value3
			print(Value3)
		#for Loop
	#if n > 2
	
#def Fibonacci




def Main():
	
	print("Up to which value would you like the sequence to go: ", end = "")
	n = int(input())
	
	Fibonacci(n)
	
#def Main

Main()
