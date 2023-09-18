import functools
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        string = func(*args, **kwargs)
        # isinstance(object, type)
        if isinstance(string, str):  # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
            reversed_string = string[::-1] # start from the end of the string and move backward by one character at a time until the beginning of the string is reached.
            return reversed_string
        else:
            return None  # Return None if the result is False
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

