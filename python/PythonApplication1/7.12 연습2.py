Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("=" * 50)
==================================================
>>> print("My program")
My program
>>> print("=" * 50)
==================================================
>>> # multistring.py
>>> print("=" * 50)
==================================================
>>> a= "life is too short, you need python"
>>> a[4]
' '
>>> a[5]
'i'
>>> a[0:3]
'lif'
>>> a[0:4]
'life'
>>> a[10:]
'o short, you need python'
>>> a[9:]
'oo short, you need python'
>>> a[8:]
'too short, you need python'
>>> a="202106081828KIMNAEUN"
>>> year = a[:3]
>>> month = a[3:5]
>>> day = a[5:7]
>>> time = a[7:11]
>>> name = a[11:]
>>> name
'8KIMNAEUN'
>>> year
'202'
>>> a="202106081828KIMNAEUN"
>>> year=a[:4]
>>> month=a
>>> month
'202106081828KIMNAEUN'
>>> a="202106081828KIMNAEUN"
>>> year=a[:4]
>>> month=a[4:6]
>>> day=a[6:8]
>>> time=a[8:12]
>>> name=a[12:]
>>> name
'KIMNAEUN'
>>> time
'1828'
>>> year
'2021'
>>> month
'06'
>>> day
'08'
>>> time
'1828'
>>> name
'KIMNAEUN'
>>> a[12:15]+ +a[16:17]+
SyntaxError: invalid syntax
>>> a[12:15]+ +a[16:17]+ +a[17:]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a[12:15]+ +a[16:17]+ +a[17:]
TypeError: bad operand type for unary +: 'str'
>>> a[12:15]+" "+a[15:17]+" "+a[17:}
SyntaxError: invalid syntax
>>> a[12:15+" "+a[15:17]+" "+a[17:]
  a=kimnaeun
  
SyntaxError: invalid syntax
>>> 
