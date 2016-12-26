#4.6 Defining Functions 
#Arbitrary : Based o random choice

def fib(n): #defining a function 
#Fibonacci series is starting
	a, b = 0, 1  #defining variables
	while a < n: #while a is smaller than fib(n)
		print(a, end='') 
		a, b = b, a+b
	print(9)
print(fib(100))
print('Hello World')bv m nrv