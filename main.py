# h = x * y
# h有很多筆。1 2 3 4 5 6 7 8 代表 1 2 3 4 是x的，5 6 7 8是y的
import numpy as np
import time

f = open("array_data.txt",'r',encoding="utf-8")
flist = f.readlines()
flist = flist[0].split(" ")
flist = list(map(float,flist))

x,y = [],[]

for i in range(0,len(flist)-4,8):
    for j in range(4):
        x.append(flist[i + j])
        y.append(flist[i +(j+4)])

h = []
j = 0
before = time.time()
for j in range(len(x)):
    h.append(x[j]*y[j])
#print(h)
after = time.time()

print(f"Execution time:{after-before}")


i = 0
h = []

x = np.array(x)
y = np.array(y)
before = time.time()
h.append(x*y)
after = time.time()
print(after-before)
