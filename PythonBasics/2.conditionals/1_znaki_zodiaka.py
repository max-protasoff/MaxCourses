print('Знаки зодиака')

try:
    month = input('Введите месяц')
    day = int(input('Введите число'))
    if day <= 31:
        if month.lower() == 'январь':
            if day <= 20:
                print('Козерог')
            elif day >= 21:
                print('Водолей')
        elif month.lower() == 'февраль':
            if day <= 18:
                print('Водолей')
            elif day >= 19:
                print('Рыбы')
        elif month.lower() == 'март':
            if day <= 20:
                print('Рыбы')
            elif day >= 21:
                print('Овен')
        elif month.lower() == 'апрель':
            if day <= 20:
                print('Овен')
            elif day >= 21:
                print('Телец')
        elif month.lower() == 'май':
            if day <= 21:
                print('Телец')
            elif day >= 22:
                print('Близнецы')
        elif month.lower() == 'июнь':
            if day <= 21:
                print('Близнецы')
            elif day >= 22:
                print('Рак')
        elif month.lower() == 'июль':
            if day <= 22:
                print('Рак')
            elif day >= 23:
                print('Лев')
        elif month.lower() == 'август':
            if day <= 23:
                print('Лев')
            elif day >= 24:
                print('Дева')
        elif month.lower() == 'сентябрь':
            if day <= 23:
                print('Дева')
            elif day >= 24:
                print('Весы')
        elif month.lower() == 'октябрь':
            if day <= 23:
                print('Весы')
            elif day >= 24:
                print('Скорпион')
        elif month.lower() == 'ноябрь':
            if day <= 22:
                print('Скорпион')
            elif day >= 23:
                print('Стрелец')
        elif month.lower() == 'декабрь':
            if day <= 21:
                print('Стрелец')
            elif day >= 22:
                print('Козерог')

except Exception:
    print('Month must be text and day must be an integer')
