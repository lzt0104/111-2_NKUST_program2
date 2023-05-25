import numpy as np


#建立一維陣列的方法
A = np.array([1,6,8,3,9])
print(A)

#建立都是0的陣列
B = np.zeros(10)  #
print(B)

#建立都是1的陣列
D=np.ones(50)
print(D)

#建立長度為N的陣列
E=np.empty(5)
print(E)

#建立一個範圍內的陣列
F = np.arange(start=1,stop=12,step=2,dtype=int)
print(F)

G= np.arange(10)
print(G)

#建立一個範圍內的陣列(小數)
H = np.linspace(0,2,9)
print(H)

#陣列的資訊
I = np.array([1,5,7,9,33,88,99])
print("維度",I.ndim)
print("個數",I.size)
print("形狀",I.shape)
print("類別",I.dtype)
print("陣列大小",I.itemsize) #以Byte位元組為單位