stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

name = ''
max_sales = 0

for key, value in stats.items():
    if name == '':
        name = key
    if value > max_sales:
        max_sales = value
        name = key
print(name)
