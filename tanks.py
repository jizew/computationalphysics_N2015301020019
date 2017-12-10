import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

the_origin_V = [[0 for col in range(65)] for row in range(65)]


for i in range(30,35):
    for j in range(30, 35):
        the_origin_V[i][j] = 1

'''
for i in range(15, 49):
    the_origin_V[20][i] = 1
    the_origin_V[44][i] = 1
    the_origin_V[21][i] = 1
    the_origin_V[45][i] = 1
'''
V = [the_origin_V]
Delta_V = 0
m=0
while 1:
#for i in range(0, 60):
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
    if(Delta_V<=0.0001):
        break
x = []
for i in range(0, 65):
    x.append([i for j in range(65)])
X = sum(x, [])

y = []
for i in range(0, 65):
    y.append([i for i in range(0, 65)])
'''
Y = sum(y, [])
Z1 = sum(V[0], [])
Z5 = sum(V[m], [])

fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
ax1.scatter(X, Y, Z1, s=2)

ax2.scatter(X, Y, Z5, s=2)
'''

'''
C=[['#00ff00' for col in range(65)] for row in range(65)]
for i in range(0,65):
    for j in range(0,65):
        c0=V[m][i][j]
        c0=int(c0*255)
        if(c0<16):
            c1='0'+hex(c0)[2:]
        else:
            c1=hex(c0)[2:]
        C[i][j]='#'+c1+'ff'+c1
'''

C=[['#ffffff' for col in range(65)] for row in range(65)]  #初始化颜色矩阵
for i in range(0,65):
    for j in range(0,65):
        c0=V[m][i][j]
        c0=int(c0*(256*256*256-1)) #用0x000000到0xFFFFFF表示0~1的电势值
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
        plt.scatter(x1[i],y1[j],s=8, c=cc,marker ='s')
        #plt.scatter(x1[i], y1[j], s=8, c='b', marker='s',alpha =V[m][i][j])
#plt.scatter(x[1],y[1],s=10, c=C[1][1])
#plt.scatter(x[15],y[15],s=10, c=C[30][30])
plt.show()
#print(C)