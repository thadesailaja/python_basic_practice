Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> id(a)
140735913413336
>>> b=20
>>> id(b)
140735913413656
>>> c=30
>>> id(c)
140735913413976
>>> d=40
>>> id(d)
140735913414296
>>> e=20
>>> id(e)
140735913413656
>>> c=50
>>> id(c)
140735913414616
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
35
>>> <--MVP-->
SyntaxError: invalid syntax
>>> a,b,c=10,20,30
>>> a,b,c
(10, 20, 30)
>>> c,b,a
(30, 20, 10)
>>> k=a
>>> k
10
>>> a,b=b,a
>>> a,b
(20, 10)
>>> A
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
x=nikky
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x=nikky
NameError: name 'nikky' is not defined
x='nikky'
x
'nikky'
x='Nikky'
x
'Nikky'
--DT--
SyntaxError: invalid syntax
a=10
type(a)
<class 'int'>
b=24.3
type(b)
<class 'float'>
c=5+10j
type(c)
<class 'complex'>
d=true
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d=true
NameError: name 'true' is not defined. Did you mean: 'True'?
d=True
type(d)
<class 'bool'>
e=False
type(e)
<class 'bool'>
s='thade sailaja'
s
'thade sailaja'
s="thade sailaja"
s
'thade sailaja'
len(s)
13
s[6]
's'
s[9]
'l'
s[3]
'd'
s[5]
' '
s[11]
'j'
s[7]
'a'
s[-5]
'i'
s[4]
'e'
s[-10]
'd'
s[-4]
'l'
s[-9]
'e'
s[2:4:1]
'ad'
x='hai python'
x[4:6:0]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    x[4:6:0]
ValueError: slice step cannot be zero
x[4:6:]
'py'
x[6:13:]
'thon'
s[6:13:]
'sailaja'
s[0:5:1]
'thade'
s[0:5:2]
'tae'
s[6:13:]
'sailaja'
s[6:13:2]
'siaa'
s[::]
'thade sailaja'
s[-11:-4:2]
'aesi'
s[-9:5:1]
'e'
s[-12:-6:1]
'hade s'
s[-13:-1:]
'thade sailaj'
s[-7:0:1]
''
s[5:5:]
''
s[-4:-9:1]
''
s[-4:-2:1]
'la'
s[-1:-13:1]
''
s[-1:-13:-1]
'ajalias edah'
s[-1:0:-1]
'ajalias edah'
s[-1:-14:-1]
'ajalias edaht'
s[-2:-11:-2]
'jla d'
s[-1:-9:]
''
s[-4:1:-1]
'lias eda'
s[18:0:-1]
'ajalias edah'
s[13:0:-1]
'ajalias edah'
s[-13:0:-1]
s[-3:3:-1]
'alias e'
s[-1:0:-1]
'ajalias edah'
s[-1:5:-1]
'ajalias'
s[-1:1:-1]
'ajalias eda'
s[-1:-14:-1]
'ajalias edaht'
s[4:-5:-1]
''
s[-6:-12:-2]
'a d'
s[-1:-13:-3]
'alsd'
