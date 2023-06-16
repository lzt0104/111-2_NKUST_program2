import numpy as np

def add_arrays(A, B):
    result = np.add(A, B)
    return result

# 讀取使用者輸入的第一個3x3陣列
A = []
print("請輸入第一個3x3陣列：")
for _ in range(3):
    row = list(map(int, input().split()))
    A.append(row)

# 讀取使用者輸入的第二個3x3陣列
B = []
print("請輸入第二個3x3陣列：")
for _ in range(3):
    row = list(map(int, input().split()))
    B.append(row)

# 呼叫函式進行陣列相加運算
result = add_arrays(A, B)

# 顯示結果
print("輸出結果：")
for row in result:
    print(" ".join(map(str, row)))
