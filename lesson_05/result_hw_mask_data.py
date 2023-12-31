from hw_05 import mask_data

# TARGET FUNCTIONS


@mask_data(target_key=["name"])
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# @mask_data(target_key=["name","age"])
# def get_user(name: str, age: int):
#   return {
#     "name": name,
#     "age": age
#   }


# TEST OUPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
