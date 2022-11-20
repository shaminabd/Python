def s(a, b, *arg, **kwargs):
    print(a)
    print(b)
    print('arg: ')  # все не проинициализированные позиционные аргументы
    for i in arg:
        print(i)
    print('kwargs: ') # словарь со всеми не проинициализированными именованными аргументами
    for key in kwargs:
        print(key, kwargs[key])
s(10, 20, 30, 40, c = 50, d = 60, j = 70)