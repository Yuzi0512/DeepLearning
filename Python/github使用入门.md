### GitHub使用入门

---

鉴于每次使用github后停一段时间再用，都会不知道怎么下手，最近换了新笔记本电脑，在使用github时又犯了很多刚用时候的困惑，所以这次把这个流程给记录清楚，以便自己以后查阅。

---

1. **注册github账号**

   登录网址 https://github.com/， 注册，按照提示创建个人账户。

2. **创建一个仓库**

   进入github主页 -> 右上角加号  -> New repository -> Repository name ->public -> Add a READEME file (最好不要选)

   -> choose a license (MIT License) -> Create repositoy

   <img src="C:\Users\lzzha\AppData\Roaming\Typora\typora-user-images\image-20240105143539035.png" alt="image-20240105143539035" style="zoom: 50%;" />

   <img src="C:\Users\lzzha\AppData\Roaming\Typora\typora-user-images\image-20240105143626953.png" alt="image-20240105143626953" style="zoom:50%;" />

   <img src="C:\Users\lzzha\AppData\Roaming\Typora\typora-user-images\image-20240105143858966.png" alt="image-20240105143858966" style="zoom:50%;" />

   这样就创建好了，点绿色的`Code` 可以看到有HTTPS， SSH，记住这里，之后我们要用它连接远程仓库。

3. **删除一个仓库**

   进入这个仓库 -> Settings -> role down to the end ->Danger Zone -> Delete this repository。 

4. **安装git客户端**

   官方下载地址：[http://git-scm.com/download/](https://link.zhihu.com/?target=http%3A//git-scm.com/download/)

   安装过程无脑 next，直到安装成功。

   *  打开git-bash.exe, 它能够在开始菜单中找到。
   * 配置姓名和邮箱

   ```
   git config --global user.name "yao.zhang"
   git config --global user.email "essenzhangyao@gmail.com"
   
   git config --list //查看所有设置
   git config user.name  //查看用户名
   git config user.email //查看邮箱
   git config --global core.editor emacs //设置默认文本编辑器为emacs
   git config --global core.editor vim
   //windows系统中，如果想要使用别的文本编辑器，必须指定可执行文件的完整路径，比如：
   git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
   ```

5. **配置ssh**

   ssh key是加密传输，加密传入的算法有很多，git使用rsa算法。现在github需要使用ed25519算法，具体链接如下：

   https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

   操作如下：

   * 打开 git bash 或者 cmd

   * ```
     ssh-keygen -t ed25519 -C "essenzhangyao@gmail.com" //支持 ed25519算法的系统
     ```

   * ```shell
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com" //不支持ed25519算法的旧系统
     ```

   之后会让你

   ```
   Enter a file in which to save the key(c/users/YOU/.ssh/id_ed25519):
   ```

   ```shell
   > Enter passphrase (empty for no passphrase): [Type a passphrase]
   > Enter same passphrase again: [Type passphrase again]
   ```

   这几个步骤直接按回车，选择默认文件位置，和没有密码。

   这样，我们的ssh就生成好了，存放在了这个路径下：**C:\Users\你的用户名\ .ssh**

   其中一个是私钥，另一个pub是公钥。

   用记事本打开公钥，copy里面的内容，这就是你的ssh key 公钥。然后为GitHub账号配置ssh key。

   ![image-20240105151132913](C:\Users\lzzha\AppData\Roaming\Typora\typora-user-images\image-20240105151132913.png)

   

   Settings->SSH and GPG keys -> New SSH key ->将刚刚复制的内容粘贴到Key 里面 -> Title 那里写上 “Yale'sLaptop" 或”我的台式机“

   -> Add SSH key  -> Complete!

   <img src="C:\Users\lzzha\AppData\Roaming\Typora\typora-user-images\image-20240105151415955.png" alt="image-20240105151415955" style="zoom:50%;" />

   **解释一下为什么用ssh**：

   往GitHub上push项目的时候，有两种方式，ttps或者ssh，如果走https的方式，每次都需要输入账号密码，非常麻烦。而采用ssh的方式，就不再需要输入，只需要在github账号下配置一个ssh key即可。

   **验证是否设置成功**：

   打开git bash 或者 cmd，输入：

   ```
   ssh -T git@github.com
   ```

   如果出现：

   ```
   D:\Users\lzzha\source\repos\机房预约系统>ssh -T git@github.com
   Hi yalezhang2021! You've successfully authenticated, but GitHub does not provide shell access.
   ```

   就说明成功了。

   注意，设置成功后，即可不需要账号密码clone和push代码，**但是要注意自己在clone仓库的时候要使用ssh的url，而不是https！**



6. **ssh的验证原理**

   验证原理
   SSH登录安全性由非对称加密保证，产生密钥时，一次产生两个密钥，一个公钥，一个私钥，在git中一般命名为id_rsa.pub, id_rsa。

   那么如何使用生成的一个私钥一个公钥进行验证呢？

   本地生成一个密钥对，其中公钥放到远程主机，私钥保存在本地
   当本地主机需要登录远程主机时，本地主机向远程主机发送一个登录请求，远程收到消息后，随机生成一个字符串并用公钥加密，发回给本地。本地拿到该字符串，用存放在本地的私钥进行解密，再次发送到远程，远程比对该解密后的字符串与源字符串是否等同，如果等同则认证成功。

7. **ssh key是针对每台主机的**

   比如我在某台主机上操作git和我的远程仓库，想要push时不输入账号密码，走ssh协议，就需要配置ssh key，放上去的key是**当前主机的ssh公钥**。那么如果我换了一台其他主机，想要实现无密登录，也就需要重新配置。

8. **为什么配置了ssh key就不再需要密码了**

   因为配置的时候是把当前主机的公钥放到了你的GitHub账号下，相当于当前主机和你的账号做了一个关联，你在这台主机上已经登录了你的账号，此时此刻GitHub认为是该账号主人在操作这台主机，在配置ssh后就信任该主机了。所以下次在使用git的时候即使没有登录GitHub，也能直接从本地push代码到远程了。当然这里不要混淆了，你不能随意push你的代码到任何仓库，你只能push到你自己的仓库或者其他你有权限的仓库！
   
9. 上传本地项目到GitHub

   现在我想要将一个本地的项目上传到GitHub上，这个文件夹的位置为：**D:\Users\lzzha\source\repos\机房预约系统**

   在这个文件夹里打开cmd：

   ```
   git init //把这个目录变成Git可以管理的仓库
   git add README.md //文件添加到仓库
   git add . //不但可以跟单一文件，还可以跟通配符，更可以跟目录。一个点就把当前目录下所有未追踪的文件全部add了 
   git commit -m "first commit" //把文件提交到仓库
   git remote add origin git@github.com:wangjiax9/practice.git //关联远程仓库，这里要用仓库的ssh地址
   git push -u origin master //把本地库的所有内容推送到远程库上
   
   ```

   这里关联远程仓库 记得要用的是ssh的url。

   执行的步骤就是：

   ```
   git init
   git add .
   git commit -m "first commit"
   git remote add origin git@github.com:yalezhang2021/Computer-Room-Reservation-Management-System.git
   git push -u origin master //第一次因为新建的远程仓库是空的，要加上 -u 这个参数，等仓库里有了内容之后就可以用下面的
   git push origin master
   ```

   

10. 注意避坑

    在第2步，创建远程仓库的时候，如果勾选了 add a readme file,  那么到第9步我们push的时候会报错： `failed to push some refs to ......`，。这是由于你新建的那个仓库里面的READEME文件不在本地仓库目录中，这时候可以通过下面的命令先将内容合并一下：

    ```
    git pull --rebase origin master
    ```

    这时再push就能成功了。

11. GitHub在2020年之后就将默认分支改为了main而不是master，所以会导致我们push了之后出现了两个分支，一个main一个master。解决方法如下

    1. 将这个仓库的默认分支改为master。在该仓库的setings下-> Default branch

       <img src="C:\Users\lzzha\AppData\Roaming\Typora\typora-user-images\image-20240105155500374.png" alt="image-20240105155500374" style="zoom:50%;" />

    2. 方法二是可以在本地改名

       ```
       git pull --rebase origin main
       git switch -c main //创建并切换到新分支 main
       git branch -v //查看分支
       git checkout 分支名 //切换分支
       git push -u origin main //第一次push还是要用 -u
       git push origin main //之后可以用这个
       ```

       在GitHub上设置main为default branch.

       然后删除掉master分支

       ```
       git branch -d master //删除本地master 
       //会提示还没有merge，不能删除，如果强行删除需要用 git branch -D master
       git branch-D master
       ```

       ```
       git push origin :master //删除远程master
       ```

       ok, 至此，删除完毕。