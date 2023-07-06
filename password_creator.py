import random

name = input("Which account password you want?: ")
chars = "abcdefghijklmnopqrstuvwxyz"
nums = "12345467890"
spec = "_@!&*"
li = []


for i in range(16):
    if i <= 10:
        pos = random.randint(0, 25)
        li.insert(i, chars[pos])
    elif i <= 14:
        pos = random.randint(0, 9)
        li.insert(i, nums[pos])
    else:
        pos = random.randint(0, 4)
        li.insert(i, spec[pos])


random.shuffle(li)
password = ''.join([str(element) for element in li])
print(name + ": " + password)

with open("C:\\Users\\Red\\Desktop\\beg-python\\text_file\\pass_creator.txt", 'w') as pass_file:
    pass_file.write(f"{name} is : {password}\n")
