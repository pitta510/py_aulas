import math

def calcula(v, x):
    r = 0
    
    for i in range(len(v)):
        r += v[i] * math.pow(x, i)

    return r

def deriva(v):
    d = [0 for i in range(len(v))]
    for i in range(len(v)-1, 0, -1):
        d[i-1] = v[i] * i

    return d

if __name__ == "__main__":
    v1 = [2, 0, 0, 0, 0, 18, 0]
    v2 = [-7, 2, 0, 0, 0, 0, 3]

    print(calcula(v1, 1))

    print(deriva(v2))