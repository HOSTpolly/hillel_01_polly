import functools


def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        string = func(*args, **kwargs)

        if isinstance(string, str):
            reversed_string = string[::-1]
            return reversed_string
        else:
            return None

    return wrapper


def mask_data(target_key):
    """Replace the value of specific keys in a dictionary with a 'masked' version."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_dict = func(*args, **kwargs)
            if isinstance(current_dict, dict):
                masked_dict = current_dict.copy()
                for key in target_key:
                    if key in masked_dict:
                        replace_with = "*"
                        masked_dict[key] = replace_with
                return masked_dict
            else:
                return current_dict

        return wrapper

    return decorator
