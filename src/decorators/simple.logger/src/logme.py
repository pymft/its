import time


def logme_part_one(fn):
    def inner(*args, **kwargs):
        res = fn(*args, **kwargs)

        log_str = f'"{time.time()}","{fn.__name__}","{args}","{kwargs}","{res}"\n'
        f = open('logs.csv', mode='a')
        f.write(log_str)
        f.close()

        return res
    return inner


def logme_part_two(filename):
    def decorator(fn):
        def inner(*args, **kwargs):
            res = fn(*args, **kwargs)

            log_str = f'"{time.time()}","{fn.__name__}","{args}","{kwargs}","{res}"\n'
            f = open(filename, mode='a')
            f.write(log_str)
            f.close()

            return res
        return inner
    return decorator


class LogMeClass:
    def __init__(self, filename):
        self.__filename = filename

    def __call__(self, fn):
        def inner(*args, **kwargs):
            res = fn(*args, **kwargs)

            log_str = f'"{time.time()}","{fn.__name__}","{args}","{kwargs}","{res}"\n'
            f = open(self.__filename, mode='a')
            f.write(log_str)
            f.close()

        return inner
