Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #Chapter Four Control Flow Tools


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
... >>> >>> ... Please enter an interger: Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: invalid literal for int() with base 10: 'f x < 0:'
>>> x = int(input("enter integer"))
enter integerTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '\tx = 0'
>>> print("hello world")
hello world
>>> 