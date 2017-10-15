# coding=UTF-8
background_image_filename = 'background.png'
cannon_image_filename = 'ball.png'
import pygame
from pygame.locals import *
from sys import exit
import math as ma
# 定义轨迹函数
def cannon(sita, v0):   # 定义角度 初速度 模式 重力加速度 步长
    g = 9.8
    dt = 0.001
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
    result = {'list_x': x_t, 'list_y': y_t,'list_t': t_list,'total': [x,max(y_t)],'maxi':i}                  #传递参数
    return (result)
pygame.init()
screen = pygame.display.set_mode((1000, 600), 0, 32)
background = pygame.image.load(background_image_filename).convert()
ball = pygame.image.load(cannon_image_filename).convert_alpha()
x, y = 100,100
sita=45
v0=750
tru=1
tt=1
font = pygame.font.SysFont("arial", 40)
font2 = pygame.font.SysFont("simsunnsimsun", 40)
xt = 500
yt = 50
text='sita= '+str(sita)+' '+'V0= '+str(v0)+' '
text_surface = font.render(text, True, (0, 0, 255))
text_surface2 = font2.render(u'按数字1开始，左右键控制速度，上下键控制角度', True, (0, 0, 255))
while True:
    screen.blit(background, (0, 0))
    screen.blit(ball, (100 - 25, 500 - 18))
    screen.blit(text_surface, (500, 50))
    screen.blit(text_surface2, (100, 10))
    pygame.display.update()
    while tru:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type != KEYDOWN:
                pass
            elif event.type == KEYDOWN:
                if  event.key != K_1:
                        if event.key == K_UP:
                            sita = sita + 1
                            if sita == 90:
                                sita = 1
                            else:
                                pass
                        elif event.key == K_DOWN:
                            sita = sita - 1
                            if sita == 0:
                                sita = 90
                            else:
                                pass
                        elif event.key == K_LEFT:
                            v0 = v0 - 1
                            if v0 == 700:
                                v0 = 800
                            else:
                                pass
                        elif event.key == K_RIGHT:
                            v0 = v0 + 1
                            if v0 == 800:
                                v0 = 700
                            else:
                                pass
                        else:
                            pass
                else:
                    tru=0
                text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
                text_surface = font.render(text, True, (0, 0, 255))
                screen.blit(background, (0, 0))
                screen.blit(ball, (100 - 25, 500 - 18))
                screen.blit(text_surface, (500, 50))
                screen.blit(text_surface2, (100, 10))
                pygame.display.update()
    while tt:
      for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        result = cannon(sita, v0)
        x = result.get('list_x')
        y = result.get('list_y')
        i = result.get('maxi')
        p = int(i / 1000)
        x_ = [0]
        y_ = [0]
        q = 0
        while (q <= 999):
            x_.append(int(x[q * p] / 50))
            y_.append(int(y[q * p] / 50))
            q += 1
            screen.blit(background, (0,0))
            screen.blit(ball, (100+x_[q-1]-25, 500-y_[q-1]-18))
            # 在新的位置上画图
            pygame.display.update()
        x, y = 100, 100
        sita = 45
        v0 = 750
        pygame.display.update()
        tt = 0
    tru = 1
    tt = 1
