import datetime
def logger(func):
    def inner(*args, **kwargs):
        s = datetime.now()
        print(s)
        func(*args, **kwargs)
    inner._name_ = func._name_
    return inner
@ logger
def suma(a, b):
    if a>0 and b >0:
        print(a, b)
        return a+b
        print(suma._name_)
    elif a<0 and b<0:
        print(a, b)
        return a-b
        print(suma._name_)
    else:
        print(a, b)
        return 0
        print(suma._name_)
