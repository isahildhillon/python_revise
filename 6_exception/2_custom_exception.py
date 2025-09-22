class CustomError(Exception):
    '''A Simple Custom Error'''
    pass

age=int(input("Enter Your Age : "))
if age>=18:
    print("You can vote")
else:
    raise CustomError("You can not vote")