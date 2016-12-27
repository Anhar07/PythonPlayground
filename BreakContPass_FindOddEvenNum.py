#4.4: Brak and continue Statements, and else Clasues on looops
for n in range(2, 10):
	#the range 2 to 10
	for x in range(2, n):
		#(2, 3), (2, 4), (2, 5) <<like that
		if n % x == 0:
			#3 % 2 = 1, 4 % 2 = 0 etc
			print(n, 'equals', x, '*', n//x) #ignores remainder
			#n equal 2 times "n//x?" 4 // 2 = 0
			break
			#w/o break it woould repeat
		else:
			print(n, 'is a prime number')
			break #ends loop and goes to next

#Practicing up : Determin if divisible by 2
print("B R E A K  O F F")
for x in range(0, 20):
	for y in range(2, x):
		if x % y == 0:
			print(x, 'is equal to', y, '*', x//y )
			break
		else:
			print(x, 'is a prime number')
			break
print("B")
print("O")
#continue
for num in range(2, 10):
	if num % 2 == 0:
		print('Found an even number', num)
		continue #if num % 2 does not equal 0, u contiue
		#continue = go to next command
		#next statement runs then
	print('Found an odd number', num) #indenting is important
	#indent bc print belonds to "for" not "if"

#Another practice ana
for i in range(0, 50):
	for k in range(2, i):
		if i % k == 0:
			print(i, "is equal to", k, '*', i//k)
			break
		else:			
			break
#4.5 Pass Statements

while True:
	pass #it does nothing

class MyEmptyClass: #used for minimal class
	pass

def initlog(*args):
	pass # i dont understand the point of this
