# coding=UTF-8
'''
background_image_filename = 'D:\pycharmdoc\qizhong\sackground.jpg'
background2_image_filename = 'D:\pycharmdoc\qizhong\sackground.png'
music_filename = 'D:\pycharmdoc\qizhong\music.mp3'
sound1_filename = 'D:\pycharmdoc\qizhong\sashe.wav'
sound2_filename = 'D:\pycharmdoc\qizhong\soom.wav'
cannon_image_filename = 'D:\pycharmdoc\qizhong\sall.png'
#cannon_image_filename = 'D:\pycharmdoc\qizhong\plane2.png'
plane_image_filename = 'D:\pycharmdoc\qizhong\plane2.png'
start_image_filename = 'D:\pycharmdoc\qizhong\start.png'
'''
background_image_filename = 'sackground.jpg'
background2_image_filename = 'sackground.png'
music_filename = 'music.mp3'
sound1_filename = 'sashe.wav'
sound2_filename = 'soom.wav'
cannon_image_filename = 'sall.png'
xlal_image_filename = 'xlal.png'
dengji_image_filename = 'dengji2.png'
#cannon_image_filename = 'D:\pycharmdoc\qizhong\plane2.png'
plane_image_filename = 'plane2.png'
start_image_filename = 'start.png'
import pygame
from pygame.locals import *
from sys import exit
import math as ma
import random as ran
import threading
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
background2 = pygame.image.load(background2_image_filename).convert()
dengji = pygame.image.load(dengji_image_filename).convert_alpha()
start = pygame.image.load(start_image_filename).convert_alpha()
pause=1
price=9
diff=3
pygame.mixer.init()
pygame.mixer.music.load(music_filename)
sound1 = pygame.mixer.Sound(sound1_filename)
sound2 = pygame.mixer.Sound(sound2_filename)
pygame.mixer.music.set_volume(10 / 100.0)
pygame.mixer.music.play(-1)
while True:
    while pause:
        xs, ys = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            screen.blit(background, (0, 0))
            #screen.blit(start, (250, 0))
            screen.blit(dengji, (270, 180))
            xs, ys = pygame.mouse.get_pos()
            font = pygame.font.SysFont("simsunnsimsun", 40)
            font2 = pygame.font.SysFont("simsunnsimsun", 30)
            text = u'上次游戏的分数为：'+str(price)+'分'
            text2 = u''+str(xs)+str(ys)
            text3 = u'点击你要挑战的等级开始游戏（1级最难）'
            if (price==0):
                text4 = u'             同学你需再努力一下'
            if (price >= 6) and(price<=8):
                if(diff==1):
                    text4 = u'很熟练啊同学，祝贺你获得青铜级合格证'
                if (diff==2):
                    text4 = u'很熟练啊同学，祝贺你获得白银级合格证'
                if (diff==3):
                    text4 = u'很熟练啊同学，祝贺你获得黄金级合格证'
            if (price >= 9):
                if(diff==1):
                    text4 = u'            优秀的防空兵'
                if (diff==2):
                    text4 = u'          白银防空兵get'
                if (diff==3):
                    text4 = u'    黄金打飞机圣手说的就是你了'
            else:pass
            text_surface = font.render(text, True, (0, 0, 255))
            text_surface2 = font.render(text2, True, (0, 0, 255))
            text_surface3 = font.render(text3, True, (0, 0, 255))
            text_surface4 = font2.render(text4, True, (255, 255, 20))
            screen.blit(text_surface, (40, 140))
            screen.blit(text_surface2, (85, 80))
            screen.blit(text_surface3, (200, 80))
            screen.blit(text_surface4, (460, 150))
            pygame.display.update()
            if (xs >= 367) and (xs <= 560) and (ys >= 179) and (ys <= 336):
                diff=3
                if event.type == MOUSEBUTTONDOWN:
                    pause = 0
            if (xs >= 290) and (xs <= 433) and (ys >= 400) and (ys <= 525):
                diff = 2
                if event.type == MOUSEBUTTONDOWN:
                    pause = 0
            if (xs >= 490) and (xs <= 638) and (ys >= 400) and (ys <= 525):
                diff = 1
                if event.type == MOUSEBUTTONDOWN:
                    pause = 0
    if (diff==1):
        screen = pygame.display.set_mode((1000, 600), 0, 32)
        background = pygame.image.load(background_image_filename).convert()
        ball = pygame.image.load(cannon_image_filename).convert_alpha()
        xlal = pygame.image.load(xlal_image_filename).convert_alpha()
        plane1 = pygame.image.load(plane_image_filename).convert_alpha()
        plane2 = pygame.image.load(plane_image_filename).convert_alpha()
        plane3 = pygame.image.load(plane_image_filename).convert_alpha()
        sita = 45
        v0 = 750
        ball_count = 10
        font = pygame.font.SysFont("arial", 40)
        font2 = pygame.font.SysFont("simsunnsimsun", 40)
        font3 = pygame.font.SysFont("simsunnsimsun", 40)
        font4 = pygame.font.SysFont("simsunnsimsun", 40)
        xt = 500
        yt = 50
        text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
        price = 0
        text3 = u'你的分数为：' + str(price)
        text4 = u'你还有' + str(ball_count) + '发炮弹~，把握机会哦少年'
        text_surface = font.render(text, True, (0, 0, 255))
        text_surface2 = font2.render(u'  ', True, (0, 0, 255))
        text_surface3 = font3.render(text3, True, (0, 0, 255))
        text_surface4 = font4.render(text4, True, (249, 139, 87))
        yp1 = ran.randint(10, 200)
        xp1 = ran.randint(900, 990)
        vp1 = ran.randint(1, 1)
        ip1 = 0
        yp2 = ran.randint(10, 200)
        xp2 = ran.randint(900, 990)
        vp2 = ran.randint(1, 1)
        ip2 = 0
        yp3 = ran.randint(10, 200)
        xp3 = ran.randint(900, 990)
        vp3 = ran.randint(1, 1)
        ip3 = 0
        tru1 = 1
        ball_count = 10
        while (tru1):
            text4 = u'你还有' + str(ball_count) + '发炮弹~，把握机会哦少年'
            text_surface4 = font4.render(text4, True, (249, 139, 87))
            screen.blit(background, (0, 0))
            screen.blit(ball, (75, 482))
            screen.blit(xlal, (7, 482))
            screen.blit(plane1, (xp1, yp1))
            screen.blit(plane2, (xp2, yp2))
            screen.blit(plane3, (xp3, yp3))
            screen.blit(text_surface, (400, 550))
            screen.blit(text_surface2, (300, 510))
            screen.blit(text_surface3, (450, 90))
            screen.blit(text_surface4, (300, 30))
            pygame.display.update()
            tru = 1
            while tru:
                while tru:
                    if (ball_count <= 0):
                        pause = 1
                        tru1 = 0
                    ip1 += 1
                    ip2 += 1
                    ip3 += 1
                    text_surface = font.render(text, True, (0, 0, 255))
                    screen.blit(background, (0, 0))
                    screen.blit(ball, (100 - 25, 500 - 18))
                    screen.blit(xlal, (7, 482))
                    # screen.blit(plane, (xp, yp))
                    if ((xp1 - ip1 * vp1) <= 0):
                        yp1 = ran.randint(10, 200)
                        xp1 = ran.randint(900, 990)
                        vp1 = 1
                        ip1 = 0
                    if ((xp2 - ip2 * vp2) <= 0):
                        yp2 = ran.randint(10, 200)
                        xp2 = ran.randint(900, 990)
                        vp2 = 1
                        ip2 = 0
                    if ((xp3 - ip3 * vp3) <= 0):
                        yp3 = ran.randint(10, 200)
                        xp3 = ran.randint(900, 990)
                        vp3 = 1
                        ip3 = 0
                    x, y = pygame.mouse.get_pos()
                    v0 = int(ma.sqrt((482 - y) * (482 - y) + (x - 75) * (x - 75))) * 2.5
                    if (v0 >= 2000):
                        v0 = 2000
                    elif (v0 <= 400):
                        v0 = 400
                    lenth = int(266 * (v0 - 400) / 1600)
                    xx = 75 + 16 + 150 * ma.cos(ma.atan((600 - y) / (x + 1)))
                    yy = 482 + 16 - 150 * ma.sin(ma.atan((600 - y) / (x + 1)))
                    pygame.draw.line(screen, (50, 50, 55), (75 + 16, 482 + 16), (xx, yy), 4)
                    pygame.draw.line(screen, (50, 50, 50), (75 + 16, 482 + 50), (75 + 16 + lenth, 482 + 50), 4)
                    screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                    screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                    screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                    screen.blit(text_surface, (400, 550))
                    screen.blit(text_surface2, (300, 510))
                    screen.blit(text_surface3, (450, 90))
                    screen.blit(text_surface4, (300, 30))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pause = 1
                                tru = 0
                                tru1 = 0
                        else:
                            pass
                        # if event.type != KEYDOWN:
                        #     pass
                        ip1 += 1
                        ip2 += 1
                        ip3 += 1
                        x, y = pygame.mouse.get_pos()
                        xx = 75 + 16 + 150 * ma.cos(ma.atan((600 - y) / (x + 1)))
                        yy = 482 + 16 - 150 * ma.sin(ma.atan((600 - y) / (x + 1)))
                        sita = int(180 * ma.atan((600 - y) / (x + 1)) / ma.pi)
                        v0 = int(ma.sqrt((482 - y) * (482 - y) + (x - 75) * (x - 75))) * 2.5
                        if (v0 >= 2000):
                            v0 = 2000
                        elif (v0 <= 400):
                            v0 = 400
                        lenth = int(266 * (v0 - 400) / 1600)
                        text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
                        text_surface = font.render(text, True, (0, 0, 255))
                        screen.blit(background, (0, 0))
                        screen.blit(ball, (100 - 25, 500 - 18))
                        # screen.blit(plane, (xp, yp))
                        pygame.draw.line(screen, (50, 50, 55), (75 + 16, 482 + 16), (xx, yy), 4)
                        pygame.draw.line(screen, (50, 50, 50), (75 + 16, 482 + 50), (75 + 16 + lenth, 482 + 50), 4)
                        screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                        screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                        screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                        screen.blit(text_surface, (400, 550))
                        screen.blit(text_surface2, (300, 510))
                        screen.blit(text_surface3, (450, 90))
                        screen.blit(text_surface4, (300, 30))
                        pygame.display.update()
                        if event.type == MOUSEBUTTONDOWN:
                            x, y = pygame.mouse.get_pos()
                            sita = int(180 * ma.atan((600 - y) / (x + 1)) / ma.pi)
                            v0 = int(ma.sqrt((482 - y) * (482 - y) + (x - 75) * (x - 75))) * 2.5 + 200
                            text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
                            text_surface = font.render(text, True, (0, 0, 255))
                            screen.blit(background, (0, 0))
                            screen.blit(ball, (100 - 25, 500 - 18))
                            screen.blit(xlal, (7, 482))
                            screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                            screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                            screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                            screen.blit(text_surface, (400, 550))
                            screen.blit(text_surface2, (300, 510))
                            screen.blit(text_surface3, (450, 90))
                            pygame.display.update()
                            if event.type == MOUSEBUTTONDOWN:
                                ball_count -= 1
                                tru = 0
            result = cannon(sita, v0)
            xb = result.get('list_x')
            yb = result.get('list_y')
            i = result.get('maxi')
            p = int(i / 1000)
            x_ = [0]
            y_ = [0]
            q = 0
            q_ = [q]
            q = 1
            while (q <= 999):
                if not tru1:
                    break
                x_.append(int(xb[q * p] / 50))
                y_.append(int(yb[q * p] / 50))
                q_.append(q)
                q += 1
            qq = 0
            while (qq < max(q_)):
                if not tru1:
                    break
                qq += 1
                ip1 += 1
                ip2 += 1
                ip3 += 1
                screen.blit(background, (0, 0))
                screen.blit(ball, (100 + x_[qq] - 25, 500 - y_[qq] - 18))
                text_surface2 = font2.render(u'                   冷却ing', True, (255, 0, 0))
                text_surface3 = font2.render(text3, True, (0, 0, 255))
                screen.blit(text_surface2, (100, 510))
                screen.blit(text_surface3, (300, 90))
                if (ma.sqrt(((100 + x_[qq] - 25) - (xp1 - ip1 * vp1)) * ((100 + x_[qq] - 25) - (xp1 - ip1 * vp1)) + (
                            (500 - y_[qq] - 18) - yp1) * ((500 - y_[qq] - 18) - yp1)) <= 20):
                    yp1 = ran.randint(10, 200)
                    xp1 = ran.randint(900, 990)
                    vp1 = 1
                    ip1 = 0
                    price += 1
                    screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                    pygame.mixer.music.pause()
                    pygame.mixer.music.set_volume(80 / 100.0)
                    sound2.play()
                    pygame.time.delay(100)
                    pygame.mixer.music.set_volume(10 / 100.0)
                    pygame.mixer.music.unpause()
                    break
                screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                if (ma.sqrt(((100 + x_[qq] - 25) - (xp2 - ip2 * vp2)) * ((100 + x_[qq] - 25) - (xp2 - ip2 * vp2)) + (
                            (500 - y_[qq] - 18) - yp2) * ((500 - y_[qq] - 18) - yp2)) <= 20):
                    yp2 = ran.randint(10, 200)
                    xp2 = ran.randint(900, 990)
                    vp2 = 1
                    ip2 = 0
                    price += 1
                    screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                    pygame.mixer.music.pause()
                    pygame.mixer.music.set_volume(80 / 100.0)
                    sound2.play()
                    pygame.time.delay(100)
                    pygame.mixer.music.set_volume(10 / 100.0)
                    pygame.mixer.music.unpause()
                    break
                screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                if (ma.sqrt(((100 + x_[qq] - 25) - (xp3 - ip3 * vp3)) * ((100 + x_[qq] - 25) - (xp3 - ip3 * vp3)) + (
                            (500 - y_[qq] - 18) - yp3) * ((500 - y_[qq] - 18) - yp3)) <= 20):
                    yp3 = ran.randint(10, 200)
                    xp3 = ran.randint(900, 990)
                    vp3 = 1
                    ip3 = 0
                    price += 1
                    screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                    pygame.mixer.music.pause()
                    pygame.mixer.music.set_volume(80 / 100.0)
                    sound2.play()
                    pygame.time.delay(100)
                    pygame.mixer.music.set_volume(10 / 100.0)
                    pygame.mixer.music.unpause()
                    break
                screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                if ((xp1 - ip1 * vp1) <= 0):
                    yp1 = ran.randint(10, 300)
                    xp1 = ran.randint(900, 990)
                    vp1 = ran.randint(1, 1)
                    ip1 = 0
                if ((xp2 - ip2 * vp2) <= 0):
                    yp2 = ran.randint(10, 300)
                    xp2 = ran.randint(900, 990)
                    vp2 = ran.randint(1, 1)
                    ip2 = 0
                if ((xp3 - ip3 * vp3) <= 0):
                    yp3 = ran.randint(10, 300)
                    xp3 = ran.randint(900, 990)
                    vp3 = ran.randint(1, 1)
                    ip3 = 0
                # 在新的位置上画图
                pygame.display.update()
                x, y = 100, 100
                sita = 45
                v0 = 750
            text3 = u'你的分数为：' + str(price)
            text_surface3 = font2.render(text3, True, (0, 0, 255))
            text_surface2 = font2.render(u'  ', True, (0, 0, 255))
            tru = 1
            pygame.event.get()
    if(diff==2):
        screen = pygame.display.set_mode((1000, 600), 0, 32)
        background = pygame.image.load(background_image_filename).convert()
        ball = pygame.image.load(cannon_image_filename).convert_alpha()
        xlal = pygame.image.load(xlal_image_filename).convert_alpha()
        plane1 = pygame.image.load(plane_image_filename).convert_alpha()
        plane2 = pygame.image.load(plane_image_filename).convert_alpha()
        plane3 = pygame.image.load(plane_image_filename).convert_alpha()
        sita = 45
        v0 = 750
        ball_count = 10
        font = pygame.font.SysFont("arial", 40)
        font2 = pygame.font.SysFont("simsunnsimsun", 40)
        font3 = pygame.font.SysFont("simsunnsimsun", 40)
        font4 = pygame.font.SysFont("simsunnsimsun", 40)
        xt = 500
        yt = 50
        text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
        price = 0
        text3 = u'你的分数为：' + str(price)
        text4 = u'你还有' + str(ball_count) + '发炮弹~，把握机会哦少年'
        text_surface = font.render(text, True, (0, 0, 255))
        text_surface2 = font2.render(u'  ', True, (0, 0, 255))
        text_surface3 = font3.render(text3, True, (0, 0, 255))
        text_surface4 = font4.render(text4, True, (249, 139, 87))
        yp1 = ran.randint(10, 200)
        xp1 = ran.randint(900, 990)
        vp1 = ran.randint(1, 2)
        ip1 = 0
        yp2 = ran.randint(10, 200)
        xp2 = ran.randint(900, 990)
        vp2 = ran.randint(1, 2)
        ip2 = 0
        yp3 = ran.randint(10, 200)
        xp3 = ran.randint(900, 990)
        vp3 = ran.randint(1, 2)
        ip3 = 0
        tru1 = 1
        ball_count = 10
        while (tru1):
            text4 = u'你还有' + str(ball_count) + '发炮弹~，把握机会哦少年'
            text_surface4 = font4.render(text4, True, (249, 139, 87))
            screen.blit(background, (0, 0))
            screen.blit(ball, (75, 482))
            screen.blit(xlal, (7, 482))
            screen.blit(plane1, (xp1, yp1))
            screen.blit(plane2, (xp2, yp2))
            screen.blit(plane3, (xp3, yp3))
            screen.blit(text_surface, (400, 550))
            screen.blit(text_surface2, (300, 510))
            screen.blit(text_surface3, (450, 90))
            screen.blit(text_surface4, (300, 30))
            pygame.display.update()
            tru = 1
            qi=1                            #判定击中后是否减速一波，1为默认，不减速
            while tru:
                while tru:
                    if (ball_count <= 0):
                        pause = 1
                        tru1 = 0
                    ip1 += 1
                    ip2 += 1
                    ip3 += 1
                    text_surface = font.render(text, True, (0, 0, 255))
                    screen.blit(background, (0, 0))
                    screen.blit(ball, (100 - 25, 500 - 18))
                    screen.blit(xlal, (7, 482))
                    # screen.blit(plane, (xp, yp))
                    if ((xp1 - ip1 * vp1) <= 0):
                        yp1 = ran.randint(10, 200)
                        xp1 = ran.randint(900, 990)
                        vp1 = ran.randint(1, 2)
                        ip1 = 0
                    if ((xp2 - ip2 * vp2) <= 0):
                        yp2 = ran.randint(10, 200)
                        xp2 = ran.randint(900, 990)
                        vp2 = ran.randint(1, 2)
                        ip2 = 0
                    if ((xp3 - ip3 * vp3) <= 0):
                        yp3 = ran.randint(10, 200)
                        xp3 = ran.randint(900, 990)
                        vp3 = ran.randint(1, 2)
                        ip3 = 0
                    x, y = pygame.mouse.get_pos()
                    v0 = int(ma.sqrt((482 - y) * (482 - y) + (x - 75) * (x - 75))) * 2.5
                    if (v0 >= 2000):
                        v0 = 2000
                    elif (v0 <= 400):
                        v0 = 400
                    lenth = int(266 * (v0 - 400) / 1600)
                    xx = 75 + 16 + 150 * ma.cos(ma.atan((600 - y) / (x + 1)))
                    yy = 482 + 16 - 150 * ma.sin(ma.atan((600 - y) / (x + 1)))
                    pygame.draw.line(screen, (50, 50, 55), (75 + 16, 482 + 16), (xx, yy), 4)
                    pygame.draw.line(screen, (50, 50, 50), (75 + 16, 482 + 50), (75 + 16 + lenth, 482 + 50), 4)
                    screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                    screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                    screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                    screen.blit(text_surface, (400, 550))
                    screen.blit(text_surface2, (300, 510))
                    screen.blit(text_surface3, (450, 90))
                    screen.blit(text_surface4, (300, 30))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pause = 1
                                tru = 0
                                tru1 = 0
                        else:
                            pass
                        # if event.type != KEYDOWN:
                        #     pass
                        ip1 += 1
                        ip2 += 1
                        ip3 += 1
                        x, y = pygame.mouse.get_pos()
                        xx = 75 + 16 + 150 * ma.cos(ma.atan((600 - y) / (x + 1)))
                        yy = 482 + 16 - 150 * ma.sin(ma.atan((600 - y) / (x + 1)))
                        sita = int(180 * ma.atan((600 - y) / (x + 1)) / ma.pi)
                        v0 = int(ma.sqrt((482 - y) * (482 - y) + (x - 75) * (x - 75))) * 2.5
                        if (v0 >= 2000):
                            v0 = 2000
                        elif (v0 <= 400):
                            v0 = 400
                        lenth = int(266 * (v0 - 400) / 1600)
                        text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
                        text_surface = font.render(text, True, (0, 0, 255))
                        screen.blit(background, (0, 0))
                        screen.blit(ball, (100 - 25, 500 - 18))
                        # screen.blit(plane, (xp, yp))
                        pygame.draw.line(screen, (50, 50, 55), (75 + 16, 482 + 16), (xx, yy), 4)
                        pygame.draw.line(screen, (50, 50, 50), (75 + 16, 482 + 50), (75 + 16 + lenth, 482 + 50), 4)
                        screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                        screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                        screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                        screen.blit(text_surface, (400, 550))
                        screen.blit(text_surface2, (300, 510))
                        screen.blit(text_surface3, (450, 90))
                        screen.blit(text_surface4, (300, 30))
                        pygame.display.update()
                        if event.type == MOUSEBUTTONDOWN:
                            x, y = pygame.mouse.get_pos()
                            sita = int(180 * ma.atan((600 - y) / (x + 1)) / ma.pi)
                            v0 = int(ma.sqrt((482 - y) * (482 - y) + (x - 75) * (x - 75))) * 2.5 + 200
                            text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
                            text_surface = font.render(text, True, (0, 0, 255))
                            screen.blit(background, (0, 0))
                            screen.blit(ball, (100 - 25, 500 - 18))
                            screen.blit(xlal, (7, 482))
                            screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                            screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                            screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                            screen.blit(text_surface, (400, 550))
                            screen.blit(text_surface2, (300, 510))
                            screen.blit(text_surface3, (450, 90))
                            pygame.display.update()
                            if event.type == MOUSEBUTTONDOWN:
                                ball_count -= 1
                                tru = 0
            result = cannon(sita, v0)
            xb = result.get('list_x')
            yb = result.get('list_y')
            i = result.get('maxi')
            p = int(i / 1000)
            x_ = [0]
            y_ = [0]
            q = 0
            q_ = [q]
            q = 1
            while (q <= 999):
                if not tru1:
                    break
                x_.append(int(xb[q * p] / 50))
                y_.append(int(yb[q * p] / 50))
                q_.append(q)
                q += 1
            qq = 0
            while (qq < max(q_)):
                if not tru1:
                    break
                qq += 1
                ip1 += 1
                ip2 += 1
                ip3 += 1
                screen.blit(background, (0, 0))
                screen.blit(ball, (100 + x_[qq] - 25, 500 - y_[qq] - 18))
                text_surface2 = font2.render(u'                   冷却ing', True, (255, 0, 0))
                text_surface3 = font2.render(text3, True, (0, 0, 255))
                screen.blit(text_surface2, (100, 510))
                screen.blit(text_surface3, (300, 90))
                if (ma.sqrt(((100 + x_[qq] - 25) - (xp1 - ip1 * vp1)) * ((100 + x_[qq] - 25) - (xp1 - ip1 * vp1)) + (
                            (500 - y_[qq] - 18) - yp1) * ((500 - y_[qq] - 18) - yp1)) <= 20):
                    yp1 = ran.randint(10, 200)
                    xp1 = ran.randint(900, 990)
                    vp1 = 1
                    vp2 = 1
                    vp3 = 1
                    ip1 = 0
                    qi = 0
                    price += 1
                    screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                    pygame.mixer.music.pause()
                    pygame.mixer.music.set_volume(80 / 100.0)
                    sound2.play()
                    pygame.time.delay(100)
                    pygame.mixer.music.set_volume(10 / 100.0)
                    pygame.mixer.music.unpause()
                    break
                screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                if (ma.sqrt(((100 + x_[qq] - 25) - (xp2 - ip2 * vp2)) * ((100 + x_[qq] - 25) - (xp2 - ip2 * vp2)) + (
                            (500 - y_[qq] - 18) - yp2) * ((500 - y_[qq] - 18) - yp2)) <= 20):
                    yp2 = ran.randint(10, 200)
                    xp2 = ran.randint(900, 990)
                    vp1 = 1
                    vp2 = 1
                    vp3 = 1
                    ip2 = 0
                    qi = 0
                    price += 1
                    screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                    pygame.mixer.music.pause()
                    pygame.mixer.music.set_volume(80 / 100.0)
                    sound2.play()
                    pygame.time.delay(100)
                    pygame.mixer.music.set_volume(10 / 100.0)
                    pygame.mixer.music.unpause()
                    break
                screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                if (ma.sqrt(((100 + x_[qq] - 25) - (xp3 - ip3 * vp3)) * ((100 + x_[qq] - 25) - (xp3 - ip3 * vp3)) + (
                            (500 - y_[qq] - 18) - yp3) * ((500 - y_[qq] - 18) - yp3)) <= 20):
                    yp3 = ran.randint(10, 200)
                    xp3 = ran.randint(900, 990)
                    vp1 = 1
                    vp2 = 1
                    vp3 = 1
                    ip3 = 0
                    qi = 0
                    price += 1
                    screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                    pygame.mixer.music.pause()
                    pygame.mixer.music.set_volume(80 / 100.0)
                    sound2.play()
                    pygame.time.delay(100)
                    pygame.mixer.music.set_volume(10 / 100.0)
                    pygame.mixer.music.unpause()
                    break
                screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                if(qi==1):
                    if ((xp1 - ip1 * vp1) <= 0):
                        yp1 = ran.randint(10, 300)
                        xp1 = ran.randint(900, 990)
                        vp1 = ran.randint(1, 2)
                        ip1 = 0
                    if ((xp2 - ip2 * vp2) <= 0):
                        yp2 = ran.randint(10, 300)
                        xp2 = ran.randint(900, 990)
                        vp2 = ran.randint(1, 2)
                        ip2 = 0
                    if ((xp3 - ip3 * vp3) <= 0):
                        yp3 = ran.randint(10, 300)
                        xp3 = ran.randint(900, 990)
                        vp3 = ran.randint(1, 2)
                        ip3 = 0
                elif(qi==0):
                    if ((xp1 - ip1 * vp1) <= 0):
                        yp1 = ran.randint(10, 300)
                        xp1 = ran.randint(900, 990)
                        vp1 = ran.randint(1, 1)
                        ip1 = 0
                        qi = 1
                    if ((xp2 - ip2 * vp2) <= 0):
                        yp2 = ran.randint(10, 300)
                        xp2 = ran.randint(900, 990)
                        vp2 = ran.randint(1, 1)
                        ip2 = 0
                        qi = 1
                    if ((xp3 - ip3 * vp3) <= 0):
                        yp3 = ran.randint(10, 300)
                        xp3 = ran.randint(900, 990)
                        vp3 = ran.randint(1, 1)
                        ip3 = 0
                        qi = 1
                else:pass
                # 在新的位置上画图
                pygame.display.update()
                x, y = 100, 100
                sita = 45
                v0 = 750
            text3 = u'你的分数为：' + str(price)
            text_surface3 = font2.render(text3, True, (0, 0, 255))
            text_surface2 = font2.render(u'  ', True, (0, 0, 255))
            tru = 1
            pygame.event.get()
    if(diff==3):
        screen = pygame.display.set_mode((1000, 600), 0, 32)
        background = pygame.image.load(background_image_filename).convert()
        ball = pygame.image.load(cannon_image_filename).convert_alpha()
        xlal = pygame.image.load(xlal_image_filename).convert_alpha()
        plane1 = pygame.image.load(plane_image_filename).convert_alpha()
        plane2 = pygame.image.load(plane_image_filename).convert_alpha()
        plane3 = pygame.image.load(plane_image_filename).convert_alpha()
        sita = 45
        v0 = 750
        ball_count = 10
        font = pygame.font.SysFont("arial", 40)
        font2 = pygame.font.SysFont("simsunnsimsun", 40)
        font3 = pygame.font.SysFont("simsunnsimsun", 40)
        font4 = pygame.font.SysFont("simsunnsimsun", 40)
        xt = 500
        yt = 50
        text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
        price = 0
        text3 = u'你的分数为：' + str(price)
        text4 = u'你还有' + str(ball_count) + '发炮弹~，把握机会哦少年'
        text_surface = font.render(text, True, (0, 0, 255))
        text_surface2 = font2.render(u'  ', True, (0, 0, 255))
        text_surface3 = font3.render(text3, True, (0, 0, 255))
        text_surface4 = font4.render(text4, True, (249, 139, 87))
        yp1 = ran.randint(10, 200)
        xp1 = ran.randint(900, 990)
        vp1 = ran.randint(1, 2)
        ip1 = 0
        yp2 = ran.randint(10, 200)
        xp2 = ran.randint(900, 990)
        vp2 = ran.randint(1, 2)
        ip2 = 0
        yp3 = ran.randint(10, 200)
        xp3 = ran.randint(900, 990)
        vp3 = ran.randint(1,2)
        ip3 = 0
        tru1 = 1
        ball_count = 10
        while (tru1):
            text4 = u'你还有' + str(ball_count) + '发炮弹~，把握机会哦少年'
            text_surface4 = font4.render(text4, True, (249, 139, 87))
            screen.blit(background, (0, 0))
            screen.blit(ball, (75, 482))
            screen.blit(xlal, (7, 482))
            screen.blit(plane1, (xp1, yp1))
            screen.blit(plane2, (xp2, yp2))
            screen.blit(plane3, (xp3, yp3))
            screen.blit(text_surface, (400, 550))
            screen.blit(text_surface2, (300, 510))
            screen.blit(text_surface3, (450, 90))
            screen.blit(text_surface4, (300, 30))
            pygame.display.update()
            tru = 1
            while tru:
                while tru:
                    if (ball_count <= 0):
                        pause = 1
                        tru1 = 0
                    ip1 += 1
                    ip2 += 1
                    ip3 += 1
                    text_surface = font.render(text, True, (0, 0, 255))
                    screen.blit(background, (0, 0))
                    screen.blit(ball, (100 - 25, 500 - 18))
                    screen.blit(xlal, (7, 482))
                    # screen.blit(plane, (xp, yp))
                    if ((xp1 - ip1 * vp1) <= 0):
                        yp1 = ran.randint(10, 200)
                        xp1 = ran.randint(900, 990)
                        vp1 = ran.randint(1,2)
                        ip1 = 0
                    if ((xp2 - ip2 * vp2) <= 0):
                        yp2 = ran.randint(10, 200)
                        xp2 = ran.randint(900, 990)
                        vp2 = ran.randint(1,2)
                        ip2 = 0
                    if ((xp3 - ip3 * vp3) <= 0):
                        yp3 = ran.randint(10, 200)
                        xp3 = ran.randint(900, 990)
                        vp3 = ran.randint(1,2)
                        ip3 = 0
                    x, y = pygame.mouse.get_pos()
                    v0 = int(ma.sqrt((482 - y) * (482 - y) + (x - 75) * (x - 75))) * 2.5
                    if (v0 >= 2000):
                        v0 = 2000
                    elif (v0 <= 400):
                        v0 = 400
                    lenth = int(266 * (v0 - 400) / 1600)
                    xx = 75 + 16 + 150 * ma.cos(ma.atan((600 - y) / (x + 1)))
                    yy = 482 + 16 - 150 * ma.sin(ma.atan((600 - y) / (x + 1)))
                    pygame.draw.line(screen, (50, 50, 55), (75 + 16, 482 + 16), (xx, yy), 4)
                    pygame.draw.line(screen, (50, 50, 50), (75 + 16, 482 + 50), (75 + 16 + lenth, 482 + 50), 4)
                    screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                    screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                    screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                    screen.blit(text_surface, (400, 550))
                    screen.blit(text_surface2, (300, 510))
                    screen.blit(text_surface3, (450, 90))
                    screen.blit(text_surface4, (300, 30))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pause = 1
                                tru = 0
                                tru1 = 0
                        else:
                            pass
                        # if event.type != KEYDOWN:
                        #     pass
                        ip1 += 1
                        ip2 += 1
                        ip3 += 1
                        x, y = pygame.mouse.get_pos()
                        xx = 75 + 16 + 150 * ma.cos(ma.atan((600 - y) / (x + 1)))
                        yy = 482 + 16 - 150 * ma.sin(ma.atan((600 - y) / (x + 1)))
                        sita = int(180 * ma.atan((600 - y) / (x + 1)) / ma.pi)
                        v0 = int(ma.sqrt((482 - y) * (482 - y) + (x - 75) * (x - 75))) * 2.5
                        if (v0 >= 2000):
                            v0 = 2000
                        elif (v0 <= 400):
                            v0 = 400
                        lenth = int(266 * (v0 - 400) / 1600)
                        text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
                        text_surface = font.render(text, True, (0, 0, 255))
                        screen.blit(background, (0, 0))
                        screen.blit(ball, (100 - 25, 500 - 18))
                        # screen.blit(plane, (xp, yp))
                        pygame.draw.line(screen, (50, 50, 55), (75 + 16, 482 + 16), (xx, yy), 4)
                        pygame.draw.line(screen, (50, 50, 50), (75 + 16, 482 + 50), (75 + 16 + lenth, 482 + 50), 4)
                        screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                        screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                        screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                        screen.blit(text_surface, (400, 550))
                        screen.blit(text_surface2, (300, 510))
                        screen.blit(text_surface3, (450, 90))
                        screen.blit(text_surface4, (300, 30))
                        pygame.display.update()
                        if event.type == MOUSEBUTTONDOWN:
                            x, y = pygame.mouse.get_pos()
                            sita = int(180 * ma.atan((600 - y) / (x + 1)) / ma.pi)
                            v0 = int(ma.sqrt((482 - y) * (482 - y) + (x - 75) * (x - 75))) * 2.5 + 200
                            text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
                            text_surface = font.render(text, True, (0, 0, 255))
                            screen.blit(background, (0, 0))
                            screen.blit(ball, (100 - 25, 500 - 18))
                            screen.blit(xlal, (7, 482))
                            screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                            screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                            screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                            screen.blit(text_surface, (400, 550))
                            screen.blit(text_surface2, (300, 510))
                            screen.blit(text_surface3, (450, 90))
                            pygame.display.update()
                            if event.type == MOUSEBUTTONDOWN:
                                ball_count -= 1
                                tru = 0
            result = cannon(sita, v0)
            xb = result.get('list_x')
            yb = result.get('list_y')
            i = result.get('maxi')
            p = int(i / 1000)
            x_ = [0]
            y_ = [0]
            q = 0
            q_ = [q]
            q = 1
            while (q <= 999):
                if not tru1:
                    break
                x_.append(int(xb[q * p] / 50))
                y_.append(int(yb[q * p] / 50))
                q_.append(q)
                q += 1
            qq = 0
            while (qq < max(q_)):
                if not tru1:
                    break
                qq += 1
                ip1 += 1
                ip2 += 1
                ip3 += 1
                screen.blit(background, (0, 0))
                screen.blit(ball, (100 + x_[qq] - 25, 500 - y_[qq] - 18))
                text_surface2 = font2.render(u'                   冷却ing', True, (255, 0, 0))
                text_surface3 = font2.render(text3, True, (0, 0, 255))
                screen.blit(text_surface2, (100, 510))
                screen.blit(text_surface3, (300, 90))
                if (ma.sqrt(((100 + x_[qq] - 25) - (xp1 - ip1 * vp1)) * ((100 + x_[qq] - 25) - (xp1 - ip1 * vp1)) + (
                            (500 - y_[qq] - 18) - yp1) * ((500 - y_[qq] - 18) - yp1)) <= 20):
                    yp1 = ran.randint(10, 200)
                    xp1 = ran.randint(900, 990)
                    vp1 = ran.randint(1,2)
                    ip1 = 0
                    price += 1
                    screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                    pygame.mixer.music.pause()
                    pygame.mixer.music.set_volume(80 / 100.0)
                    sound2.play()
                    pygame.time.delay(100)
                    pygame.mixer.music.set_volume(10 / 100.0)
                    pygame.mixer.music.unpause()
                    break
                screen.blit(plane1, (xp1 - ip1 * vp1, yp1))
                if (ma.sqrt(((100 + x_[qq] - 25) - (xp2 - ip2 * vp2)) * ((100 + x_[qq] - 25) - (xp2 - ip2 * vp2)) + (
                            (500 - y_[qq] - 18) - yp2) * ((500 - y_[qq] - 18) - yp2)) <= 20):
                    yp2 = ran.randint(10, 200)
                    xp2 = ran.randint(900, 990)
                    vp2 = ran.randint(1,2)
                    ip2 = 0
                    price += 1
                    screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                    pygame.mixer.music.pause()
                    pygame.mixer.music.set_volume(80 / 100.0)
                    sound2.play()
                    pygame.time.delay(100)
                    pygame.mixer.music.set_volume(10 / 100.0)
                    pygame.mixer.music.unpause()
                    break
                screen.blit(plane2, (xp2 - ip2 * vp2, yp2))
                if (ma.sqrt(((100 + x_[qq] - 25) - (xp3 - ip3 * vp3)) * ((100 + x_[qq] - 25) - (xp3 - ip3 * vp3)) + (
                            (500 - y_[qq] - 18) - yp3) * ((500 - y_[qq] - 18) - yp3)) <= 20):
                    yp3 = ran.randint(10, 200)
                    xp3 = ran.randint(900, 990)
                    vp3 = ran.randint(1,2)
                    ip3 = 0
                    price += 1
                    screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                    pygame.mixer.music.pause()
                    pygame.mixer.music.set_volume(80 / 100.0)
                    sound2.play()
                    pygame.time.delay(100)
                    pygame.mixer.music.set_volume(10 / 100.0)
                    pygame.mixer.music.unpause()
                    break
                screen.blit(plane3, (xp3 - ip3 * vp3, yp3))
                if ((xp1 - ip1 * vp1) <= 0):
                    yp1 = ran.randint(10, 300)
                    xp1 = ran.randint(900, 990)
                    vp1 = ran.randint(1, 2)
                    ip1 = 0
                if ((xp2 - ip2 * vp2) <= 0):
                    yp2 = ran.randint(10, 300)
                    xp2 = ran.randint(900, 990)
                    vp2 = ran.randint(1, 2)
                    ip2 = 0
                if ((xp3 - ip3 * vp3) <= 0):
                    yp3 = ran.randint(10, 300)
                    xp3 = ran.randint(900, 990)
                    vp3 = ran.randint(1, 2)
                    ip3 = 0
                # 在新的位置上画图
                pygame.display.update()
                x, y = 100, 100
                sita = 45
                v0 = 750
            text3 = u'你的分数为：' + str(price)
            text_surface3 = font2.render(text3, True, (0, 0, 255))
            text_surface2 = font2.render(u'  ', True, (0, 0, 255))
            tru = 1
            pygame.event.get()
    else:pass








'''

    x, y = pygame.mouse.get_pos()
    sita = int(180 * ma.atan((600 - y) / (x + 1)) / ma.pi)
    v0 = int(ma.sqrt((482 - y) * (482 - y) + (x - 75) * (x - 75))) * 2.5
    text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
    text_surface = font.render(text, True, (0, 0, 255))
    screen.blit(background, (0, 0))
    screen.blit(ball, (100 - 25, 500 - 18))
    screen.blit(plane, (xp, yp))
    screen.blit(text_surface, (500, 50))
    screen.blit(text_surface2, (100, 10))
    pygame.display.update()
    if event.type == MOUSEBUTTONDOWN:
        tru = 0

'''

'''
                if event.type == KEYDOWN:
                    if  event.key != K_1:
                            if event.key == K_UP:
                                sita = sita + 1
                                if sita >= 90:
                                    sita =0
                                else:
                                    pass
                            elif event.key ==\
                                    K_DOWN:
                                sita = sita - 1
                                if sita <= 0:
                                    sita = 90
                                else:
                                    pass
                            elif event.key == K_LEFT:
                                v0 = v0 - 1
                                if v0 == 500:
                                    v0 = 1000
                                else:
                                    pass
                            elif event.key == K_RIGHT:
                                v0 = v0 + 1
                                if v0 == 1000:
                                    v0 = 500
                                else:
                                    pass
                            else:
                                pass
                            x, y = pygame.mouse.get_pos()
                            sita=int(180*ma.atan((600-y)/(x))/ma.pi)
                            text = 'sita= ' + str(sita) + ' ' + 'V0= ' + str(v0) + ' '
                            text_surface = font.render(text, True, (0, 0, 255))
                            screen.blit(background, (0, 0))
                            screen.blit(ball, (100 - 25, 500 - 18))
                            screen.blit(text_surface, (500, 50))
                            screen.blit(text_surface2, (100, 10))
                            pygame.display.update()
                    else:
                        tru=0
'''
