def one_val_checker(new_func):
    def two_val_checker(func):
        def wrapper(number):
            if new_func(number):
                print(func(number))
            else:
                raise ValueError('{}'.format(number))

        return wrapper

    return two_val_checker


@one_val_checker(lambda i: i > 0)
def cube(i):
    return i ** 3


try:
    result = cube(int(input('Введите число: ')))
except ValueError:
    print('Error')
