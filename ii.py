Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> c=30
>>> id(a)
140735829789400
>>> id(b)
140735829789720
>>> id(c)
140735829790040
>>> d=10
>>> id(d)
140735829789400
>>> b=50
>>> id(b)
140735829790680
>>> a,b,c=10,20,30
>>> a,b,c
(10, 20, 30)
>>> 
>>> a=10
>>> k=a
>>> k
10
>>> 
>>> x=70
>>> y=80
>>> x,y=y,x
>>> x,y
(80, 70)
>>> a=10
>>> b=20
>>> temp=a+b
>>> temp
30
>>> a=temp-a
>>> a
20
>>> b=temp-b
>>> b
10

import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
len(keyword.kwlist)
35
