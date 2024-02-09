在编辑一篇维基百科的文章时，你可以创建一个无序列表，即让每个列表项占
据一行，并在前面放置一个星号。但是假设你有一个非常大的列表，希望添加前面
的星号。你可以在每一行开始处输入这些星号，一行接一行。或者也可以用一小段
Python 脚本，将这个任务自动化。

bulletPointAdder.py 脚本将从剪贴板中取得文本，在每一行开始处加上星号和空
格，然后将这段新的文本贴回到剪贴板。

example：

```
# copy the following lists
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars

# run bulletPointAdder.py and paste
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars

#这段前面加了星号的文本，就可以粘贴回维基百科的文章中，成为一个无序列表。
```



总结任务：

1. 从剪贴板粘贴文本	pyperclip.copy()
2. 对它做一些处理    用到 split 和 join 方法
3. 将新的文本复制到剪贴板 pyperclip.paste()



第2步要注意，列表是可变的，字符串是不可变的，所以在选择拼接的时候

```
for i in lines:
	i = '* ' + i # 不对

for i in range(len(lines)):
	lines[i] = '* ' + lines[i]	# 正确
```

