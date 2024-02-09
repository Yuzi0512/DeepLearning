#### \# 口令管理箱 PasswordLocker

\# 你可能在许多不同网站上拥有账号，每个账号使用相同的口令是个坏习惯。如

\# 果这些网站中任何一个有安全漏洞，黑客就会知道你所有的其他账号的口令。最好

\# 是在你的计算机上，使用口令管理器软件，利用一个主控口令，解锁口令管理器。



\# 用一个命令行参数来运行这个程序，该参数是账号的名称，例如，账号的口令将拷贝到剪贴板，这样用户就能将它粘贴到口令输入框。



##### 运行程序

执行python脚本不只可以在IDLE的文件编辑器中按F5或选择Run菜单项。

还有更方便的方法要善于使用--从命令行运行。

**第一行** 

在windows上，第一行一定要是`#! python3`

在OS X上，第一行一定要是`#! /usr/bin/env python3`

在windows上，第一行一定要是`#! /usr/bin/python3`

**在windows系统上运行python程序**

为了方便运行python程序，可以创建一个.BAT批处理文件，用py.exe来运行python程序。

要创建一个批处理文件，就创建一个新的文本文件，包含一行内
容，类似下面这样：(**需要改成自己的路径**)

```
@py.exe E:\PythonData\PasswordLocker\pw.py %*
@pause
```

然后将其重命名为和.py文件一样的名字，用.bat作为后缀： `pw.bat`



在Windows 上，`pw.bat`所在的文件夹应该添加到PATH中，这样就可以从Run 对话框中运行其中的批处理文件。

开始-》环境变量-》高级设置-》系统变量/用户变量-》PATH-》添加`E:\PythonData\PasswordLocker`(**需要改成自己的路径**)，这里注意不能有中文路径！



Windows系统中运行：

按下**Win-R**
并输入脚本的名称，就能运行C:\MyPythonScripts 文件夹中的Python 脚本。例如，
运行pw，将运行pw.bat. 例如我想复制email的密码

```
Win-R
pw email
#然后去别的地方 CTRL V粘贴就可以了
```



在cmd中运行python程序：

首先cd到.py文件所在的文件夹路径，然后运行：

```
python pw.py
#如果要查看email的密码
python pw.py email
```

