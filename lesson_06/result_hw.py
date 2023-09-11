from hw_06 import mask_data

# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


callable = mask_data(target_key="name")
another_callable = callable(get_user)
another_callable("John", 12)


# TEST OUPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
