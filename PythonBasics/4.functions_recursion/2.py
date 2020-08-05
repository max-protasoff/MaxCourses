try:
    pos = int(input("Enter n-th Fibonacci number: "))
except exception:
    print("Invalid input")

def fibo(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

print(fibo(pos))
