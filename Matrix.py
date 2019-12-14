# class Matrix the Bulding Block of metpy -- : Matrix Python 
# version :  1.0.0

"""
    matrix : stores the matrix.
    shape : store a tuple contain the dimension of the matrix.
"""
import random 


class Matrix:

    def __init__(self, lst):
        if lst == []:
            self.matrix = lst 
            self.shape = (0, 0)
        else:
            self.matrix = lst
            for sub_array in lst:
                if(len(sub_array) != len(self.matrix[0])):
                    raise TypeError("|| GIVEN MATRIX DEOS NOT FOLLOW THE RULES FOR THE MATRIX ||")                             
            self.shape = (len(self.matrix), len(self.matrix[0]))
    
    # to get the transpoce of the matrix.
    def getT(self):
        result = []
        for  i in range(0, self.shape[1]):
            lst = []
            for j in range(0, self.shape[0]):
                data = 0
                lst.append(data)
            result.append(lst)
        print(result)

        for i in range(0, self.shape[0]):
            for j in range(0, self.shape[1]):
               result[j][i] = self.matrix[i][j]
        return Matrix(result)    

    # for matrix multiplication.
    def __mul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Matrix Multplication is not fesible")
        else: 
            result = []
            lst = []
            for i in range(0, self.shape[0]):
                lst = []
                for j in range(0, other.shape[1]):
                    data = 0
                    for k in range(0, self.shape[1]):
                        data += self.matrix[i][k] * other.matrix[k][j]
                    lst.append(data) 
                result.append(lst)
            return Matrix(result)

    # matrix addition
    def __add__(self, other):
        if self.shape == other.shape:
            result = []
            for i in range(0, self.shape[0]):
                lst = []
                data = 0
                for j in range(0, self.shape[1]):
                    data =  self.matrix[i][j] + other.matrix[i][j]
                    lst.append(data)
                    data = 0
                result.append(lst)
            return Matrix(result)
        else:
            raise TypeError("Matrix addition is no feasible")

    # matrix substraction.
    def __sub__(self, other):
        if self.shape == other.shape:
            result = []
            for i in range(0, self.shape[0]):
                lst = []
                data = 0
                for j in range(0, self.shape[1]):
                    data =  self.matrix[i][j] - other.matrix[i][j]
                    lst.append(data)
                    data = 0
                result.append(lst)
            return Matrix(result)
        else:
            raise TypeError("Matrix addition is no feasible")

    # the print() function for the Matrix class.
    def __str__(self):
        string_to_result = "["
        for row in self.matrix:
            string_to_result += str(row) + "," 
        string_to_result += "]"
        return string_to_result

    

if __name__ == '__main__':
    obj = Matrix([[1,0,0],[0,1,0],[0,0,1]])
    obj1 = Matrix([[1,1,0],[0,1,1],[1,0,1]])
    print(obj1)
