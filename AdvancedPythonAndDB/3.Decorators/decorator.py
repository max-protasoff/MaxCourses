import datetime

def logger(func):
    def wrapper(args_for_func):
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write('Function called: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
        func(args_for_func)
    return wrapper


@logger
def print_hello(word):
    print('hello ' + word)


print_hello(input('Enter your name: '))
