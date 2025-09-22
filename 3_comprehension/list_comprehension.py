num = [1,2,3,4,5,6,7]

squared_num= [x**2 for x in num]
print(squared_num)

squared_even_num = [x**2 for x in num if x%2==0]

print(squared_even_num)