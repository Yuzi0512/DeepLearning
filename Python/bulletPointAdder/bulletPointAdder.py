#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# or each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Seperate lines and add stars
lines = text.split('\n')    # str to list
for i in range(len(lines)): # 注意这里是列表操作，不能用字符串相加
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)     # list to str with \n
pyperclip.copy(text)
