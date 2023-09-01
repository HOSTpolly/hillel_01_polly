# print(1+1)
# print("1"+"1")


from functools import singledispatch


@singledispatch
def custom_add(a,b):
   raise NotImplementedError("Unsupported type")
   
@custom_add.register(int)
def _(a,b):
    return a+b
    

@custom_add.register(int)
def _(a,b):
    return f"Concat {a} {b}"


 
print(custom_add(1,1))
print(custom_add("1","1"))
print(custom_add(12.1,"1"))

# class Authentication:
#     def __init__(self, user: User | Anonymous) ->None:
#         self.user: User|Anonymous

# Class User:
#     name:strpassword:str
    
# class Anonymous:
#     geo:list
    
# class Backend:
#     @singledispatch
#     def get_admin_page.register(User):
#     raise NotImplemented
    
#     @get_admin.register
#     def get_admin_page.register(User):
#     return admin_page
    

    