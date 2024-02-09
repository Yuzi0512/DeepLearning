#! python3
# pw.py - An insecure password locker program
import sys
import pyperclip

PASSWORDS = {'email': 'HHDHGJDJunu789?!@',
             'blog': '$atSdfGH980',
             'luggage': '501501',
             'door': '45456654'}
if len(sys.argv) < 2:
    # sys.argv 用来保存命令行参数
    # sys.argv 列表中的第一项总是一个字符串，它包含程序的文件名 pw.py， 第二项是第一个命令行参数
    # 这个参数就是账户名称，如果用户忘记添加参数，即列表中少于两个值，需要显示用法信息
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    