boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    boys.sort()
    girls.sort()
    print('Dream couples')
    for boy, girl in zip(boys, girls):
        print(boy, 'and', girl)
else:
    print('Boys and girls number mismatch')
