# h = x * y
import numpy as np
import time

f = open("array_data.txt",'r',encoding="utf-8")
# TODO: 資料以八筆為單位。1 2 3 4 5 6 7 8 代表 1 2 3 4 是x的，5 6 7 8是y的. 但前提是要先讀出來到flist
flist = 0 # 這是讀出來的資料。要修改並刪減
x,y = [],[]

for i in range(len(flist)-4): #想想為什麼是len(flist)-4。也可以用自己的寫法
    # TODO: 把屬於x和屬於y的分別加進x和y
    pass #寫完把這行刪掉

h = []

before = 0 # TODO: 用time模組取得“精確時間”
for j in range(len(x)):
    h.append(x[j]*y[j])
after = 0 # TODO: 用time模組取得“精確時間”

print(f"Execution time:{after - before}")

#變數重置
i = 0
h = []

# TODO: 把 h = x * y 用numpy重做一遍。只有相乘的部分要計時。Hint: numpy可以直接用矩陣“元素相乘”