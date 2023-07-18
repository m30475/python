Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('퇴사하고싶다')
퇴사하고싶다
>>> food = "python's favorite food is perl"
>>> food
"python's favorite food is perl"
>>> say="\"python's favorite food is perl.\" he says."
>>> say
'"python\'s favorite food is perl." he says.'
>>> say="\"python\'s favorite food is perl.\" he says."
>>> say
'"python\'s favorite food is perl." he says.'
>>> say = "\"python is very easy.\" he says."
>>> say
'"python is very easy." he says.'
>>> print('왜 위에 있는 favorite 에는 역슬래시 찍히는거임?')
왜 위에 있는 favorite 에는 역슬래시 찍히는거임?
>>> multiline='''
   life is too short
   you need python
   '''
>>> multiline
'\n   life is too short\n   you need python\n   '
>>> print(multiline)

   life is too short
   you need python
   
>>> print('그냥 멀티라인 치면 멀티라인의 구성을 알려주는건가')
그냥 멀티라인 치면 멀티라인의 구성을 알려주는건가
>>> print(say)
"python is very easy." he says.
>>> say
'"python is very easy." he says.'
>>> head="이항 "
>>> tail='400달라 가즈아'
>>> head + tail
'이항 400달라 가즈아'
>>> head='이항 "
SyntaxError: EOL while scanning string literal
>>> head='이항 '
>>> tail='400달라 가즈아아아아아아 '
>>> (head+tail)*5
'이항 400달라 가즈아아아아아아 이항 400달라 가즈아아아아아아 이항 400달라 가즈아아아아아아 이항 400달라 가즈아아아아아아 이항 400달라 가즈아아아아아아 '
>>> a="20210608KIMNAEUN"
>>> YEAR=A[:5]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    YEAR=A[:5]
NameError: name 'A' is not defined
>>> YEAR=A[:5]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    YEAR=A[:5]
NameError: name 'A' is not defined
>>> year=a[:5]
>>> year
'20210'
>>> year=a[:4]
>>> date=a[5:9]
>>> lastname=[9:12]
SyntaxError: invalid syntax
>>> lastname=[9:12]
SyntaxError: invalid syntax
>>> date
'608K'
>>> date=a[4:8]
>>> lastname=a[8:12]
>>> lastname=a[8:11]
>>> lastname
'KIM'
>>> firstname=a[11:]
>>> year
'2021'
>>> date
'0608'
>>> lastname
'KIM'
>>> firstname
'NAEUN'
>>> lastname[:2]+' '+lastname[3:]
'KI '
>>> firstname[:2]+' '+firstname[3:]
'NA UN'
>>> firstname[:2]+' '+firstname[2:]
'NA EUN'
>>> print('바로 위에 띄어쓰기 실습한 내용으로\/n firstname 을 저장하고 싶으면 어떻게 하나요?')
바로 위에 띄어쓰기 실습한 내용으로\/n firstname 을 저장하고 싶으면 어떻게 하나요?
>>> print('바로위에 \n 저장')
바로위에 
 저장
>>> 
>>> print('바로 위에 띄어쓰기 실습한 내용으로\n firstname을 저장하고 싶으면 어떻게 하나요?')
바로 위에 띄어쓰기 실습한 내용으로
 firstname을 저장하고 싶으면 어떻게 하나요?
>>> 이항 %d 달러 가즈아 % 400
SyntaxError: invalid syntax
>>> number=400
>>> "이항 %d달러 가즈아아아!" % number
'이항 400달러 가즈아아아!'
>>> number = 400
>>> wealth = "십억"
>>> "이항
SyntaxError: EOL while scanning string literal
>>> 
>>> "이항 %d달러 가면, %s 번다!" % (number.wealth)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    "이항 %d달러 가면, %s 번다!" % (number.wealth)
AttributeError: 'int' object has no attribute 'wealth'
>>> "dlgkd %d 달러가면, %s 번다!" % (number, wealth)
'dlgkd 400 달러가면, 십억 번다!'
>>> "이항 %d 달러 가면, %s 번다!" % (number, wealth)
'이항 400 달러 가면, 십억 번다!'
>>> "I eat {0} apples".format(3)
'I eat 3 apples'
>>> price=400
>>> wealth= 11억
SyntaxError: invalid syntax
>>> wealth=1B$
SyntaxError: invalid syntax
>>> wealth=1bilion$
SyntaxError: invalid syntax
>>> wealth="11억"
>>> 이항 {0}달러 가면 {0}번다! format(price, wealth)
SyntaxError: invalid syntax
>>> "이항 {0}달러 가면 {0} 번다!". format(price, wealth)
'이항 400달러 가면 400 번다!'
>>> "이항 [0}달러 가면 {1} 번다!". format(price, wealth)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    "이항 [0}달러 가면 {1} 번다!". format(price, wealth)
ValueError: Single '}' encountered in format string
>>> "이항{0}달러 가면 {1}번다!".format(price, wealth)
'이항400달러 가면 11억번다!'
>>>  a=20210608kimnaeun
 
SyntaxError: unexpected indent
>>> 
>>> a=20210608kimnaeun
SyntaxError: invalid syntax
>>> a = 20210608kimnaeun
SyntaxError: invalid syntax
>>> print(a)
20210608KIMNAEUN
>>> a.lower()
'20210608kimnaeun'
>>> a.upper()
'20210608KIMNAEUN'
>>> a=a.lower()
>>> a
'20210608kimnaeun'
>>> a=a.upper()
>>> a
'20210608KIMNAEUN'
>>> "이항{price}달러 가면,{wealth} 벌고\n나은이 부자만들어 줘야지
SyntaxError: EOL while scanning string literal
>>> 
>>> "이항 {price}달러 가면, {wealth}벌고\n나은이 부자만들어줘야지!"
'이항 {price}달러 가면, {wealth}벌고\n나은이 부자만들어줘야지!'
>>> 
>>> "이항 {0} 달러 가면, {1}벌고\\n나은이 부자만들어줘야지!".format(price, wealth)
'이항 400 달러 가면, 11억벌고\\n나은이 부자만들어줘야지!'
>>> "이항 {0}달러 가면,{1}벌고 \n나은이 부자만들어줘야지".format(price, wealth)
'이항 400달러 가면,11억벌고 \n나은이 부자만들어줘야지'
>>> print("이항 {0}달러 가면 {1} 벌고 \n나은이 부자만들어줘야지".format(price, wealth))
이항 400달러 가면 11억 벌고 
나은이 부자만들어줘야지
>>> f'이항 {price} 가면 {wealth} 번다!'
'이항 400 가면 11억 번다!'
>>> p=[1, 2, 3]
>>> p
[1, 2, 3]
>>> i=[1, 2, [가, 나, [a, b, c, d,[9, 8]]]]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    i=[1, 2, [가, 나, [a, b, c, d,[9, 8]]]]
NameError: name '가' is not defined
>>> i=[1, 2, [apple, google, nvidia, [ehang, joby]]]
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    i=[1, 2, [apple, google, nvidia, [ehang, joby]]]
NameError: name 'apple' is not defined
>>> i=[1, 2, ['apple', 'google', 'nvidia', ['ehang', 'joby']]]
>>> a[2][3][0]
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a[2][3][0]
IndexError: string index out of range
>>> a[2]
'2'
>>> a[3]
'1'
>>> a[4]
'0'
>>> a[5]
'6'
>>> p[3]
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    p[3]
IndexError: list index out of range
>>> a[2][1]
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a[2][1]
IndexError: string index out of range
>>> i[2][3][0]
'ehang'
>>> i[:2]
[1, 2]
>>> i[:3]
[1, 2, ['apple', 'google', 'nvidia', ['ehang', 'joby']]]
>>> i[:[3]]
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    i[:[3]]
TypeError: slice indices must be integers or None or have an __index__ method
>>> print("nvidia까지만 출력하고 싶으면 어떻게 해야하나요?")
nvidia까지만 출력하고 싶으면 어떻게 해야하나요?
>>> 퇴사='''
이항{0} 달라 가면
{1} 벌고 퇴사다
'''.format(price, wealth)
>>> print(퇴사)

이항400 달라 가면
11억 벌고 퇴사다

>>> 
