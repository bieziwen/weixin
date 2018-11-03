import time
def times(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        for i in range(1,10000):
            func()
        end_time=time.time()
        t=end_time-start_time
        return t
    return wrapper


@times
def f():
    pass


if __name__ == '__main__':
    print(f())
