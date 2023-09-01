# names=["John","Merry"]

# _names =iter(names)

# for name in names:
#     print (f"{name=}")

names:list[str]=["John","Merry"]

_names =iter(names)
print(names.__next__())
print(names.__next__())
print(names.__next__())

class Iterator:
    def __iter__(self):
        pass
    def __next__(self):
        pass
instances = Iterator()
for instance in instances:
    print (instance)


while True:
    # name=names.__next__()
    try:
       value = next(_names)
       print (f"{value =}")
    except StopIteration:
        break