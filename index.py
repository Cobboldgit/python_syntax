# ==== Global Variables ==== #

# variable created outside a function
# is a global variable
from math import fabs
import random


x = 'awesome'


def myFunction():
    print('Python is ' + x)


def myFunction2():
    x = 'Great'
    print('Python is ' + x)


# print(x)


def myFunction3():
    global x  # global keyword
    x = 'Nice'
    print('Python is ' + x)


# print(x)


# ==== Data types ==== #

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

a = 'hello world'  # str
b = '20'  # int
c = 20.5  # float
d = 1j  # complex
e = ['a', 'b', 'c']  # list
f = ('a', 'b', 'c')  # tuple
g = range(6)  # range
h = {'name': 'John', 'age': 26}  # dict
i = {'John', 'Augustine', 26}  # set
j = frozenset({'a', 'b', 'c'})  # frozenset
k = True  # bool
l = b'Hello'  # bytes
m = bytearray(6)  # bytearray
n = memoryview(bytes(5))  # memoryview
o = None  # Nonetype

# random numbers
# print(random.randrange(1, 10))

# ==== Python strings ==== #
a = ''' Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''

# print(a)

# === Looping through a string ==== #
# for x in a:
# print(x)

# ==== string length ==== #
# print(len(a))

# ==== check string ==== #

# print('lorem' in a)
# if 'lorem' in a:
#     print("Yes, it's in")

# if 'lorem' not in a:
#     print("It's not in")


# ==== Slicing Strings ==== #

# print(a[0:5])
# print(a[:5]) # :5 slices from start
# print(a[6:]) #7: slices from index 7
# print(a[-5:])


# ==== strings Modifying ==== #

# print(a.strip()) #remove whitespaces
# print(a.replace('l', 'L')) # replacing string

# ==== Concatenation === #

# you cannot join string and number like 'string' + 4

txtToConc = 'I want {} pieces of item {} for {} dollars.'
# print(txtToConc.format(3, 567, 49.95, 1))

myOrder = 'I want {2} bags of {1} at {0} dollars'
# print(myOrder.format(5, 'rice', 2))


# ==== Escape Characters ==== #

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# ==== Lists ==== #

myList = ['a', 'c', 'b', 'd']

# if 'b' in myList: 
#     myList.insert(3,'e')
#     print(myList)
# myList.insert(4, 'e')
# print(myList)

# myList.remove('b')
# print(myList)

# myList.append('e')
# print(myList)

# myList.extend(e)
# print(myList)

# myList.pop(2)
# print(myList)

# myList.pop()
# print(myList)

# del myList[0]
# print(myList)

# del myList delete the entire variable
# print(myList)

# myList.clear() this clears the items
# print(myList)


# ==== Loop lists ==== #

# for x in myList:
#     print(x)

# for x in range(10):
#     print(x)

# i = 0
# while i < len(myList):
#     print(myList[i])
#     i = i + 1

# [print(x) for x in myList] short way to loop

# newList = [x for x in myList if 'a' in x]
# print(newList)

# print([x for x in range(10)])


# ==== dictionaries ==== #

thisDict = {
    'name': 'Augustine Cobbold',
    'age': 20,
    'school': 'Codetrain'
}

print(thisDict.keys())

   