a=open("C:/Users/Administrator/Desktop/name.txt")
i=15
p=len('name')
while p:
    c = a.readlines(1)
    c = ''.join(c).strip('\n')
    print(c)
    p=len(c)
a.close()
