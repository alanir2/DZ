def test(a, b=4, *args, **kwargs):
    print('a and b', a, b)
    print('type', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('poz primer', i, arg)
    print('tip kwargs', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('imen arg', key, '=', value)


test(5, 6, 7, 8, cat='mow')
test(5, b=8, cat='mow')
test(5, cat='mow', address='moscow')

# Факториал
def factorial_1(n):
    if n == 1:
        return 1
    fac_min_1 = factorial_1(n=n - 1)
    return n * fac_min_1


print(factorial_1(9))


def factorial_2(x):
    pr = 1
    for i in range(1, x+1):
        pr = pr * i
    return pr


print(factorial_2(9))
