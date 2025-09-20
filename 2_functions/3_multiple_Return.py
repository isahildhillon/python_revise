def multiple_return():
    '''    This function returns multiple values''' # this is a doc string
    return "Sahil",22,"India"

name,age,country = multiple_return()
print("My Name is ", name)
print("My Age is ", age)
print("My Country is ", country)

"""Output
My Name is  Sahil
My Age is  22
My Country is  India
"""
biodata = multiple_return()
print(biodata)


# Output ('Sahil', 22, 'India')
