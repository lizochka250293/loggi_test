import datetime

def logger(func):
    def inner(*args, **kwargs):
        s = datetime.datetime.now()
        print(s)
        print(func.__name__)
        print(args)
        print(kwargs)
        func(*args, **kwargs)

    return inner


@logger
def suma(a, b):
    if a > 0 and b > 0:
        return a + b

    elif a < 0 and b < 0:
        return a - b

    else:
        return 0


suma(3, 5)
suma(a=4, b=5)
