def infinite_count():
    count=1
    while True:
        yield count
        count +=1

count = infinite_count()
print(next(count))