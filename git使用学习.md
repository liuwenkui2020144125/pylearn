### Git原理及基本使用学习

#### 诞生：

最初版本的git 诞生于Linus和他的团队在开发Linux内核的过程中。一开始，Linus和他的团队选用的版本控制工具是BitKeeper（一款非开源，但是有条件免费的产品）。但后来由于种种原因BitKeeper宣布终止免费，当时市面上也没有能满足Linux内核开发所需要的分布式版本控制系统，Linus为了解决这一问题，闭关一周，独自设计编写了初版git。

#### 实现原理：

初始化一个git仓库，此时文件夹中只有一个隐藏文件夹 .git , .git 文件夹为git的版本库，存放git实现版本控制所需要的全部信息，git跟传统的代码管理器（如:svn）不同， 主要区别在于git多了个本地仓库以及缓存区，所以即使**无法联网**也一样能提交代码。

#### 工作流程：

> 从远端版本库clone到本地版本库，创建一个分支到工作区，修改代码
>
> > add到暂存区
> >
> > > commit到本地版本库
> > >
> > > > push到远端版本库

工作区，版本库和版本库中的暂存区之间的关系：

![img](https://img2020.cnblogs.com/blog/154172/202111/154172-20211128154955686-1532351478.png)

> --工作区：代码所在的目录，就是自己电脑中能够看到的目录
>
> --暂存区：英文叫stage或者index。一般存放在.git/index文件中，所以我们把暂存区也叫作索引index
>
> --版本库：工作区有一个隐藏的.git，这个不算工作区，而是GIt的版本库。

#### git使用

> `git init` —— 初始化仓库
> `git checkout <branch>` —— 将存储库中的分支检出到工作目录中
> `git add <file>` —— 将文件中的更改添加到更改集中
> `git commit` —— 将工作目录中的更改集提交到仓库中
> `git status` —— 跟踪当前所在的分支上已添加以及未添加的更改。
> `git log` —— 显示工作目录中更改（提交）的历史记录
> `git log <path>` —— 查看特定路径下的更改。
>
> **步骤：**
>
> > 1. 将代码从仓库检出（checkout）到工作目录，
> > 2. 将在此工作目录中所做的更改添加到（add）暂存区域的更改集中，
> > 3. 将更改集提交到（commit）仓库中。

####  删除本地仓库操作：

> 1、#显示所有本地分支
>
> > $ git branch
> > 2、#初始化本地版本库，若出现Reinitialized existing Git repository说明该仓库存在
>
> > $ git init
> > 3、#找到目录.git
>
> > $ ls -a
> > 上面的ls 的’l’是小写的L
>
> 4、删除
>
> > $ rm -rf .git

#### Git结合Github：

> 1. 创建远程仓库
>
>    > 在Github上创建远程仓库
>
> 2. 添加远程仓库
>
>    > `git remote add 别名 远程地址`
>    >
>    > ` # 例子：git remote add origin https://github.com/Du-xx/gitTest.git`
>
> 3. 查看远程地址别名
>
>    > `git remote -v`
>
> 4. 推送push
>
>    > `git push 别名 分支名`
>    >
>    > `git push -u 别名 分支名    # -u指定默认主机`
>    >
>    > `# 例子：git push origin master`
>
> 5. 克隆clone
>
>    > `git clone  远程地址`
>    >
>    > `# 例子：git clone https://github.com/Du-xx/gitTest.git`
>
> 6. 拉取pull
>
>    > `# pull = fetch + merge`
>    >
>    > `git fetch 别名 分支名git merge 别名 分支名`
>    >
>    > `# 等价于git pull 别名 分`支名`
>    >
>    > `# 例子：git pull origin master`
>
> 7. 删除git与github的联系
>
>    > `git remote remove origin # origin是本仓库在github上的别名`

#### 常用指令：

> ` mkdir：         XX (创建一个空目录 XX指目录名)`
>
>    `pwd：          显示当前目录的路径。`
>
>    `git init          把当前的目录变成可以管理的git仓库，生成隐藏.git文件。`
>
>    `git add XX       把xx文件添加到暂存区去。`
>
>    `git commit –m “XX”  提交文件 –m 后面的是注释。`
>
>    `git status        查看仓库状态`
>
>    `git diff  XX      查看XX文件修改了那些内容`
>
>    `git log          查看历史记录`
>
>    `git reset  --hard HEAD^ 或者 git reset  --hard HEAD~ 回退到上一个版本`
>
>    `cat XX         查看XX文件内容`
>
>    `git reflog       查看历史记录的版本号id`
>
>    `git checkout -- XX  把XX文件在工作区的修改全部撤销。`
>
>    `git rm XX          删除XX文件`
>
>    `git remote add origin https://github.com/tugenhua0707/testgit 关联一个远程库`
>
>    `git push –u(第一次要用-u 以后不需要) origin master 把当前master分支推送到远程库`
>
>    `git clone https://github.com/tugenhua0707/testgit  从远程库中克隆`
>
>    `git checkout –b dev  创建dev分支 并切换到dev分支上`
>
>    `git branch  查看当前所有的分支`
>
>    `git checkout master 切换回master分支`
>
>    `git merge dev    在当前的分支上合并dev分支`
>
>    `git branch –d dev 删除dev分支`
>
>    `git branch name  创建分支`
>
>    `git stash 把当前的工作隐藏起来 等以后恢复现场后继续工作`
>
>    `git stash list 查看所有被隐藏的文件列表`
>
>    `git stash apply 恢复被隐藏的文件，但是内容不删除`
>
>    `git stash drop 删除文件`
>
>    `git stash pop 恢复文件的同时 也删除文件`
>
>    `git remote 查看远程库的信息`
>
>    `git remote –v 查看远程库的详细信息`
>
>    `git push origin master  Git会把master分支推送到远程库对应的远程分支上`

   
