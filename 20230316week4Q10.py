class Matrix:
    def __init__(self,row,columns):
        self.__row = row
        self.__columns = columns
        self.__arr=[[0 for i in range(self.__columns)] for j in range(self.__row)] #初始值為0
    
    def getRow(self):
        return self.__row
    
    def getColumns(self):
        return self.__columns
    
    def setElement(self,row,columns,value):
        self.__arr[row][columns] = value

    def getElement(self,row,columns):
        return self.__arr[row][columns]

    def add(self, other):
        if ((self.__columns == other.getcolumns()) and (self.__row==other.getRow())):
            print("add")
        else:
            print("Matrices cannot be added")
matrix1=Matrix(3, 3)
# print(matrix1.getRow())
# print(matrix1.getColumns())
# matrix1.setElement(1, 1,4)
# print(matrix1.getElement(1, 1))
matrix2=Matrix(4, 4)