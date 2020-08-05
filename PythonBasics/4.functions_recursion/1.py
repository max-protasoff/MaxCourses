print('=====Factorial=====')


try:
    num = int(input("Enter integer: "))
except Exception:
    print("Invalid input")

'''without recursion'''
#def fact(n):
#    final_num = 1
#    for i in range(1, n + 1):
#        final_num *= i
#    return final_num
#print(fact(num))

'''with recursion'''
def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)
print(fact(num))
