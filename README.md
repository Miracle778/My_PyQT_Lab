# 简介

上网络安全理论技术试验课做的几个实验。用的是pyqt5，有端口扫描器、注册表编辑器、U盘病毒等。

因为时间有点久了，而且当时写的时候目录结构有点乱，也没做好整理总结，所以有几个实验就不放了。这里只放两个，一个是简单的端口扫描器，另一个是注册表编辑器。

-----

# 程序运行效果

# 端口扫描器
![](https://raw.githubusercontent.com/Miracle778/blog.images/master/%E7%BD%91%E5%AE%89%E7%90%86%E8%AE%BA%E5%AE%9E%E9%AA%8C/scan.gif)

# 注册表编辑器
![](https://raw.githubusercontent.com/Miracle778/blog.images/master/%E7%BD%91%E5%AE%89%E7%90%86%E8%AE%BA%E5%AE%9E%E9%AA%8C/registryedit.gif)

-------

# 说明
时间有点久了，细节什么的也记不清了，翻了一下当时交的实验报告，实验报告里面写了实验中遇到的问题和解决方法，但编写过程没有多写，也是挺无奈，只能把实验报告搬上来参照参照，大致讲讲设计过程了。

实验报告PDF放在目录实验报告文件夹下了，是一份总的实验报告，端口扫描器和注册表编辑器的这两部分报告也在里面。

下面简单讲下设计过程。
1. 端口扫描器
主要是做了TCP connect扫描和SYN扫描两个功能，SYN扫描是利用scapy库改包发包，但是在windows上抓不到修改后的包，当时上网查到的原因好像是windows下对原始套接字做了限制，不能使用原始套接字发送TCP data，这个我当时也写进实验报告里了。**所以SYN扫描我是放在linux下面做的，上传的源码里没有该功能函数代码**
然后是Connect扫描功能，这个就简单了，直接利用TCP的特性与目标IP端口连接，根据是否超时判断是否开放。
这里用了下多线程，多线程当时是这样构思的，输入信息里输入要扫描的端口区间和要使用的线程数目。然后把线程数目作为for循环间隔进行扫描，这里不太好解释，举个例子说明一下
比如输入了扫描端口区间是1-10000，线程数是50，那么第一个线程就从1开始扫描，以50位间隔进行，到大于10000结束，第二个线程从2开始扫描，第三个线程从3开始... 即第一个线程扫描端口 1 51 101 ... ,第二个线程扫描 2 52 102...,第50个线程扫描 50 100 150...，然后这里线程函数传参里面有个pid，是为了线程同步搞的，给每个线程从0开始手动编号，然后加个判断，直到pid=输入的线程数时才输出扫描结束。
这个多线程实现方法只是当时随便一想的，可能有点sb。。。轻喷，下面是线程函数的代码
```python
    def Connect(self,ipaddr,port,port_right,blank,pid):
        #多线程
        for i in range(port,port_right+1,blank):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                sock.connect((ipaddr,i))
                self.open_port.append(i)
                self.textEdit.append('{}:open'.format(i))
            except:
                self.close_port.append(i)   # 连接超时异常即为端口未开放
            finally:
                sock.close()

        if self.spinBox.value() == pid + 1:
            self.textEdit.append('扫描结束')
        return
```

2. 注册表编辑器
这里用到python自带的`winreg`库对注册表进行访问修改等操作，因为注册表项太多了，于是采用了动态展开的方式。
一开始只有几个注册表的根键，然后通过点击生成子目录和子健及他们对应的值(子目录不展开)，这里是用点击事件传递点击的节点名称即父键，然后利用winreg包里的函数遍历生成点击节点的子健、子目录和值。
然后就是编辑注册表、冰河病毒检测这些功能，其实也就是利用鼠标点击传递当前节点的注册表键的名称，然后利用winreg里函数操作。
这个实验也挺简单的，主要是当时不熟悉pyqt的树这些控件，查文档函数浪费了点时间，所以这里也就不多讲了。


