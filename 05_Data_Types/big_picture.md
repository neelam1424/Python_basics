# Object Types / Data Types
     - Numbers : 1234,3.14,3+4j,0b111,Decimal(),Fraction()
     - String (immutable) : (String is also treated as list )'spam',"Bob's",b'a\x01c',u'sp\xc4m'
     - List :[1,[2,'three'],4.5],list(range(10))
     -Tuple :(1,'spam',4,'U'),tuple('spam'),namedtuple
     - Dictionary : {'food':'spam','taste':'yum'},dict (hours=10)
     - Set : set('abc'),{'a','b','c'}
     - File :open('eggs.txt'),open(r'C:ham.bin','wb')
     -Boolean : True, False
     -None : None
     -Functions,modules,classes
     - Advanced : Decorators, Generators, Iterators,Meta Programming

examples :- 
>>> 12 + 12
24
>>> 2.5 * 5
12.5
>>> 2 ** 4
16
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.random()
0.1862876519414074
>>> random.choice([1,2,3,4,5])
2
>>> username ="NeelamMore"
>>> len(username)
10
>>> username[0]
'N'
>>> username[0] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment  
>>> username[-1]
'e'
>>> username[-2]
'r'
>>> username[1:3]
'ee'
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']      
>>> myList=[123,"chai",3.14]
>>> mylist
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mylist' is not defined. Did you mean: 'myList'?
>>> myList
[123, 'chai', 3.14]
>>> len(myList)
3
>>> myList[0]
123
>>> myList[-1]
3.14
>>> myD = {'one':'lemon',''two':'Ginger','three':'tea'}
  File "<stdin>", line 1
    myD = {'one':'lemon',''two':'Ginger','three':'tea'}   
                          ^
SyntaxError: ':' expected after dictionary key
>>> myD = {'one':'lemon','two':'Ginger','three':'tea'} 
>>> myD
{'one': 'lemon', 'two': 'Ginger', 'three': 'tea'}
>>> myD['one']
'lemon'
>>> myTup = (1,2,4)
>>> myTup[0]       
1
>>> len(myTup)
3