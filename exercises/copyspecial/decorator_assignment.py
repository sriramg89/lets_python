
def logged(func):
    def inner(*args,):
        func(*args)
        print("You called func" + str(args))
        print("It returned "+str(func(*args)))
    return inner

@logged
def func(*args):
    return 3 +len(args)

func(4,4,4)