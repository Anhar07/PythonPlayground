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
print(words[:])
for i in words:		#it doesnt matter what letter you use as long as it is consistent
	print(i, len(i)) #i = words. so it prints cat 3, pretty cool
#another for statement
for w in words [:]: #i guess it is for looping list
	if len(w) > 6: #command
		words.insert(0, w) #.insert() for any LISTS
print(words)

#Range() function

for i in range(5): #iterating
	print(i)

print ("BR E SA K  O F F")

for i in range(0, 10, 3): #called a step
	print(i)

print ("BR E SA K  O F F")

for i in range(5,9): #called a step
	print(i)

print ("BR E SA K  O F F")

for i in range(-10, -100, -30): #i dont understand why theres 3 but i'm feeling lazy spppp yeah
	print(i)






