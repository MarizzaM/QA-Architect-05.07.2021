def foo1(*args):
    print(len((set(args))))

foo1(1, 1 , 4 , 5 , 6 , 7, 1, 4, -3)

def foo2(**kwargs):
    print(f'keys = {kwargs.keys()}')
    print(f'values = {kwargs.values()}')

    print(len(set(kwargs.values())))
    print(len(kwargs.values()))

foo2(name='danny',  age=12, city='TV')
