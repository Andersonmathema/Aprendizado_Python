def Fibonacci(n):
    if n < 2:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

x = int(input("Digite um número: "))
print(Fibonacci(x))
