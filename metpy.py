import random 
import Matrix 

# array generation using by random number
def randn(row = 3, columns = 3):
        result = []
        for i in range(0, row):
            lst = []
            for j in range(0, columns):
                lst.append(1/random.randint(3, 20))
            result.append(lst)
        return Matrix.Matrix(result)

# creation of array.
def array(arr = []):
    return Matrix.Matrix(arr)


if __name__ == '__main__':
    obj = array()
    print(obj)