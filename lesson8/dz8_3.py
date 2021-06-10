from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        my_number = [i for i in (*args, *kwargs.values())]
        tmp = [f'{func.__name__}({i}: {type(i)})' for i in my_number]
        print(*tmp, *func(*args, **kwargs))

    return wrapper


@type_logger
def cube(*a, **b):
    new_list = [i for i in (*a, *b.values()) if isinstance(i, float) or isinstance(i, int)]
    return [i ** 3 for i in new_list]


result = cube(1, 2, 3, 'Time', 4.3, [1, 3], {"key": 'val'})

print(result)
