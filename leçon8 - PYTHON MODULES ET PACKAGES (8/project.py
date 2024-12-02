def quadrado(x):
    return x **2

def soma(x,y):
    return x + y

def fibonacci(n):
    fb = []
    a = 0
    b = 1
    while a < n:
        a, b = b, a+b
        fb.append(a)
    return fb


if __name__ == "__main__":
    print("Err")
    print(fibonacci(34))
    print(dir(__name__))
