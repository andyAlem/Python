import time
from functools import wraps


def log(filename=None):
    """Декоратор log, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            start_function_info = (
                f"{func.__name__} started: {time.strftime('%Y-%m-%d %H:%M:%S')} *:{args}, **:{kwargs}"
            )
            print(start_function_info)
            if filename:
                with open(filename, "a") as file:
                    file.write(start_function_info + "\n")
            try:
                result = func(*args, **kwargs)
                log_message = "my_function is ok"
                print(log_message)
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                return result
            except Exception as ex:
                log_message = f"{func.__name__} Error: {ex}. Inputs: {args}, {kwargs}"
                print(log_message)
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
            finally:                                #https://sky.pro/media/zachem-nuzhna-konstrukcziya-finally-v-python/
                end_time = time.time()
                time_for_work = end_time - start_time
                time_for_work_info = (
                    f"{func.__name__} finished:{time.strftime('%Y-%m-%d %H:%M:%S')} "
                    f"(Time for work: {time_for_work:.2f} seconds)"
                )
                print(time_for_work_info)
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
