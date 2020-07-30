try:
    x_coord = int(input('Current x: '))
    y_coord = int(input('Current y: '))
    x1_coord = int(input('x1: '))
    y1_coord = int(input('y1: '))
except Exception:
    print('INVALID INPUT')

if 1 <= x_coord <= 8 and 1 <= y_coord <= 8 and 1 <= x1_coord <= 8  and 1 <= y1_coord <= 8:
    if abs(x_coord - x1_coord) == abs(y_coord - y1_coord):
        print('YES')
    else:
        print('NO')
