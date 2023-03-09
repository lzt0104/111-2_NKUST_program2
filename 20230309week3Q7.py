"""
1.在宣告時便需要指定一個BoundedStack堆疊的大小。
2.BoundedStack有三個方法：
1.push (存入堆疊資料)
2.pop (從堆疊中取出資料)
3.測試一個BoundedStack實例是否為空的empty 方法(Boolean 值)。
3.在push 方法中，若判斷已超出堆疊最大容量，則顯示”stack-overflow”。
4.在pop 方法中，若堆疊區為空值，則顯示”stack-is-empty”。
5.在測試是否為空值的方法，若為空值，請傳回”true”，否則傳回”false”。
"""
class BoundedStack:

    def __init__(self,size):
        self.limit = size
        self.mystack =[]
    
    def getPush(self,text):
        if (len(self.mystack) <= self.limit):
            self.mystack.append(text)
        else:
            print("Stack-overflow")

    
    def getPop(self):
        if (len(self.mystack) != 0):
            print(self.mystack.pop())
        else:
            print("stack-is-empty")

    def isEmpty(self):
        if (len(self.mystack)==0):
            print("Stack is Empty.")

s0 = BoundedStack(5)
s0.isEmpty()
s0.getPush(6)
s0.getPop()
s0.getPush("123")
s0.getPush("456")
s0.getPush("123")
s0.getPush("456")
s0.getPush("456")
print(s0.mystack)