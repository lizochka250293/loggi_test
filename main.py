import datetime
def logger(func):
    def arguments(arg1, arg2):
        print(datetime.now())

        func()
    return arguments(arg1, arg2)
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
