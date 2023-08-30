import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    nparray=numpy.array(arr,float)
    return nparray

arr = input().strip().split(' ')
result = arrays(arr)
print(result)