import matplotlib as mpl
import matplotlib.pyplot as plt
import math as ma
# 定义轨迹函数
def cannon(sita, v0, model,g,dt):   # 定义角度 初速度 模式 重力加速度 步长
    x = 0
    y = 0
    v_x = v0*ma.cos(sita*ma.pi/180)
    v_y = v0*ma.sin(sita*ma.pi/180)
    B0 = 4*0.00001
    x_t = [x]                       #构建数值解x的列表
    y_t = [y]                       #构建数值解y的列表
    v_x_t = [v_x]
    v_y_t = [v_y]
    dx = v_x * dt
    dv_x = -B0*ma.sqrt(v_x*v_x+v_y*v_y)*v_x*dt
    dy = v_y*dt
    dv_y = (-g-B0*ma.sqrt(v_x*v_x+v_y*v_y)*v_y)*dt
    t_list = [0]
    i = 0
    if (model == 1):
        while (y >=0):  # 飞行中
            B = B0
            i += 1
            x = x + dx
            v_x = v_x + dv_x
            y = y + dy
            v_y = v_y + dv_y
            x_t.append(x)  # 将新的步长后的位置
            v_x_t.append(v_x)
            y_t.append(y)
            v_y_t.append(v_y)
            t_list.append(i * dt)
            dx = v_x * dt
            dv_x = -B * ma.sqrt(v_x * v_x + v_y * v_y) * v_x * dt
            dy = v_y * dt
            dv_y = (-g - B * ma.sqrt(v_x * v_x + v_y * v_y) * v_y) * dt
    elif(model ==2) :
        while (y >= 0):
            i += 1
            x = x + dx
            v_x = v_x + dv_x
            y = y + dy
            v_y = v_y + dv_y
            x_t.append(x)
            v_x_t.append(v_x)
            y_t.append(y)
            v_y_t.append(v_y)
            t_list.append(i * dt)
            B = B0 * ma.exp(-y/10000)    #等温
            dx = v_x * dt
            dv_x = -B * ma.sqrt(v_x * v_x + v_y * v_y) * v_x * dt
            dy = v_y * dt
            dv_y = (-g - B * ma.sqrt(v_x * v_x + v_y * v_y) * v_y) * dt
    elif(model ==3):
        while (y >=0):
            i += 1
            x = x + dx
            v_x = v_x + dv_x
            y = y + dy
            v_y = v_y + dv_y
            x_t.append(x)
            v_x_t.append(v_x)
            y_t.append(y)
            v_y_t.append(v_y)
            t_list.append(i * dt)
            B = B0 * ma.pow((1-(6.5*0.001*y/300)),2.5)          #绝热
            dx = v_x * dt
            dv_x = -B * ma.sqrt(v_x * v_x + v_y * v_y) * v_x * dt
            dy = v_y * dt
            dv_y = (-g - B * ma.sqrt(v_x * v_x + v_y * v_y) * v_y) * dt
    else:
        while (y >=0):
            i += 1
            x = x + dx
            v_x = v_x + dv_x
            y = y + dy
            v_y = v_y + dv_y
            x_t.append(x)
            v_x_t.append(v_x)
            y_t.append(y)
            v_y_t.append(v_y)
            t_list.append(i * dt)
            B = B0 * ma.pow((1 - (6.5 * 0.001 * y / 300)), 2.5)
            gy=g*(6371*6371*1000000/((6371000+y)*(6371000+y)))    #     g修正
            dx = v_x * dt
            dv_x = -B * ma.sqrt(v_x * v_x + v_y * v_y) * v_x * dt
            dy = v_y * dt
            dv_y = (-gy - B * ma.sqrt(v_x * v_x + v_y * v_y) * v_y) * dt
    result = {'list_x': x_t, 'list_y': y_t,'list_t': t_list,'total': [x,max(y_t)]}                  #传递参数
    return (result)
#  创建带输入提示的函数，可通过此函数调用上方函数画出轨迹
def show_():
    print('请顺序输入角度 速度 模式 重力加速度 步长,以回车间隔\n')
    print('模式代码为 1 2 3 4 ，1为阻力不变，2为等温模型，3为绝热模型，4为绝热且重力加速可变模型 ，\n')
    sita = float(input())
    v0 = float(input())
    model = int(input())
    g = float(input())
    dt = float(input())
    result=cannon(sita, v0, model, g, dt)
    x=result.get('list_x')
    y=result.get('list_y')
    plt.plot(x,y,label = ('sita= '+str(sita)+'v0='+str(v0)+'model='+str(model)+'dt='+str(dt)+'g='+str(g)))
    plt.legend(loc='best')
    plt.xlabel('x/m')
    plt.ylabel('y/m')
    obj = result.get('total')
    print('飞行距离：', obj[0], '最高高度:', obj[1])
    plt.show()
#计算发射角度的函数
def target(m):
    v0=750
    sita=5
    g=9.8
    dt=0.0001
    while (sita<=89):
        x = 0
        y = 0
        v_x = v0 * ma.cos(sita * ma.pi / 180)
        v_y = v0 * ma.sin(sita * ma.pi / 180)
        B0 = 4 * 0.00001
        x_t = [x]  # 构建数值解x的列表
        y_t = [y]  # 构建数值解y的列表
        v_x_t = [v_x]
        v_y_t = [v_y]
        dx = v_x * dt
        dv_x = -B0 * ma.sqrt(v_x * v_x + v_y * v_y) * v_x * dt
        dy = v_y * dt
        dv_y = (-g - B0 * ma.sqrt(v_x * v_x + v_y * v_y) * v_y) * dt
        t_list = [0]
        i = 0
        while (y >=0):
            i += 1
            x = x + dx
            v_x = v_x + dv_x
            y = y + dy
            v_y = v_y + dv_y
            x_t.append(x)
            v_x_t.append(v_x)
            y_t.append(y)
            v_y_t.append(v_y)
            t_list.append(i * dt)
            B = B0 * ma.pow((1 - (6.5 * 0.001 * y / 300)), 2.5)
            gy=g*(6371*6371*1000000/((6371000+y)*(6371000+y)))
            dx = v_x * dt
            dv_x = -B * ma.sqrt(v_x * v_x + v_y * v_y) * v_x * dt
            dy = v_y * dt
            dv_y = (-gy - B * ma.sqrt(v_x * v_x + v_y * v_y) * v_y) * dt
        if(abs(x-m)<=60):
            return(sita)
        else:
            sita = sita + 1
    return(1)
