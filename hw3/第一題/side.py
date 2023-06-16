#定義函數
def check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "fit"
    else:
        return "unfit"

#使用者輸入值
input_str = input("請輸入三個數值（以空白隔開）：")
sides = input_str.split()
a = int(sides[0])
b = int(sides[1])
c = int(sides[2])

result = check(a, b, c)

print(a,b,c,"是否可構成三角形：",result)
