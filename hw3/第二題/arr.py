arr1 = input("請輸入第一個陣列（6個數字，以空白隔開）：").split()
arr2 = input("請輸入第二個陣列（6個數字，以空白隔開）：").split()

# 創建一個空的結果陣列
result = []

# 迭代 arr1 的每個元素的索引
for i in range(len(arr1)):
    # 將 arr1[i] 與 arr2[i] 轉換為整數，並計算它們的總和
    sum = int(arr1[i]) + int(arr2[i])

    # 檢查總和是否為偶數
    if sum % 2 == 0:
        # 如果是偶數，將 '0' 加入結果陣列
        result.append('0')
    else:
        # 如果是奇數，將 '1' 加入結果陣列
        result.append('1')

# 將結果陣列中的元素用空格連接成字串
output_str = ' '.join(result)

# 輸出結果字串
print(output_str)
