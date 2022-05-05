import os

try:
    os.remove("myNewFile.txt")
except:
    print("Something went wrong")

print(2)