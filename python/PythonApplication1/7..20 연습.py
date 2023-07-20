Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  a=[1, 2, [tesla, nvidia, ehang]]
 
SyntaxError: unexpected indent
>>> a= [1, 2, [tesla, nvidia, ehang]]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a= [1, 2, [tesla, nvidia, ehang]]
NameError: name 'tesla' is not defined
>>> a=[1, 2, ["tesla", "nvidia", "ehang"]]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a.sort(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.sort(a)
TypeError: must use keyword argument for key function
>>> a
[1, 2, ['tesla', 'nvidia', 'ehang']]
>>> b=[tesla, ehang. nvidia, joby]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b=[tesla, ehang. nvidia, joby]
NameError: name 'tesla' is not defined
>>> a=[1, 2, 3, 4]
>>> a
[1, 2, 3, 4]
>>> a= [123213, 5354534, 8342, 95390]
>>> 
a
>>> a
[123213, 5354534, 8342, 95390]
>>> a.sort
<built-in method sort of list object at 0x037C3C10>
>>> a.sort()
>>> a
[8342, 95390, 123213, 5354534]
>>> a=['tesla', 'ehang', 'joby', 'nvidia', 'ionq']
>>> a
['tesla', 'ehang', 'joby', 'nvidia', 'ionq']
>>> a.sort()
>>> a
['ehang', 'ionq', 'joby', 'nvidia', 'tesla']
>>> a.pop(joby)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.pop(joby)
NameError: name 'joby' is not defined
>>> a.pop('joby')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.pop('joby')
TypeError: 'str' object cannot be interpreted as an integer
>>> a
['ehang', 'ionq', 'joby', 'nvidia', 'tesla']
>>> a
['ehang', 'ionq', 'joby', 'nvidia', 'tesla']
>>> a.pop('joby')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.pop('joby')
TypeError: 'str' object cannot be interpreted as an integer
>>> a.remove(2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.remove(2)
ValueError: list.remove(x): x not in list
>>> a.remove('joby')
>>> a
['ehang', 'ionq', 'nvidia', 'tesla']
>>> a.extend['tqqq', 'soxl']
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.extend['tqqq', 'soxl']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.extend(['tqqq', 'soxl'])
>>> a
['ehang', 'ionq', 'nvidia', 'tesla', 'tqqq', 'soxl']
>>> a.sort()
>>> a
['ehang', 'ionq', 'nvidia', 'soxl', 'tesla', 'tqqq']
>>> a.reverse()
>>> a
['tqqq', 'tesla', 'soxl', 'nvidia', 'ionq', 'ehang']
>>> l={'stocklist': a]
SyntaxError: invalid syntax
>>> l={'stocklist': a}
>>> i
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    i
NameError: name 'i' is not defined
>>> ;
SyntaxError: invalid syntax
>>> l
{'stocklist': ['tqqq', 'tesla', 'soxl', 'nvidia', 'ionq', 'ehang']}
>>> l={stocklist: a}
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l={stocklist: a}
NameError: name 'stocklist' is not defined
>>> l
{'stocklist': ['tqqq', 'tesla', 'soxl', 'nvidia', 'ionq', 'ehang']}
>>> l[2]='price'.format(price)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l[2]='price'.format(price)
NameError: name 'price' is not defined
>>> price = "11억"
>>> l[2]='price'.format(price)
>>> l
{'stocklist': ['tqqq', 'tesla', 'soxl', 'nvidia', 'ionq', 'ehang'], 2: 'price'}
>>> l[3]='price'{0}.format(price)
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> grade={'ehang'= 50%%, 'tesla'=20%%, 'tqqq'=15%%}
SyntaxError: invalid syntax
>>> grade={'ehang':50%%, 'tesla':20%%, 'tqqq':15%%}
SyntaxError: invalid syntax
>>> grade=
SyntaxError: invalid syntax
>>> grade={'ehang':50%, 'tesla':20%, 'tqqq':15%}
SyntaxError: invalid syntax
>>> grade={'ehang':50, 'tesla':20, 'tqqq': 15}
>>> grade['ehang']
50
>>> grade=['tqqq']
>>> grade
['tqqq']
>>> grade={'ehang':50, 'tesla':20, 'tqqq': 15}
>>> grade['tqqq']
15
>>> grade['tesla']
20
>>> l[1]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    l[1]
KeyError: 1
>>> l[stocklist]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    l[stocklist]
NameError: name 'stocklist' is not defined
>>> l['stocklist']
['tqqq', 'tesla', 'soxl', 'nvidia', 'ionq', 'ehang']
>>> info={'name':'김나은', 'birthday':20210608, 'age': 2}
>>> info[name]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    info[name]
NameError: name 'name' is not defined
>>> info['name']
'김나은'
>>> info['age']
2
>>> info['birthday']
20210608
>>> info.keys()
dict_keys(['name', 'birthday', 'age'])
>>> list(infor.keys())
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list(infor.keys())
NameError: name 'infor' is not defined
>>> list(info.keys())
['name', 'birthday', 'age']
>>> list(info.values())
['김나은', 20210608, 2]
>>> print(list(info.values()))
['김나은', 20210608, 2]
>>> list.get('name')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    list.get('name')
AttributeError: type object 'list' has no attribute 'get'
>>> info.get('name')
'김나은'
>>> id(info)
58381344
>>> 정보=info
>>> id(info)
58381344
>>> id(정보)
58381344
>>> 정보 is info
True
>>> 
