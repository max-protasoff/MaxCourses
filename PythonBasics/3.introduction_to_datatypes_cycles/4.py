ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique = list()
for key, value in ids.items():
    for id in value:
        if id not in unique:
            unique.append(id)

print(unique)

# Подскажи пж более нормальный вариант, если он возможен, думаю, этот не очень эффективный
