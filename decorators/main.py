import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = original_result.upper()
        print(func.__name__)
        return modified_result
    return wrapper

@uppercase
def greet(name):
    return f"hello {name}"

print(greet("REZA"))

