# Mathematical function for the metpy : python library for the matrix manuplation 

def factorial(x):
    if x == 0:
        return 1 
    else:
        return x * factorial(x-1)

def exp(x):
    result_value = 0
    for i in range(0,200):
        result_value += x**i / factorial(i)
    return result_value 

def log(x):
    if x <= 0:
        raise ValueError("Out of the domain of logarithmic function")
    else:
        result_value = 0
        for i in range(1,x + 1):
            result_value += 1/i 
        return result_value
 

if __name__ == '__main__':
    val = log(1)
    print(val)
