# -*- coding:utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
# 定义衰变函数
def decay_eq(na, nb, t, dn):   # na,nb为粒子数，t为dt与\tau的比值 dn为允许的误差
    na_0 = na
    nb_0 = nb
    c0 = na + nb                        #用初值确定常数
    c1 = na - nb
    na_t = [na_0]                       #构建数值解NA的列表
    nb_t = [nb_0]                       #构建数值解NB的列表
    real_nb = [nb_0]                    #构建理论解的列表
    dna = (nb - na) * t
    dnb = (na - nb) * t
    t_list = [0]
    i = 0
    while (abs(na - nb) >= 1e-9):     #定义平衡状态
        i += 1
        na = na + dna
        nb = nb + dnb
        na_t.append(na)           #将新的步长后的粒子数写在列表中
        nb_t.append(nb)
        t_list.append(i * t)
        dna = (nb - na) * t
        dnb = (na - nb) * t
        realnb = 0.5 * c0 - 0.5 * c1 * math.exp(-2 * i * t)    #理论计算值
        real_nb.append(realnb)
        if (abs(realnb - nb) > dn):
            break
    result = {'list_real_nb': real_nb, 'list_na': na_t, 'list_nb': nb_t, 'list_t': t_list, 'total': [na, nb, t * i],
              'rna': na, 'rnb': nb}                  #传递参数
    return (result)
def show_():
    print('请顺序输入初始时NA,NB的粒子数,以回车间隔两粒子数\n')
    na=float(input())
    nb=float(input())
    print('请输入 时间步长：衰变时间常数T 的值，以回车结束输入\n')
    t=float(input())
    print('请输入 判定数值模拟失效的误差阈值，以回车结束输入\n')
    dn=float(input())
    result=decay_eq(na,nb,t,dn)
    x=result.get('list_t')
    y1=result.get('list_na')
    y2=result.get('list_nb')
    y3 = result.get('list_real_nb')
    plt.plot(x,y1,label = 'number of NA')
    plt.plot(x,y2,label = 'numner of NB')
    plt.plot(x, y3, label='numner of real_NB')
    plt.legend(loc='best')
    plt.xlabel('dt:tau')
    plt.ylabel('numbers of NA/NB')
    obj = result.get('total')
    print('平衡时间：', obj[2], '剩余NA:', obj[0], '剩余NB:', obj[1])
    plt.show()

