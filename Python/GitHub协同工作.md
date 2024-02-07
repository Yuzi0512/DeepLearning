Github 可以满足多人协作开发项目的需求。在这里我简单记录一下如何两人合作完成代码。

 

方法一：邀请协同开发

这种方法邀请者和被邀请者有几乎相同的权限，被邀请者的push 操作无法被拒绝。邀请者和被邀请者使用同一个repository。

 

首先两个人（userA 和 userB）都需要有各自的github 账号，其中userA 邀请userB 来共同开发， 具体操作步骤如下：

第一步：邀请

userA 登入GitHub以后可以选择新建一个repository，将想要共同完成的工程上传，然后在当前repository的setting中，选择Collaborators，search user B， 向他发送合作邀请，当userB同意后，他就会出现在Collaborators栏目下（如下图所示）。

ps： userB的邀请信息以邮件方式发送给userB的注册邮箱，userB可以在那封邮件中点同意邀请

![img](https://img-blog.csdnimg.cn/20200207134034784.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0plbm55X1dKTg==,size_16,color_FFFFFF,t_70)



第二步： userB 修改代码

这里userB 首先需要下载一个git bash，下载地址：windows 版本。

下载完成后在电脑里会显示如下图，

![img](https://img-blog.csdnimg.cn/20200207135134575.png)



点击Git Bash，

![img](https://img-blog.csdnimg.cn/20200207135708229.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0plbm55X1dKTg==,size_16,color_FFFFFF,t_70)

第一件事是登录自己的GitHub账号，输入

git config --global user.name "Your Name"（注意前边是“- -global”，有两个横线）
git config --global user.email "email@example.com"

登入以后，userB 可以将需要共同完成的工程clone 到本地，在git Bash 中输入

git clone https://github.com/userAname/repository_name

这样子会把工程下载到命令行对应的目录下，win+R >cmd 查看命令行地址，如果想改变clone的工程的存放地址，可以输入

git clone https://github.com/userAname/repository_name  D:/clone_file

其中“D:/clone_file”就是你想存放clone 工程的地址（请确保这个文件夹是空的，不然会出现fatal: destination path 'D:/clone_file' already exists and is not an empty directory.）

clone完成后，userB 就可以在本地修改工程内容了。

 

第三步，userB上传修改内容

当userB 完成修改后就可以提交了，首先到 D:/clone_file，右击这个文件夹，选择 Git Bash here，



然后在git Bash 中按第三步的方式登入GitHub，如果想看看自己修改了哪些部分，可以输入

git commit

上传修改，输入

git commit -a -m “change2”   或者

git add .

git commit -m "change2"

之后再输入 git push，就可以把修改上传到服务器，这时候userA 就可以看到自己GitHub 上面的项目更新了，如图：



如果userA 想把userB的修改更新到本地的话， 同样打开git Bash，登入GitHub账户，输入git pull，修改到本地。

同样，如果userA 修改了内容，userB 也可以使用git pull，把修改更新到本地。

 

 

方法二：fork仓库同步/pull

![img](https://img-blog.csdnimg.cn/20200207163242363.png)

这个方法userA 和userB 使用不同的repository， 代码安全性高，但是管理好复杂。

第一步：fork 代码 clone 到本地

userA 新建了repository，上传了工程，邀请了userB以后，userB接受邀请以后，可以在GitHub上点击fork 



把工程复刻到自己的repository中。然后再和上面一样，在git Bash 中把工程clone 到本地。但要注意的是，假设 repository name 为 test， 这里如果clone到本地  D:/clone_file 中，实际存放在 D:/clone_file/test 下，在git Bash 中要进入 test 文件夹下才能进行push 操作，进入该文件夹 输入 cd D:/clone_file/test。

 

第二步： 修改并上传

这里userB修改和上传的操作和前面的一样，但是这里要注意的一个问题是，当userB 做完修改，想要git push 的时候，可能会出现这样的错误

![img](https://img-blog.csdnimg.cn/20200207164805649.png)

解决办法是：

在git push 之前，先输入

git config --global --edit
然后在显示出的内容的最后输入（按 i 开始输入）

[credential]
  helper = username
  useHttpPath = true
然后按 alt + c 推出输入，英文模式下 按 ":wq" 退出。

然后再输入git push 将修改上传到服务器。不过这些改动只会上传到userB 的repository中，不会更改user A的repository。

 

第三步: 发起pull request

如果userB 希望自己的改动能同步到userA的工程中，就需要在Github 的repository 中发起pull request。

![img](https://img-blog.csdnimg.cn/20200207170603568.png)

userA 就会在自己的Github上接收到pull request，（request 为0 是因为我把它处理了）

![img](https://img-blog.csdnimg.cn/20200207171405279.png)

点进去就可以选择把userB 的修改merge 到自己的repository中。

 

参考：

1. GitHub 协同工作

2. git修改文件后，怎么提交到远程仓库

3. 如何将修改过后的文件通过git上传文件到GitHub

4. ! [remote rejected] master -> master (permission denied)

