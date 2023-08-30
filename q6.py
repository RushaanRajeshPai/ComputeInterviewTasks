cube = lambda x: x*x*x

def fibonacci(n):
    res = []
    for n in range(0,n):
        if n < 2:
            res.append(n)
        else:
            res.append(res[(n-2)] + res[(n - 1)])
    return res

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))