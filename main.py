import datetime
def logger(func):
    def arguments(*args, **kwargs):
        s = datetime.now()

        print(s, func._name_)
    return func(*args, **kwargs)
@ logger
def suma(a, b):
    if a>0 and b >0:
        return a+b
    elif a<0 and b<0:
        return a-b
    else:
        return 0

a = 3
b = 7
suma = logger(suma)
