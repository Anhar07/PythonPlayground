#4.6 Defining Functions 
#Arbitrary : Based o random choice

def fib(n): #defining a function 
#Fibonacci series is starting
	a, b = 0, 1  #defining variables
	while a < n: #while a is smaller than fib(n)
		print(a, end=' ') #end makes it stay on same line
		a, b = b, a+b
	print()
fib(20)




#fib2
def fin(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result 


fin(100)
