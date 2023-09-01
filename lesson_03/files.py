# file = open("./lesson_3/text.txt")
# lines:list[str]=file.readlines()
# print(lines)

# from pathlib import Path 
# ROOT_DIR = Path (__file__).absolute().parent
# # this_file = Path (__file__).absolute().parent

# #breakpoint() //WindowsPath('d:/hillel_polly/hillel_01_polly/lesson_3/files.py')

# # file = open("./lesson_3/text.txt")
# file = open( ROOT_DIR / "text.txt")
# lines:list[str]=file.readlines()
# print(lines)


from pathlib import Path 
import codecs
ROOT_DIR = Path (__file__).absolute().parent
# this_file = Path (__file__).absolute().parent

#breakpoint() //WindowsPath('d:/hillel_polly/hillel_01_polly/lesson_3/files.py')

# file = open("./lesson_3/text.txt")
file = codecs.open( ROOT_DIR / "rockyou.txt" , encoding='utf-8', mode='r')
# lines:list[str]=file.readlines()
# text:str=file.read()
text:str=file.readline()
counter = 0
while True:
    try:
        word=file.readline()
        counter += 1
        print(word)
    except Exception:
        break
        
        
print(counter)