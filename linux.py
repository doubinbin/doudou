Liunx系统总结
ls 命令功能	列出目录下的文件和子目录的信息
     -l  长格式列出，包含文件权限/硬链接数/拥有者/所属组/文件大小/时间/文件名等信息
     -h 以人性化的方式列出
     -a 列出所有文件，包含隐藏文件
     -t 以时间先后顺序列出
     -d 查看目录本身的信息
文件创建及状态查看
     touch filename
        1.文件不存在，创建这个文件，文件名小于255个字符， 可以一次创建多个文件。  
        2.文件存在，修改这个文件的时间戳。
      stat filename 
        命令功能：查看文件的时间戳。
         accesee 文件被访问的时间，
         modify文件内容被修改的时间，
         change文件属性被修改的时间
     du 计算文件的大小。
         -s 目录总的大小 
         -h人性化显示stat filename 
文件的删除、移动、复制     
rm filename 
         命令功能：删除文件。root用户删除文件会提示、普通用户删除文件不会提示
         强制删除-f。
         交互式删除-i。
         删除目录，-r，递归删除。
     cp 源文件 目的地 
        保留源文件权限，-p。
        复制目录，-r
     mv 源文件 目的地 
        1.移动文件 
        2.为文件改名（指定目的名称）
  文件的内容查看
     grep 
功能：按行过滤显示。
^字符串。以..开始。
字符串$，以..结尾。
--color匹配到的字符串高亮显示，
-v反选，过滤出不包含该字符串的行。
cut -d"分割符" -f列数 filename。
功能：按列截取查看文件内容。
file 判断文件内容的类型。
wc 
功能：统计文件的行数/单词数/字节数。
-l 查看行数，
-w查看单词数，
-c查看字节数。
    文件的查找
whereis和which根据PATH变量查找
locate 特征：查找速度快，根据数据库查找，数据库var/lib/mlocate/mlocate.db。配置文件/etc/updatedb.conf。 updatedb可手动更新数据库。 非 实时/根据文件名的模糊查找
find    [查找路径] 查找条件 [查找后执行的动作] 。 实时的/准确的/全面 的查找。 比较慢。 查找路径省略即为当前目录. 
文件的内容查看
diff 比较两个文件内容的不同
date 查看系统时间。
-s设置系统时间
hwclock 查看硬件时间。
-s设置系统时间，以硬件时间为依据。 
-w设置硬件时间，以系统时间为依据。
cal 查看日历
文件的扩展命令
ln 源文件 链接文件： 创建硬链接
ln -s 源文件 链接文件：创建软链接
软链接特征：源文件和链接文件由不同的inode，权限，创建时间等。可以轻易分辨源文件和软链接文件，软链接文件颜色高亮显示，软链接文件权限为777。软链接文件大小为路径的长短，路径指向源文件对应的block。可针对目录做软链接，可跨文件系统。软链接类似windows快捷方式。 删除源文件，软链接文件会随之失效。
硬链接特征：无法区分哪个是源文件，哪个是链接文件。修改一 个文件的权限，另外一个也随之变化。无法针对目录操作。无法跨文件系统。 删除源文件，对于硬链接文件没有影响，只是硬链接计数器减一。
superblock：存放文件系统的整体信息
inode：文件属性存放的位置。ls -i 可以查看inode号  文件节点号
block：文件内容存放的位置
       文件的内容查看
       diff 比较两个文件内容的不同
date 查看系统时间。
-s设置系统时间
hwclock 查看硬件时间。
-s设置系统时间，以硬件时间为依据。 
-w设置硬件时间，以系统时间为依据。
cal 查看日历
目录操作
mkdir 
功能：创建目录        -p创建多级
rmdir 
功能：删除空目录
删除目录及目录内容使用
rm –r
注意rm的-f为危险参数，没有提示确认的情况下若误删关键文件将导致数据无法恢复
         用户相关设置文件
 /etc/passwd	   存放用户基本信息
/etc/shadow 	存放用户的密码信息，包含加密后的密码和密码策略。
/etc/group 	    存放组基本信息。
/etc/gshadow 	 存放组的密码信息
/etc/login.defs 	 存放密码的默认策略和UID/GID范围等信息
/etc/default/useradd 	添加用户的默认设置
/etc/skel/		       用户家目录的模板文件
Linux中用户管理相关命令
useradd 添加用户。
-u指定UID
-d指定家目录
-s指定登录shell等
passwd 设置密码
echo password |  passwd --stdin username 非交互式修改用户密码
userdel username
-r并删除用户的所有目录
usermod 修改用户的属性
-g修改用户的默认组 
-G修改用户 的附加组 
-aG追加用户的附加组 
-u修改用户的UID，
-d修改用户的家目录
-s修改用户的登录shell
Linux中用户管理相关命令
chage -l username 罗列用户的密码策略 
chage username  修改用户的密码策略
su 切换用户
id 查看用户UID/组ID/所属组等信息
finger 查看用户家目录/登录shell等信息
who 查看当前系统中哪些用户在登录
whoami 查看当前你登录的是谁
groupadd 添加组。
groupdel 删除组
              Linux中管理员用户设置
              sodu	普通用户临时获取root权限     用法示例：sodu useradd xxg
visudo	可以通过命令修改/etc/sudoers授予用户的sodu管理员权限
whereis  查找命令的绝对路径
权限查看
ls -l 		查看文件的UGO权限。
U代表文件的拥有者
G代表文 件的所属组内用户
O代表其他人
列出的第一列内容的第一个字符代表文件类型。
-普通文件 ，
d目录文件，
l链接文件，
s套接字文件，
c字符设备文件，
b块设备文件，
p管道文件
对于文件：r代表可使用cat等命令查看文件内容，w代表可增 加/删除/修改文件内容，x代表可执行该文件。
对于目录：r代表可使用ls命令列出目录下的文件名，要想看文件的详细信息，需结合x权限。w代表表可在该目录下创建/删除文件和子目录，或修改 文件名称， 要与x结合使用。x代表可进入该目录。 
ll	等价于ls –l命令
UGO权限修改
chmod 权限 file/dir  修改文件或目录的权限
一种方式【u g o a】+ - = 【r w x】
第二种方式数字的组合
-R   递归修改文件夹权限      数字规则：r=4 w=2 x=1
chown username file/dir             修改文件的拥有者
chown username:groepname file/dir   修改文件的拥有者以及拥有组
chgrp groupname file/dir            修改文件的所属组
chown username：groupname       修改文件的拥有者和所属组
备注：-R   递归修改文件夹权限
默认权限
umask释义：
决定用户创建的文件和目录的默认权限。文件最大权限666，目录最大权限777
文件的默认权限为777按位减去umask值确定
/etc/profile  该文件为用户初始化设置文件，可以决定用户的初始umask值
umask 直接回车，可查看当前用户的umask值
umask 数字 可临时修改当前用户的umask值
~/.bashrc 添加umask 数字 可永久修改用户的umask值
即使生效需执行：source  .bashrc
s\t权限管理
s[suid]权限：
作用在二进制的可执行程序上，让任何人在执行这个二 进制可执行程序时临时拥有文件拥有者的权限。
设置方式：chmod u+s filename
s[sgid]权限：
作用在二进制的可执行程序上，任何人在执行这个二进 制可执行程序时临时拥有文件所属组内用户的权限。作用在目录上，任何人在这个目录下创建的文件所属组都继承目录的所属组
设置方式：chmod g+s filename/dirname
t[sticky]权限：
作用在目录上。任何人都可以在该目录下创建文件， 但是自己只能删除或修改自己的文件，不能删除其他用户创建的文件，只用这个目录的拥有者能够删除该目录下所有文件，达到动态平衡
设置方式：chmod +t filename/dirname
suid=4 sgid=2 sticky=1
数字设置示例：
chmod  4777 filename/dirname
acl权限管理
acl 权限的意义
Acl权限是UGO权限的补充权限，UGO最多可控制三类用户，而acl可针对单个用户和单个组做权限的设置。
getfacl filename 
查看文件的acl权限
setfacl -m u:username:权限 file/dir 
针对某个用户设置acl权限
setfacl -m g:groupname:权限 file/dir 
针对单个组设置acl权限
setfacl -m m:权限 
设置mask值
mask是规定acl的最大权限，用户的acl权限为用户基础权限与mask的权限相与的结果
setfacl -x u:st 文件名
删除ACL用户权限
setfacl -x g:tgroup 文件名
删除ACL组权限
setfacl -b 文件名
删除整个ACL权限
-R	递归设置
文件的压缩
zip 压缩时需指定压缩后名称，默认保留源文件，压缩比不高， 是windows和linux      唯一通用的压缩方式。可压缩目录。unzip解压
gzip和bzip2/xz压缩时不需要指定压缩后的名称，默认不保留源文件，压缩比相对较高。
bzip2压缩比最高。不可压缩目录。
gzip使用gunzip解压。
bzip2使 用bunzip2解压。
xz用unxz解压
压缩率由高到底依次为xz/bzip2/gzip/zip
文件的打包
  tar	打包命令
相关参数及意义
-c  ：建立一个压缩档案的参数指令(create 的意思)；
-x  ：解开一个压缩档案的参数指令！ 
-t  ：查看 tarfile 里面的档案！
特别注意，在参数的下达中， c/x/t 仅能存在一个！不可同时存在！
因为不可能同时压缩与解压缩。
-z  ：是否同时具有 gzip 的属性？亦即是否需要用 gzip 压缩？
-j  ：是否同时具有 bzip2 的属性？亦即是否需要用 bzip2 压缩？
-v  ：压缩的过程中显示档案！这个常用，但不建议用在背景执行过程！
-f  ：使用档名，请留意，在 f 之后要立即接档名喔！不要再加参数！
-p  ：使用原档案的原来属性（属性不会依据使用者而变） 
-P  ：可以使用绝对路径来压缩！
-N  ：比后面接的日期(yyyy/mm/dd)还要新的才会被打包进新建的档案中！ 
--exclude FILE：在压缩的过程中，不要将 FILE 打包！ 
tar 打包 -f  必须写在最后
文件的打包压缩示例
tar -cvf /tmp/etc.tar /etc  
#仅打包，不压缩！
tar -czvf /tmp/etc.tar.gz /etc 
#打包后，以 gzip 压缩
tar -cjvf /tmp/etc.tar.bz2 /etc  
#打包后，以 bzip2 压缩
tar -tzvf /tmp/etc.tar.gz	
#查阅上述 /tmp/etc.tar.gz 档案内有哪些档案
cd /usr/local/src
tar -xzvf /tmp/etc.tar.gz
#将 /tmp/etc.tar.gz 档案解压缩在 /usr/local/src 底下
cd /tmp
tar -xzvf /tmp/etc.tar.gz etc/passwd
#/tmp 底下，我只想要将 /tmp/etc.tar.gz 内的 etc/passwd 解开而已
tar -czvpf /tmp/etc.tar.gz /etc
#将 /etc/ 内的所有档案备份下来，并且保存其权限！
tar -N '2005/06/01' -czvf home.tar.gz /home
#在 /home 当中，比 2005/06/01 新的档案才备份
tar --exclude /home/dmtsai -czvf myfile.tar.gz /home/* /etc
#我要备份 /home, /etc ，但不要 /home/dmtsai 
cd /tmp
tar -cvf - /etc | tar -xvf -
将 /etc/ 打包后直接解开在 /tmp 底下，而不产生档案
文件的attr权限
attr 权限作用：针对特殊用户和特殊操作进行补充的权限
lsattr查看文件的attr权限
chattr 设置文件的attr权限
-R：递归处理，将指定目录下的所有文件及子目录一并处理。
-V：显示详细过程有版本编号。
-v：设定文件或目录版本(version)。
+ ：在原有参数设定基础上，追加参数。
- ：在原有参数设定基础上，移除参数。
= ：更新为指定参数设定。
attr 权限作用：针对特殊用户和特殊操作进行补充的权限
A：文件或目录的 atime (access time)不可被修改(modified), 可以有效预防例如手提电脑磁盘I/O错误的发生
S：硬盘I/O同步选项，功能类似sync
a：即append，设定该参数后，只能向文件中添加数据，而不能删除，多用于服务器日志文    件安全，只有root才能设定这个属性
c：即compresse，设定文件是否经压缩后再存储。读取时需要经过自动解压操作
d：即no dump，设定文件不能成为dump程序的备份目标
i：设定文件不能被删除、改名、设定链接关系，同时不能写入或新增内容。i参数对于文件  系统的安全设置有很大帮助
j：即journal，设定此参数使得当通过mount参数：data=ordered 或者 data=writeback 挂载的文件系统，文件在写入时会先被记录(在journal中)。如果filesystem被设定参数为  data=journal，则该参数自动失效
s：保密性地删除文件或目录，即硬盘空间被全部收回
u：与s相反，当设定为u时，数据内容其实还存在磁盘中，可以用于undeletion.
各参数选项中常用到的是a和i。a选项强制只可添加不可删除，多用于日志系统的安全设定。而i是更为严格的安全设定，只有superuser (root) 或具有CAP_LINUX_IMMUTABLE处理能力（标识）的进程能够施加该选项
Linux进程管理
系统运行的程序放在硬盘上，叫程序文件，那么一旦被cpu读取进入内存就叫进程． 进程是内存运行的最小单元，代表程序正在运行的一种状态，看到进程说明程序正在运行．
人通过名字识别进程，进程名一般是应用程序的名字，操作系统对数字敏感，所以就通过一种叫PID的进程号来识别进程，那么除了进程之外呢，进程还有爸爸，进程的爸爸我们称为父进程，用PPID表示．父进程用来产生进程的．父进程终止了，子进程自然也就终止了．
子进程要先复制父进程，再执行，所以相对有点耗时，所以很多服务不再基于这种方式，而是以线程方式打开客户服务，大并发过来时，进程速度慢，线程速度快。
以树状结构查看进程
Pstree
Pstree|less
进程查看命令ps详解：
ps 一般情况下我们都使用　aux这三个选项结合来查看进程
PS命令参数
a)	a 显示所有用户的所有进程（包括其它用户）；
b)	u 按用户名和启动时间的顺序来显示进程；
c)	x 显示无控制终端的进程；
d)	f 用树形格式来显示进程；
e)	r 显示运行中的进程；
-ef   aux 为常用组合 
显示内容详解
f)	user:该进成属于什么用户
g)	PID:进程号
h)	%CPU:该进程占的CPU的使用率
i)	%MEM：该进程占的物理内存的百分比
j)	VSZ:占用的虚拟内存大小，以KB为单位
k)	RSS:占用的物理内存大小
l)	TTY:是否为登入着执行的程序，若为tty1-tty6，本机登录．pts/??远程登录
STAT 进程状态:
m)	R    正在运行可中在队列中可过行的；
n)	S    处于休眠状态；
o)	Z    僵尸进程；
p)	<    优先级高的进程
q)	N    优先级较低的进程
r)	s    进程的领导者（在它之下有子进程）；
s)	l    多线程
t)	+   位于后台的进程组；
Start:这个进程开始的时间
time:这个进程的运行时间
command:这个进程的实际内容
使用ps命令查看进程的时候，是一下列出来一大堆的内容，我们要想查看某个进程的PID信息的时候，往往就要结合grep命令对输出结果进程过滤．但是这样使用不太方便，我们专门有一个过滤进程的命令就是pgrep.使用pgrep命令就可以根据进程的名称／运行该进程的用户／进程所在的终端等等查询进程的PID
pgrep 
pgrep “init” 查看系统初始化进程init的PID
-l 列出程序名和进程ID；
pgrep -l “log”进程名中包含log的进程的PID号，同时列出对应的进程名
-U　指定由哪个用户产生的进程
-t　再哪个tty终端上
pgrep -l -U student -t tty1
pidof ping  查看指定进程对应的pid
使用ps命令查看到的是一个静态的进程信息，不能够连续的反馈出当前系统的运行状态，如果我想以动态刷新的方式显示各进程的状态信息，怎么办呢？
TOP　动态查看进程
按空格space立即更新；
该命令可以按CPU使用／内存使用和执行时间对任务进行排序
Ｐ键根据cpu占用情况对进程进行排序
Ｍ键根据内存占用情况排序
Ｎ键根据启动时间进行排序
n 提示显示的进程数，比如输入3，就在整屏上显示3个进程；
c 切换到命令名显示，或显示整个命令（包括参数）
k 提示输入要杀死的进程ID，目的是用来杀死该进程（默人信号为15）
kill|kill	用以关闭进程
示例：kill   [signal]   pid
kill   [signal]   进程名
使用pkill命令可以根据进程的名称／运行该进程的用户／进程所在的终端等等属性来终止特定的进程
使用who命令找到登录系统中的可疑用户，使用pkill命令终止再对应终端的进程
示例：
who | grep -v “root”
pkill -9 -t pts/1
命令加上&将该命令调入后台作业 可以通过jobs 查询
nice  -n(指定创建进程优先级-20～19之间 )   进程优先级命令 
renice  -n  pid 调整指定pid进程的优先级
前台作业调到后台 bg + 编号  让位于后台已经停止的命令继续在后台运行 
后台作业调到前台 fg + 编号   把位于 后台作业调到前台
进程优先级值的范围从-20到19。值越低，优先级越高。
Linux计划任务管理
linux通过atd和crond这两个系统服务实现一次性／周期性计划任务的功能．
/etc/init.d/atd  status（service  atd status） 可以查看atd服务进程是否启用 
用户的计划任务，只执行一次，例如今晚关机，一次性的计划任务，用at
计划任务后台需要有个进程等待执行任务，at任务会有个后台任务叫做atd进程，时刻内存中运行。
atd中的d标示daemon，daemon守护神和恶魔的意思，守护进程，后台进程。
命令格式：at[参数][时间]
参考示例： at 5pm+3 days
参数：
-m 当指定的任务被完成之后，将给用户发送邮件，即使没有标准输出
-I atq的别名
-d atrm的别名
-v 显示任务将被执行的时间
-c 打印任务的内容到标准输出
-V 显示版本信息
-q<列队> 使用指定的列队
-f<文件> 从指定文件读入任务而不是从标准输入读入
-t<时间参数> 以时间参数的形式提交要运行的任务 
Linux计划任务管理（atd）
TIME：时间格式，这里可以定义出什么时候要进行 at 这项任务的时间，格式有：
#在今日的 HH:MM 时刻进行，若该时刻已超过，则明天的 HH:MM 进行此任务
HH:MM
#强制规定在某年某月的某一天的特殊时刻进行该项任务
HH:MM YYYY-MM-DD
#强制规定在某年某月的某一天的特殊时刻进行该项任务
HH:MM[am|pm] [Month] [Date]
#在某个时间点再加几个时间后才进行该项任务
HH:MM[am|pm] + number [minutes|hours|days|weeks]
计划任务设定后，在没有执行之前我们可以用atq命令来查看系统没有执行工作任务
删除已经设置的任务： atrm 7（任务编号）
我们可以利用 /etc/at.allow 与 /etc/at.deny 这两个文件来进行 at 的使用限制。加上这两个文件后， at 的工作情况是这样的：
先找寻 /etc/at.allow 这个文件，写在这个文件中的使用者才能使用 at ，没有在这个文件中的使用者则不能使用 at (即使没有写在 at.deny 当中);
如果 /etc/at.allow 不存在，就寻找 /etc/at.deny 这个文件，若写在这个 at.deny 的使用者则不能使用 at ，而没有在这个 at.deny 文件中的使用者，就可以使用 at 命令了。
如果两个文件都不存在，那么只有 root 可以使用 at 这个命令
Linux计划任务管理（crond）
crond 是linux下用来周期性的执行某种任务或等待处理某些事件的一个守护进程，与windows下的计划任务类似，当安装完成操作系统后，默认会安装此服务 工具，并且会自动启动crond进程，crond进程每分钟会定期检查是否有要执行的任务，如果有要执行的任务，则自动执行该任务。
Linux下的任务调度分为两类，系统任务调度和用户任务调度。
在/etc目录下有一个crontab文件，这个就是系统任务调度的配置文件
使用者权限文件：
/etc/cron.deny	说明：该文件中所列用户不允许使用crontab命令
/etc/cron.allow	说明：该文件中所列用户允许使用crontab命令
/var/spool/cron/	说明：所有用户crontab文件存放的目录,以用户名命名
用户所建立的crontab文件中，每一行都代表一项任务，每行的每个字段代表一项设置，它的格式共分为六个字段，前五段是时间设定段，第六段是要执行的命令段，格式如下： minute   hour   day   month   week   command
minute： 表示分钟，可以是从0到59之间的任何整数。
hour：表示小时，可以是从0到23之间的任何整数。
day：表示日期，可以是从1到31之间的任何整数。
month：表示月份，可以是从1到12之间的任何整数。
week：表示星期几，可以是从0到7之间的任何整数，这里的0或7代表星期日。
command：要执行的命令，可以是系统命令，也可以是自己编写的脚本文件。
在以上各个字段中，还可以使用以下特殊字符：
星号（*）：代表所有可能的值，例如month字段如果是星号，则表示在满足其它字段的制约条件后每月都执行该命令操作。
逗号（,）：可以用逗号隔开的值指定一个列表范围，例如，“1,2,5,7,8,9”
中杠（-）：可以用整数之间的中杠表示一个整数范围，例如“2-6”表示“2,3,4,5,6”
正斜线（/）：可以用正斜线指定时间的间隔频率，例如“0-23/2”表示每两小时执行一次。同时正斜线可以和星号一起使用，例如*/10，如果用在minute字段，表示每十分钟执行一次。
/etc/crontab文件包括下面几行：
[root@localhost ~]# cat /etc/crontab 
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=""HOME=/
 
# run-parts
51 * * * * root run-parts /etc/cron.hourly
24 7 * * * root run-parts /etc/cron.daily
22 4 * * 0 root run-parts /etc/cron.weekly
42 4 1 * * root run-parts /etc/cron.monthly
前 四行是用来配置crond任务运行的环境变量，第一行SHELL变量指定了系统要使用哪个shell，这里是bash，第二行PATH变量指定了系统执行 命令的路径，第三行MAILTO变量指定了crond的任务执行信息将通过电子邮件发送给root用户，如果MAILTO变量的值为空，则表示不发送任务 执行信息给用户，第四行的HOME变量指定了在执行命令或者脚本时使用的主目录。第六至九行表示的含义将在下个小节详细讲述。
crontab命令详解
1．命令格式：
crontab [-u user] file
crontab [-u user] [ -e | -l | -r ]
2．命令功能：
通过crontab 命令，我们可以在固定的间隔时间执行指定的系统指令或 shell script脚本。时间间隔的单位可以是分钟、小时、日、月、周及以上的任意组合。这个命令非常设合周期性的日志分析或数据备份等工作。
3．命令参数：
-u user：用来设定某个用户的crontab服务，例如，“-u ixdba”表示设定ixdba用户的crontab服务，此参数一般有root用户来运行。
file：file是命令文件的名字,表示将file做为crontab的任务列表文件并载入crontab。如果在命令行中没有指定这个文件，crontab命令将接受标准输入（键盘）上键入的命令，并将它们载入crontab。
-e：编辑某个用户的crontab文件内容。如果不指定用户，则表示编辑当前用户的crontab文件。
-l：显示某个用户的crontab文件内容，如果不指定用户，则表示显示当前用户的crontab文件内容。
-r：从/var/spool/cron目录中删除某个用户的crontab文件，如果不指定用户，则默认删除当前用户的crontab文件。
-i：在删除用户的crontab文件时给确认提示。
删除crontab文件
要删除crontab文件，可以用：
    $ crontab -r
恢复丢失的crontab文件
如果不小心误删了crontab文件，假设你在自己的$ H O M E目录下还有一个备份，那么可以将其拷贝到/var/spool/cron/<username>，其中<username>是用户名。如果由于权限问题无法完成拷贝，可以用：
     $ crontab <filename>
使用实例
实例1：每1分钟执行一次command
命令：
* * * * * command
实例2：每小时的第3和第15分钟执行
命令：
3,15 * * * * command
实例3：在上午8点到11点的第3和第15分钟执行
命令：
3,15 8-11 * * * command
实例4：每隔两天的上午8点到11点的第3和第15分钟执行
命令：
3,15 8-11 */2 * * command
实例5：每个星期一的上午8点到11点的第3和第15分钟执行
命令：
3,15 8-11 * * 1 command 
实例6：每晚的21:30重启smb 
命令：
30 21 * * * /etc/init.d/smb restart
实例7：每月1、10、22日的4 : 45重启smb 
命令：
45 4 1,10,22 * * /etc/init.d/smb restart
Linux电源管理命令
shutdown	安全关机
poweroff		立刻关机 
halt		立刻关机
reboot		重新启动
shutdown -h 10 10		分钟后自动关机 
参数	长参数	描叙
-a		Use /etc/shutdown.allow.
-c		中断关机：当执行"shutdown -h 12:00"指令时，只要按+键就可以中断关机的指令
-f		重新启动时不进行磁盘检测（fsck）
-F		重新启动时进行磁盘检测（fsck）
-h		关闭电源
-k		模拟关机（不是真的关机），只是向登录者发送警告信息出去！
-n		不调用init进程进行关机，而是强行关机
-r		关闭系统然后重新启动，类似于Windows平台restart
-t		延迟关机的时间
-w		仅做测试，并不真的将系统重新开机，只会把重开机的数据写入/var/log目录下的wtmp记录文件
	--help	显示命令在线帮助
Vim概述
基本上 vi/vim 共分为三种模式，分别是命令模式（Command mode），输入模式（Insert mode）和底线命令模式（Last line mode
命令模式：
用户刚刚启动 vi/vim，便进入了命令模式。 
此状态下敲击键盘动作会被Vim识别为命令，而非输入字符。比如我们此时按下i，并不会输入一个字符，i被当作了一个命令。 
以下是常用的几个命令： 
i 切换到输入模式，以输入字符。
x 删除当前光标所在处的字符。
: 切换到底线命令模式，以在最底一行输入命令。
若想要编辑文本：启动Vim，进入了命令模式，按下i，切换到输入模式。 
命令模式只有一些最基本的命令，因此仍要依靠底线命令模式输入更多命令
输入模式
在命令模式下按下i就进入了输入模式。 
在输入模式中，可以使用以下按键：
字符按键以及Shift组合，输入字符
ENTER，回车键，换行
BACK SPACE，退格键，删除光标前一个字符
DEL，删除键，删除光标后一个字符
方向键，在文本中移动光标
HOME/END，移动光标到行首/行尾
Page Up/Page Down，上/下翻页
Insert，切换光标为输入/替换模式，光标将变成竖线/下划线
ESC，退出输入模式，切换到命令模式
底线命令模式
在命令模式下按下:（英文冒号）就进入了底线命令模式。 
底线命令模式可以输入单个或多个字符的命令，可用的命令非常多。 
在底线命令模式中，基本的命令有（已经省略了冒号）：
q 退出程序
w 保存文件
按ESC键可随时退出底线命令模式。
Vim  命令行命令
hjkl上下左右移动
G光标到最后一行
gg光标到第一行
5G移动到第五行，
:2光标移动到指定行
v选中
y复制
p粘贴
yy复制一行
5yy复制5行
dd删除一行
5dd删除5行(其实是剪切)
cc是删除一行并且进入插入模式
u撤销
ctrl+r反撤销
/keyword查找(但是搜索后，再打开其他文件，也会显示搜索结果，所以搜索完要取消高亮显示 :nohl)，n下一个关键字，N上一个关键字
     :w保存
:wq 保存退出  =  :x:q 
退出:q! 修改了直接退出
:nohl  取消高亮
:s/root/redhat        将当前光标所在行的第一个root替换redhat，
:%s/root/redhat        将全文的第一个root替换redhat，
:s/root/redhat/g  将当前光标所在行全行全部替换，
:%s/root/redhat/g  全文全部替换，
:s/root/redhat/gi将当前光标所在行全行不缺分大小写全局替换，
:%s/root/redhat/gi全文不缺分大小写全局替换，
:set nu  设置行号，
:set nonu取消行号，
:nohl  取消高亮
:set把能set的内容显示出来，
set all 更多的set选项，  
：！ Ls –l /root临时执行一些命令 ，  
:.!date把命令结果写入文本编辑器，:
10,19w  /tmp/new.txt  写入新文件
:9w >> /tmp/new.txt  第九行追加到文件里
帮助文档：help查看vim的帮助文档，看编辑器怎么用
:help usr_02.txt 打开指定帮助文档
:q退出help
vimtutor vim编译器的教程
yum –y groupinstall “Chinese Support”安装中文支持包临时修改终端变量   
locale –a 显示当前支持的字符编码，
locale –a |grep zh查看中文相关
echo $LANG查看变量
LANG=zh_CN.utf8   修改变量，就会是中文提示输出
此时vimtutor是中文版的提示，man也会有部分是中文版的写入/etc/profile就是永久的设置
VIM机制多用户操作防止数据破坏
Git分支管理
G我们已经知道，每次提交，Git都把它们串成一条时间线，这条时间线就是一个分支。截止到目前，只有 一条时间线，在Git里，这个分支叫主分支，即master分支。HEAD严格来说不是指向提交，而是指向master，master才是指向提交的，所以，HEAD指向的就是当前分支。
git checkout -b dev     创建dev分支，然后切换到dev分支
git checkout命令加上-b参数表示创建并切换，相当于以下两条命令：
git branch dev 
git checkout dev
git branch命令会列出所有分支，当前分支前面会标一个*号
git checkout master   以切换回master分支
git merge dev      合并dev分支到master分支
it分支管理

Git分支管理（主要命令）
查看分支：git branch
创建分支：git branch <name>
切换分支：git checkout <name>
创建+切换分支：git checkout -b <name>
合并某分支到当前分支：git merge <name
删除分支：git branch -d <name>、
Python环境搭建
1，	在www.python.org  python官网下载python源码仓库
2，	解档
3，	进入解档目录
4，	执行 sudo yum  install  -y  gcc
5，	执行 sudo yum  install  -y  zlib*
6，	.  /  configure
7，	执行 make
8，	执行sudo  make install
9，	执行 ln  -s /usr/local/bin/python3   /usr/bin/python3
Liunx系统pycharm安装
1，	在pycharm官网下载pycharm源码包
2，	解档
3，	执行 ln -s 链接源 目标链接【install. dir】/bin/pycharm.sh/usr/bin/pycharm(install.-dir 为解码后的目录路径)
4，	执行pycharm  打开pycharm编辑器
5，	修改运行python版本为python3
Linux系统老师总结
Linux学习
1》文件操作
	查看：tree path|dir  以树状结构查看path|dir指定的目录内容
	符号：.|..|-|～|/  当前|上一级|上一次|当前用户家|根
	pwd：查看当前工作目录的绝对路径
	ls：查看指定的path（路径）或dir下的文件
		-l 长格式  -a 全部，包含隐藏文件  -d查看目录本身  -h 人性化
	cat：查看文件内容，一次性显示
	less：查看文件内容，分页显示，结束不退出
	more：查看文件内容，分页显示，结束时退出
	tail：查看文件结尾  -f 动态，一般查看log日志
	head -n：一般查看文件头部n行
	touch：touch filename 若filename不存在则创建，否则修改文件时间戳
	stat：stat fliename 查看文件状态属性
	rm：删除文件
		-r 递归删除目录  -f强制，不提示删除  -i 交互模式删除
	mkdir：创建目录  -p 递归创建目录
	cp：cp 源 目标  将源位置文件复制到目标位置
		-r 复制目录文件  -p 保留源权限属性
	mv：mv 源 目标  将源位置文件移动到目标位置 【参数同cp】
	scp：scp 源 目标 将源位置文件复制到目标位置，需要ssh协议以及服务支撑
		目标源格式：用户名@主机地址：端口号默认22/文件路径
	wc：统计文件内容
		-l 行数  -w 单词  -c 字符
	cut：按列显示内容
		-d 指定列分隔符 单字符   -f 显示列编号，从1开始
	file：查看文件内容
	grep：过滤内容
		-v 匹配之外，过滤匹配为正则表达式
	>>：输出重定向并追加
	>：输出重定向并覆盖【前边命令的输出，输出到后面的文件或管道文件中】
	|：管道【前一个命令的输出作为第二个命令的输入】
	du：统计文件大小  -s 统计目录
2》用户操作
	whoami：查看当前工作用户名
	who：查看当前登陆用户
	/etc/passwd：该文件保存系统中的所有用户信息
	/etc/shadow：该文件保存用户的密码及密码策略
	/etc/group：该文件保存用户组的信息
	useradd：创建用户
		-d 指定用户家目录  -s 指定用户登陆shall  -g 指定用户组id
	userdel：删除用户
		-r 删除同时删除家目录及邮件文件
	usermod：修改用户
		-d 修改用户家目录  -s 修改用户登陆shall  -a 追加  -G 附加组  
		-g 默认组
	passwd：修改用户密码 【不指定用户名时则修改当前用户密码】
	su：切换用户
	sudo：临时获取权限
	visudo：编辑sudo设置
	exit：用户退出
	groupadd：创建组
	groupdel：删除组
3》权限操作
	chmod：修改权限
		u|g|o|a  +|-  r|w|x|s|t
		针对拥有着|拥有组|其他人|所有人  新增|减少  读|写|执行|二进制临 		时|以及临时目录
		r=4 w=2 x=1 suid=4 sgid=2 sticky=1 umask=0002（默认值）
	chmod nnn fliename：按指定权限模型授予文件权限【读|写|执行】
	chmod nnnn fliename：按指定权限模型授予文件权限
	chown：修改文件用户所属用户信息
		变化形式：.|:
			fliename.（fliename:）文件名    同时修改用户及用户组
			fliename.fliename1（fliename：fliename1）文件名        				修改用户为fliename，组为fliename1
			.|:fliename 修改用户组
			fliename 修改拥有者
	chgrp：修改文件所属组
	getfacl：查看文件的acl权限
	setfacl：设置权限
		-m 针对某个用户或组设置acl权限【setfacl -m u：username：权限 fil			e/dir】
		-x 删除某个用户或组的acl权限【setfacl -x g：tgroup 文件名】
		-b 删除整个acl权限【setfacl -b 文件名】
		-R 递归设置
4》软件安装及服务操作
	源仓库安装方式：
		yum install softpackage【redhat，centos，fedora】
		apt-get install softpackage【deb】
	源码安装：
		1》下载
		2》解档  tar -xcvfzjt
			参数意义：解档|建档|过程可见|指定文件|gzip格式|bz2格式|				查看
		3》进入解档目录
		4》查看文档【一般文档名为RESDME.md】
		5》一般方法：./configure  make  sudo make install
		6》软连接至/usr/bin/中   ln -s 链接源 链接目标
	服务管理命令：
		【centos7及以上版本，radhat7及以上版本，fadora16及以上版本】
		systemctl start|stop|reload|restart|enable|disable|status serric		ename
		启动|停止|重置|重起|开机启动|开机不启动|查看状态
		mariadb -sever 或 mysgld
		【ubuntu】
		service servicename （参数内容同上）
5》计划任务
	一次性计划任务：
		at：时间 回车 任务命令 回车 ....... ctrl+d（退出）
		atrm：删除任务 后跟任务编号
		atq：查询任务
	周期性计划任务：
		crantab 回车 分 时 日 月 周 命令 回车.......ctrl+d（退出）
		*|-|/|， 通配|区间|步进|同时
6》git操作
	1》创建目录  mkdir mygit
	2》进入目录  cd mygit/
	3》创建仓库  git init
	4》操作文件  
	5》加入暂存区  git add 文件名
	6》提交（必须使用-m进行注释）git commit -m "注释"
	命令均在仓库中运行：
		git init： 创建仓库
		git status：查看仓库状态
		git log：查看仓库日志
		git reflog：查看操作日志
		git reset --hard 强制回退 HEAD指向当前版本 ^向前一个版本
			~n向前n个版本  亦可使用commiyid
		git add：加入暂存区  *全部通配，可使用正则匹配
		git commit：提交  -m "注释"
		git chechout：切换分支 -b 创建分支并切换（后跟分支名）
		git merge：合并指定分支到当前分支
		git branch：查看或创建分支 -d 删除分支（后跟分支名为创建，否则不			    跟分支名为查看）
	远程仓库操作：
		git clone：（后跟ssh地址）在当前目录下克隆一个远程仓库，该仓库文			    件夹与远程仓库名同名
		以下命令在clone库文件夹下执行：
			git remote add 别名 ssh地址：添加远程别名
			git push 别名：推送当前仓库内容到远程仓库
		ssh-keygen -t rsa -C username：根据用户名创建rsa密钥对
7》python环境搭建
	1》去www.python.org python官方网站下载python源码包
	2》解档
	3》进入解档目录
	4》执行sudo yum install -y gcc
	5》执行sudo yum install -y zlib*
	6》执行./configure  make  sudo make install
	7》执行ln -s /usr/local/bin/python3 /usr/bin/python3
	8》去pycharm官方网站下载pycharm源码包
	9》解档
	10》执行ln -s{install_dir}/bin/pycharm.sh /usr/bin/pycharm
	    【install_dir为解档后的目录路径】
	11》执行pycharm打开pycharm编辑器
	12》修改运行python版本为python3
8》进程管理
	pstree：查看进程树
	ps：查看进程【常用参数】-aux  -ef
	top：动态方式查看进程
		相关操作详看ppt（后期补充）
	命令&将命令以后台方式运行：
		jobs：查看后台进程组
		bg + 后台进程组编号：将后台挂起，进程重新启动
		fg + 后台进程组编号：将后台进程调至前台运行
		ctrl+c：中断当前前台进程
		nice -n 命令：将命令从n优先级运行
		nice -n pid：将指定进程优先级改为n
			     【进程优先级-20～19，数值越小，优先级越高】
		kill -signol pid：向指定进程发送信号【1信号：重置/2信号：中断/9  				  信号：强制退出/15信号：正常退出】
		pkill -signol：向参数指定的一类进行发送信号
			-t：指定终端号
			-u：指定进程所属用户
			-g：指定进程所属组
		pgrep：根据进程名查询进程pid
			-l：显示进程名，可使用正则匹配进程名
9》电源管理
	shutdown：关机
	reboot：重起
	poweroff：立即关机
10》命令窗口
	vim编辑界面：
		i：进入插入模式
		a：当前位置之后进入插入模式
		s：删除当前字符进入插入模式
		x：删除当前字符
		dd：删除当前行
		gg：光标移动到第一行
		nG：光标移动到第n行
		G：移动到最后一行
		:：进入底线模式
		:!：临时执行命令
		:.!：将执行的命令结果打印到当前位置
		cc：删除当前行并进入编辑模式
		y：复制
		p：粘贴
		nyy：复制n行
		v：进入选择模式
			h：光标前移
			j：光标下移
			k：光标上移
			l：光标后移
		u：撤销
		ctrl+r：反撤销
		end：跳到行尾
		home：跳到行首
		:w：写入
		:w>>文件名：写入后面的文件内
		:w!：强制写入
		:q：退出
		1，9w>>文件名：1-9行的内容输出到文件内
【以上内容为linux基础命令，后有机会会继续补充】
