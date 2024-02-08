### 复习： python基础

数学操作符：

```
** 	指数 	2 ** 3 8
% 	取模/取余数 	22 % 8 6
// 	整除/商数取整 	22 // 8 2
/ 	除法 	22 / 8 2.75
* 	乘法 	3 * 5 15
- 	减法 	5 - 2 3
+ 	加法 	2 + 2 4	
```

数据类型：
int, float, double, char...

基本函数：

**print()**

```
print('hello', end='')	#末尾不分行，而是以''当作结尾
print('cat', 'dog', 'mice')
print('cat', 'dog', 'mice', sep=',') #以，隔开
```



**input()**

```
myName = input();
```

**len()**

```
len('hello')	#5
```



**str(), int(), float()	转换类型**



**布尔值 bool value**

`True False`



布尔操作符

`and  or  not`

```python
True and False	#False
True or False	#True
not True		#False
```



**if else**

```python
if name == 'Mary':
    print('hello mary')
elif name == 'Alice':
    print('hello alice')
else:
	print('wrong name') 
```



**while**

```python
spam = 0
while spam < 5:
    print('hello world')
    spam += 1;
```



**break**

提前跳出循环



**continue**

用于循环内部，结束当前循环，执行下次循环



**for loop** and **range()**

```python
for i in range(5):
    print(i)
```

```python
for i in range(0, 10, 2):	#从0到10， 间隔为2， 区间为[0,10)
    print(i)
```



**sys.exit()** 提前结束程序

```python
import sys

while True:
    print('Type exit to exit.')
    response = input();
    if response == 'exit';
    	sys.exit()
    print('You typed ' + response + '.')
```



**函数**

```python
def hello():
    print('howdy')
    
hello()
hello()
```



```python
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'Yes'
    else:
        return 'Very doubtful'
    
r = random.randint(1, 9)
ans = getAnswer(r)
print(ans)
```



**None**

```
在幕后，对于所有没有return语句的函数定义，都会自动返回None。
```



**要分情局部和全局变量**

在python中，允许局部变量和全局变量同名，所以尽量避免出现这种情况，局部变量在执行完局部后就销毁了。



**global语句**，告诉编译器，后面的指定的变量是global变量

```python
def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)
--------------
spam
```



**try except 抛出异常代替报错**

```python
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(0))
-------------------------
21.0
Error: Invalid argument.
```



**数据类型：列表**list

```
[1, 2, 3]
['cat', 'dog', 'mice']
#列表是一个值，包含多个字构成的序列

spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]		#cat
spam[-1]	#elephant
spam[1:3]	#['bat','rat'] 相当于左闭右开
spam[:2]	#['cat', 'bat'] 左闭右开
spam[:]		#['cat', 'bat', 'rat', 'elephant'] 直到末尾

spam = [['cat', 'bat'], ['rat', 'elephant']]
spam[0]	#['cat', 'bat']

tmp = []

[1,2,3]+['a','b','c']
[1,2,3,'a','b','c']	#列表连接

del spam[2]	#删除下标为2处的值
```

```python
#example 输入姓名
catNmaes = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
         ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames += [name]	#连接列表
    print('The cat names are: ')
    for name in catNames:
        print(' ' + name)
```

```python
for i in range(len(catNames)):
    print(catNames[i] + ' ')
```



**操作符 in  和 not in**

```python
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I don\'t have a pet named ' + name)
else:
    print(name + ' is my pet.')
```

小技巧，多重赋值：

```
cat = ['fat', 'black', 'loud']
size, color, desposition = cat

# size = cat[0]
# color = cat[1]
# desposition = cat[2]
```



**方法index()**: 在列表中查找值的下标

```python
spam = ['hello', 'hi', 'howdy']
spam.index('hello')	#0

# 如果列表中有重复的值，返回的是它的第一次出现的下标
```

**append()    insert()  remove()  sort()**

```python
spam = ['hello', 'hi', 'howdy']
spam.append('moin')	#在列表最后面添加
spam.insert(1, 'Pooka')	#在位置1处添加，其他的往后移动
spam.remove('hello')	#如果有重复，只移除第一个
del spam[0]	#0位置会变成空，但这个位置还在！

spam = [2,5,3,14]
spam.sort()	#默认从小到大排序
spam.sort(reverse=True)	#从大到小排序

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)	#全部当成小写字母排序

```



python 中一行打不下的话分行，用 \ 

```python
print("asldjfsadhfjaskhdhkasdjfhkasjdhffasdfasdfsghkjasf\
fdkahfakdjhfkadjshfkdahfjdshfkjashfjkdshdfkjhaj")
```





**数据类型：字符串sstr和元组tuple**

和列表类似，都可以用取值，切片，len， in,  not in, 等操作

```python
name = 'Zophie'
name[0]		#Z
name[-2]	#i
name[0:4]	#Zoph
'Zo' in name	#True
'll' not in name	#True
```



**可变和不可变数据类型**

列表是可变的，可以根据下标对它重新赋值；(其实这里的改变是覆盖)

字符串是不可变的，不可以被更改。

```python
name = 'Zophie a cat'
name[7] = 'the'	# Wrong!
newName = name[0:7] + 'the' + name[8:12]	# right!

# str 不可变
text = 'hello, hi, nihao'
words = text.split(',')
for word in words:
	word = 'ss' + word
text = ','.join(words)
print(text)
# 'hello, hi, nihao'

# list 可变
text = 'hello, hi, nihao'
words = text.split(', ')
for i in range(len(words)):
	words[i] = 'ss' + words[i]
text = ','.join(words)
print(text)
# sshello,sshi,ssnihao'
```



**元组**tuple

元组几乎与列表一样，**不同的是：1. 用（）， 2.是不可变类型**

如果需要一个永远不会改变的值的序列，就用元组。

```python
eggs = ('hello', 42, 0.5)
eggs[0]	#'hello'
eggs[1:3]	#(42, 0.5)
eggs[1] = 99	#wrong!
```

此外，如果元组中只有一个值，需要在值后面跟个 逗号， 表明这种情况。否则，编译器会认为你只是在一个普通括号里输入了一个值。

```python
type(('hello',))	#<class 'tuple'>.
type(('hello'))		#<class 'str'>
```

**list(), tuple()** 转换类型

```python
tuple(['cat', 'dog', 5])
#('cat', 'dog', 5)

list(('cat', 'dog', 5))
#['cat', 'dog', 5]
```



**引用**reference

```python
spam = [0, 1, 2, 3, 4, 5]	#spam不是实际的列表，只是保存了对列表的引用
cheese = spam				#此时spam和cheese指向了同一个列表
cheese[1] = 'hello'
spam
#[0, 'hello', 2, 3, 4, 5]
cheese
#[0, 'hello', 2, 3, 4, 5]
```

**python处理列表和字典都是这样，采取了列表或字典的引用而不是其本身。**



```python
def eggs(someParameter):
    someParameter.append('hello')
    
spam = [1, 2, 3]
eggs(spam)
print(spam)
#[1, 2, 3, 'hello']
```



**copy() 和 deepcopy()**

```python
import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)	#现在，spam和cheese分别指向独立的列表，互不影响
cheese[1] = 42
spam
#['A', 'B', 'C', 'D']
cheese
['A', 42, 'C', 'D']

#如果要赋值的列表里包含了列表，就需要使用 deepcopy(), 可以同时复制他们内部的列表
spam2 = [['A', 'B'], ['C', 'D']]
cheese2 = copy.deepcopy(spam2)
```



**字典和结构化数据**

主要就是 key value 键值对，和cpp里的unordered_map一样，格式如下：

```python
myCat = {
    'size': 'fat', 
    'color': 'gray',
    'desposition': 'loud'
        }
print(myCat['size'])
#'fat'

spam = {
    12345: 'Luggage Combination',
    42: 'The Answer'
	}
print(spam[42])

```

字典和list的区别， 字典里面不排序，list里面是排序的

```python
>>> spam = ['cats', 'dogs', 'moose']
>>> bacon = ['dogs', 'moose', 'cats']
>>> spam == bacon
False
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
>>> eggs == ham
True
```

```python
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
	print('Enter a name: (blank to quit)')
	name = input()
	if name == '':
		break
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I do not have birthday information for ' + name)
		print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
```

**字典中的方法keys(), values(), items()**

```python
spam = {'color': 'red', 'age': 42}
for v in spam.values():
	print(v)	#red
for k in spam.keys():
	print(k)	#color #age
for i in spam.items():
	print(i)	#('color', 'red') #('age', 42) 这里包含的键和值是元组

#如果希望通过这些方法得到一个列表
print(spam.keys())			#(['color', 'age'])
print(list(spam.keys()))	#['color', 'age']

#利用多重赋值, 将键和值赋给不同的变量
for k, v in spam.items():
	print('key: ' + k + ' Value: ' + str(v))
#Key: age Value: 42
#Key: color Value: red
```

**字典中的方法get()**

```python
spam = {'color': 'red', 'age': 42}
print(spam.get('color', 0))
#red, 有color键， 就输出对应的value
print(spam.get('cups', 0))
#0， 没有cups键， 就输出默认值0
```

**字典中的方法setdefault()**

为字典中的某一个键设置一个默认值，当该键没有任何值时使用它。

```python
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
#等价于下面
spam.setdefault('color', 'black')	#相当于给当前字典添加了一个键值对
print(spam)
#{'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white')	#上面添加过后， 我们的字典里已经有color键了，所以这个新的默认值添加不了
print(spam)
#{'color': 'black', 'age': 5, 'name': 'Pooka'}
```

应用，用字典保存一条信息里每个字符出现的次数

```python
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(charactor, 0)
    count[character] = count[character] + 1
print(count)

{' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i':
6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}
```

**漂亮打印字典 pprint模块 和 pprint(), pformat()**

```python
import pprint
message = 'It was a bright cold day in April, and the clocks were striking
thirteen.'
count = {}
for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1
pprint.pprint(count)

{' ': 13,
',': 1,
'.': 1,
'A': 1,
'I': 1,
'a': 4,
'b': 1,
'c': 3,
'd': 3,
'e': 5,
'g': 2,
'h': 3,
'i': 6,
'k': 2,
'l': 3,
'n': 4,
'o': 2,
'p': 1,
 ....
```

pprint(): 如果字典本身包含嵌套的列表或字典，pprint.pprint() 特别有用，打印到屏幕上

pprint.pformat(): 打印的文本作为字符串，而不是打印到屏幕上



**str字符串操作**

```python
spam = "That is Alice's cat." #单引号也可以

#在字符串开始的引号前加r，使他成为原始字符串
#原始字符串忽略转义字符
print(r"That is carros\'s cat.")
#That is carros\'s cat.

#''' 用于多行字符串，忽略所有转义字符'''
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Yao
''')
```

字符串可以切片操作， in， not in 方法

还有字符串方法 upper(), lower(), isupper(), islower()

判断大小写

```python
spam = 'Hello world'
spam = spam.upper()
#HELLO WORLD

spam = spam.lower()
#hello world

#这些方法没有改变字符串本身，而是返回了一个新字符串， 重新赋值给原来的spam才能改变原来的字符串
print(spam.islower())
#True

print(spam.isupper())
#False

#此外的字符串 isX方法
isalpha()	#字符串只包含字母，且非空
isalnum()	#字符串只包含字母和数字，且非空
isdecimal()	#字符串只包含数字字符，且非空
isspace()	#字符串只包含空格，制表符和换行，并且非空
istitle()	#字符串只包含以大写字母开头，后面都是小写字母的单词

#字符串方法 join() 和 split()
#join()	#连接字符串列表，成为一个单独的字符串,由前面的给定字符串把列表中的单个字符串连接起来
' '.join(['cats', 'dogs', 'rats'])
#'cats dogs rats'
','.join(['cats', 'dogs', 'rats'])
#'cats, dogs, rats'

#split() 针对一个字符串调用，返回一个字符串列表, 默认按空格区分
spam = 'my name is Simon'
spam.split()
#['my', 'name', 'is', 'Simon']

spam = 'my name is， Simon'
spam.split(',')	#按逗号区分
#['my name is', 'Simon']

spam = '''my name is
Simon'''
spam.split('\n')	#按换行区分
#['my name is', 'Simon']

#字符串方法 rjust(), ljust(), center()
'Hello'.rjust(10) #右对齐，放在一个长度为10的字符串中
'     Hello'
'Hello'.rjust(20) #右对齐，放在一个长度为20的字符串中
'                Hello'
'Hello World'.rjust(20, '*') #右对齐，放在一个长度为20的字符串中,并以*填充
'**********Hello World'

#center() 和 ljust() 与上面相同，让文本居中或左对齐

#示例打印
def printPicnic(itemDict, leftWidth, rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, '-'))
    for k, v, in itemsDict.items():
        print(k.ljust(leftWidth, ',') + str(v).rjust(rightWIdth))
PicnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(PicnicItems, 12, 5)

---PICNIC ITEMS--
sandwiches.. 4
apples...... 12
cups........ 4
cookies..... 8000


#字符串方法 strip(), rstrip(), lstrip() 默认删除空白字符，也可以指定删除字符串参数
strip(): 返回一个新字符串，删除左右两边的空白
rstrip(): 返回一个新字符串，删除右边的空白
lstrip(): 返回一个新字符串，删除左边的空白

spam = '   Hello World '
spam.strip()
#'Hello World'

>>> spam = 'SpamSpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')	#在字符串两端删除出现的a,m,p,S， 字符串的顺序并不重要
'BaconSpamEggs'
```



**pyperclip 模块**

主要是使用它的 copy() 和paste() 函数， 可以向计算机的剪贴板发送文本，或从它接受文本。

```python
>>> import pyperclip
>>> pyperclip.copy('Hello world!')	
>>> pyperclip.paste()	#即ctrl + v
'Hello world!'
```

相关项目：

https://github.com/Yuzi0512/DeepLearning/tree/master/Python/PasswordLocker

https://github.com/Yuzi0512/DeepLearning/tree/master/Python/bulletPointAdder



至此， python基础部分结束，毕业之后就没写过python了，复习一遍，做个总结。



