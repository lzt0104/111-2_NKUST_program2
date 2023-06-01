#一維

import numpy as np

U = np.array([1,2,3])
V = np.array([1,0,1])
print(np.dot(U,V))  #內積
print(np.cross(U,V))  #外積

X = np.array([2,3,54])
Y = np.array([123,123,522])
print(np.dot(X,Y))
print(np.cross(X,Y))
print(X+Y)
print(X-Y)
print(X*Y)
print(X/Y)

#二維

grades = np.array([[95,100,100],[86,90,75],[98,98,96],[78,90,80],[70,68,72]])

print(grades)
print(grades[1,2]) 

A = np.arange(15)
print(A)
B = A.reshape(3,5) #更改陣列形狀
print(B)

C = np.arange(15).reshape(3,5)
print(C)
C.ndim
C.shape
C.size
C.dtype
C.itemsize


#陣列運算
A = np.ones(16).reshape(4,4) #ones建立都是1的一維陣列，運用reshape轉成4*4的二維陣列
print(A)
print(A*3)
A[1,0]=10
print(A)
A[3,3]=9
print(A)

print(A.ravel()) #轉換為一維陣列

print(A.reshape(2,2,4)) #轉換為三維陣列


A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)
B = np.transpose(A) #轉至
print(B)

#請建立一個二維陣列如下，並將該矩陣與該陣列的轉置陣列相加。

A = np.array([[2,4,6,8],[10,12,14,16],[18,20,22,24],[26,28,30,32]])
B = np.transpose(A)
print(A+B)
print(A*B)


#計算角度
TA = np.array([0,30,45])
TB = TA* np.pi / 180
TC = np.sin(TB)
print(TC)

#取亂數

A = np.random.randint(1,6,3)
print(A)
AC = np.random.randint(1,100,20)
print(AC)
