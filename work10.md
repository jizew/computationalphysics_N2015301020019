# 第十次作业
------
## 学号 2015301020019  姓名 王宠霖
----
## 摘要 

此次作业为计算模拟电势的分布，使用弛豫法，通过给定的初始条件和边界条件，通过把电场分割成均匀网格，逐步演化，经过足够多次的迭代后，就能得到比较精确的解。
主要进行的工作为将三维的势场分布变为二位形式展示。

## 正文
### 思路与源码
关于电势的模拟计算过程已经有详细的介绍（见参考1），此次在引用的代码基础上，加入了控制结束条件（ΔV之和小于0.0001），同时考虑到观察计算机屏幕上观察3D效果不容易清楚的看明白电势的分布，因此进行了用颜色来表征Z（即电势大小的工作）。

具体实现如下：
```
while 1:
#for i in range(0, 60):     //改动前代码             
    VO = V[m]
    K = [[0 for col in range(65)] for row in range(65)]
    Delta_V = 0
    for i in range(1, 64):
        for j in range(1, 64):
            if (VO[i][j] != 1 and VO[i][j] != -1):
                K[i][j] = round((VO[i - 1][j] + VO[i + 1][j] + VO[i][j - 1] + VO[i][j + 1]) / 4, 2)
                Delta_V += abs(VO[i][j] - K[i][j])
    for i in range(0, 65):
        for j in range(0, 65):
            K[i][j] = K[i][j] + V[0][i][j]
    V.append(K)
    m+=1
    if(Delta_V<=0.0001):     //增加控制结果精度的语句
        break
 ```
 
接下来进行的是生成二维显示三维效果，为了实现这个效果，我想到使用scatter逐点控制点颜色来实现绘制，为了达到这个目的真的是受尽折磨。。。
好吧我们先看看代码：
------   
```
C=[['#ffffff' for col in range(65)] for row in range(65)]  #初始化颜色矩阵
for i in range(0,65):
    for j in range(0,65):
        c0=V[m][i][j]
        c0=int(c0*(256*256*256-1))  #用0x000000到0xFFFFFF表示0~1的电势值
        if(c0<16):                #根据大小范围判断16进制占的位数，从而生成6位数的16进制，这里贼坑，不注意很容在下面有报错
            c1='00000'+hex(c0)[2]  #hex()函数可以将整形10进制转换为16进制字符串，我们再从第三位选起去掉0x
        elif (c0<256):
            c1='0000'+hex(c0)[2:4]
        elif (c0<16*16*16):
            c1='000'+hex(c0)[2:5]
        elif (c0<16*16*16*16):
            c1='00'+hex(c0)[2:6]
        elif (c0<16*16*16*16*16):
            c1 = '0' + hex(c0)[2:7]
        else:
            c1=hex(c0)[2:8]
        C[i][j]='#'+c1
x1=[i for i in range(0,65)]
y1=[i for i in range(0,65)]

for i in range(0,65):
    for j in range(0,65):
        cc=C[i][j]
        plt.scatter(x1[i],y1[j],s=8, c=cc,marker ='s')   #逐点画图
 ```
 在终于搞定控制颜色的一堆BUG之后，突然发现有一个贼简单的方法。。。用透明度表示电势。。。于是上面那一堆转换十六进制的东西都可以不用，只要一行代码：
 ```
 plt.scatter(x1[i], y1[j], s=8, c='b', marker='s',alpha =V[m][i][j])
 ```
 就解决问题了。。
 
 ### 效果对比展示
 首先是3D效果展示：
 ![image](https://github.com/jizew/computationalphysics_N2015301020019/blob/master/Figure_1.2.png?raw=true)
 接着为二维视角：
 ![image](https://github.com/jizew/computationalphysics_N2015301020019/blob/master/Figure_1.1.png?raw=true)
 ![image](https://github.com/jizew/computationalphysics_N2015301020019/blob/master/Figure_1.png?raw=true)
 另一种初始条件：
 ![image](https://github.com/jizew/computationalphysics_N2015301020019/blob/master/Figure_2.2.png?raw=true)
 ![image](https://github.com/jizew/computationalphysics_N2015301020019/blob/master/Figure_2.11.png?raw=true)
 ![image](https://github.com/jizew/computationalphysics_N2015301020019/blob/master/Figure_2.png?raw=true)
 
 ----
 源码链接： [python](https://raw.githubusercontent.com/jizew/computationalphysics_N2015301020019/master/tanks.py)
 ------
 ## 致谢
 参考（1）：刘庆康同学的代码以及报告 [给他点个赞](https://github.com/Cathayaliu/computationalphysics_N2015301020026)
    
