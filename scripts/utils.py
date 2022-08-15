import time


def run_time_calculation(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        calculated = time.time() - start
        print(f'Выполнено за: {calculated} секунд')
        return result
    return wrapper
