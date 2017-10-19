# coding=UTF-8
import pygame
from pygame.locals import *
import matplotlib.pyplot as plt
from sys import exit
import math as ma
# 定义轨迹函数
def ball(sita,v0,vw,alti):   # 定义角度 初速度 模式 重力加速度 步长
    g = 9.8
    dt = 0.0001
    x = 0
    y = 1.7
    y0=alti
    v_x = v0*ma.cos(sita*ma.pi/180)
    v_y = v0*ma.sin(sita*ma.pi/180)
    v_z = 0
    B0 = 0.0039+0.0058/(1+ma.exp((ma.sqrt(v_x*v_x+v_y*v_y+v_z*v_z)-35)/5))
    x_t = [x]                       #构建数值解x的列表
    y_t = [y]                       #构建数值解y的列表
    v_x_t = [v_x]
    v_y_t = [v_y]
    dx = v_x * dt
    dv_x = -B0*ma.sqrt(((v_x-vw)*(v_x-vw)+v_y*v_y))*(v_x-vw)*dt
    dy = v_y*dt
    dv_y = (-g-B0*ma.sqrt(((v_x-vw)*(v_x-vw)+v_y*v_y))*v_y)*dt
    t_list = [0]
    i = 0
    while (y>=0):
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
        B0 = 0.0039+0.0058/(1+ma.pow(2.718281828459045, ((ma.sqrt(v_x*v_x+v_y*v_y)-35)/5)))
        B = B0 * ma.pow((1 - (6.5 * 0.001 * (y+y0) / 300)), 2.5)
        gy = g * (6371 * 6371 * 1000000 / (((6371000 + (y+y0)) * (6371000 + (y+y0))))) # g修正
        dx = v_x * dt
        dv_x = -B * ma.sqrt(((v_x - vw) * (v_x - vw) + v_y * v_y)) * (v_x - vw) * dt
        dy = v_y * dt
        dv_y = (-gy - B * ma.sqrt(((v_x - vw) * (v_x - vw) + v_y * v_y)) * v_y) * dt
    result = {'list_x': x_t, 'list_y': y_t,'list_t': t_list,'total': [x,max(y_t)],'maxi':i}                  #传递参数
    return (result)
def show_():
    print('请顺序输入  海拔,以回车间隔\n')
    #print('请顺序输入速度 风速,以回车间隔\n')
    v0 = 49
    #vw = float(input())
    vw = -10
    alti = float(input())
    #alti=0
    sita=25
    result=ball(sita,v0,vw,alti)
    total=result.get('total')
    x=total[0]
    range_x=[x]
    for i in range(1,45):
        sita=25+0.5*i
        result = ball(sita, v0, vw,alti)
        total = result.get('total')
        x = total[0]
        range_x.append(x)
        max_x=max(range_x)
    for a in range(len(range_x)):
        if(range_x[a]==max_x):
            ds=a
    max_sita = 25+ds*0.5
    lsita = [max_sita]
    lvw=[vw]
    for h in range(1,21):
        vw=-10+h
        result = ball(sita, v0, vw, alti)
        total = result.get('total')
        x = total[0]
        range_x = [x]
        for r in range(1, 45):
            sita = 25 + r*0.5
            result = ball(sita, v0, vw, alti)
            total = result.get('total')
            x = total[0]
            range_x.append(x)
            max_x = max(range_x)
        for a in range(len(range_x)):
            if (range_x[a] == max_x):
                ds = a
        max_sita = 25 + ds*0.5
        lsita.append(max_sita)
        lvw.append(vw)
    x = lvw
    y = lsita
    plt.plot(x, y,'.')
    plt.xlabel('Vwind/m/s')
    plt.ylabel('theta')
    plt.show()
    '''
    print('最远时角度为：'+str(max_sita)+'  '+str(max_x))
    result = ball(max_sita-5, v0, vw, alti)
    x1 = result.get('list_x')
    y1 = result.get('list_y')
    result = ball(max_sita+5, v0, vw, alti)
    x2 = result.get('list_x')
    y2 = result.get('list_y')
    result = ball(max_sita, v0, vw, alti)
    x = result.get('list_x')
    y = result.get('list_y')
    plt.plot(x, y,label=('sita= ' + str(max_sita) + 'v0=' + str(v0) + 'V  of wind = ' + str(vw) + 'dt=' + str(0.0001) + 'Altitude=' + str(alti)))
    plt.plot(x1,y1,label=('sita= ' + str(max_sita-5)))
    plt.plot(x2, y2, label=('sita= ' + str(max_sita + 5) ))
    plt.legend(loc='best')
    plt.xlabel('x/m')
    plt.ylabel('y/m')
    plt.title('max_X= '+str(max_x)+'m   '+'theta = '+str(max_sita))
    plt.show()
    '''
show_()
















