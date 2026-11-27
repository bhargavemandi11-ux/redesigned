Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=3
type(a)
<class 'int'>
b=7.7
type(b)
<class 'float'>
c='phyton'
type(c)
<class 'str'>
d="code"
type(d)
<class 'str'>
e='''codegan'''
type(e)
<class 'str'>
f=3+9j
type(f)
<class 'complex'>
g=4j+7
type(g)
<class 'complex'>
h=2j
type(h)
<class 'complex'>
g=8+9i
SyntaxError: invalid decimal literal
x=j
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x=j
NameError: name 'j' is not defined
#datatype conversions

int(8)
8
int(6.7)
6
int("hi")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(5+8j)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(5+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(Flase)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
int(False)
0
#float
float(7)
7.0
float(6.7)
6.7
float("hi")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(5+9j)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(5+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(Flase)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
float(False)
0.0
#str
str(8)
'8'
str(3.99)
'3.99'
str(2+7j)
'(2+7j)'
str("hi")
'hi'
str(True)
'True'
str(False)
'False'
#complex
complex(70)
(70+0j)
complex("hi")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    complex("hi")
ValueError: complex() arg is a malformed string
complex(8+15j)
(8+15j)
complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(True)
True
>>> bool(False)
False
>>> bool(900)
True
>>> bool(56.780)
True
>>> bool("bhargav")
True
>>> bool(7+88j)
True
