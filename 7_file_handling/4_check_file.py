from os import path

if path.exists('hello.txt'):
    print("File exists")
else:
    print('File dont exists')