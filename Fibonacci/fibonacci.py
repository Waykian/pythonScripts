#Fibonacci series up to n
def fib(n: int):
    a = 0
    b = 1
    while(a < n):
        print(a)
        a, b = b, a + b

# Array of Fibonacci numbers up to n
def fibArray(n: int):
    result = []
    a = 0
    b = 1
    while(a < n):
        result.append(a)
        a, b = b, a + b
    return result