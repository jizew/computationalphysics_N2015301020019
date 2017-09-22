#encoding=UTF-8
import os
import time
import random
list=[[' ' for i in range(150)] for i in range(50)]
t1=random.randint(-24,24)
t2=random.randint(-73,73)
while 1:
    x = 25+t1
    y = 75+t2
    list[x][y]='宠'
    list[x][y-1]='王'
    list[x][y+1]='霖'
    for i in range(50):
        for j in range(150):
            print(list[i][j],end='')
        print()
    list = [[' ' for i in range(150)] for i in range(50)]
    t1 = random.randint(-24, 24)
    t2 = random.randint(-73, 73)
    time.sleep(0.2)
    os.system('cls')
