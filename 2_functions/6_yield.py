def count_upto_n(n):
    count=1
    while count<=n:
        yield count
        count+=1

num= count_upto_n(3)
print(next(num))
print(next(num))
print(next(num))