"""decorator function_info"""


def function_info(func):
    """function_info"""
    def wrapper(*args, **kwargs):
        """function_info"""
        function_name = func.__name__
        all_parameters = []
        new_kwargs = list(kwargs.items())

        for i in args:
            all_parameters.append(i)

        for i in new_kwargs:
            all_parameters.append(i)

        print(f"{function_name} is been called with parameters: {all_parameters}")
        result = func(*args, **kwargs)
        # print(result)
        print(f"Function {function_name} return this value: {result}")
        return result
    return wrapper


@function_info
def add_numbers(a, b):
    """example"""
    return a + b


print(add_numbers(8, 7))
