
n = int(input('Enter n: '))
m = int(input('Enter m: '))
k = int(input('Enter k: '))

if k < n * m and (k % n == 0 or k % m == 0):
    print('True')
else:
    print('False')
