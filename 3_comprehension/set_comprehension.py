nums= [1, 2, 2, 3, 3]
unique_squares = {x**2 for x in nums}
print(unique_squares)  # Output: {1, 4, 9}


students = {
    'Arts':['Ravi','Mohit','Ashish'],
    'Commerce' :['Monu','Daksh','Ravi'],
    'Non Medical' :['Sahil','Pardeep',"Ashish","Mohit"]
}

unique_students = [unique_student for student in students.values() for unique_student in student]
print(unique_students)