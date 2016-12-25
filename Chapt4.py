#Chapter Four Control Flow Tools


#if statements
x = int(input("Please enter an interger: "))
if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('single')
else:
	print('more')
#practicing if statements more
x = str(input("What is your name? "))
if x == 'jack':
	print("short name")
else:
	print("cool")

#For Statements
#MEasuring strings
words = ['cat', 'window', 'defenestrate']
for i in words:		#it doesnt matter what letter you use as long as it is consistent
	print(i, len(i)) #i = words. so it prints cat 3, pretty cool
#another for statement
