from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent

file = open(ROOT_DIR / "rockyou.txt", encoding="utf-8", mode="r")


counter = 0  # зміна,що зберігає кількість знайдених user у файлі
result = []  # зміна, що зберігає відібрані паролі у список
added_lines = 0  # зміна,що зберігає кількість доданих паролей

while True:
    try:
        line = file.readline()

        for word in line.split():
            print("Do you want to add this word:" f"{word}" " to your password_list ?")
            print(" Please, enter your desision:")

            var = input()

            if str.casefold(var) == "yes":
                result.insert(len(result), word)
                added_lines += 1

                if word == "user":
                    counter += 1
                    print("This line: " f"{line}" "contains the word 'user' ")

            elif str.casefold(var) == "enter":
                continue

            elif str.casefold(var) == "end":
                file.close()

        continue

    except Exception as a:
        print("Error:", a)
        break


print("user" f"{counter=}")
print(f"{result=}")
print(f"{added_lines=}")
