from functools import wraps

def log(filename:None)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = 'my_function is ok'
                print(log_message)
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                return result
            except Exception as ex:
                log_message = f"{func.__name__} Ошибка : {ex}. Inputs: {args}, {kwargs}"
                print(log_message)
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
        return wrapper
    return decorator
