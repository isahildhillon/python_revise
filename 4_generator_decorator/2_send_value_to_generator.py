# Send value to a generator

def admission_cell():
    print("Hello! Welcome to The Pathify")
    name=yield # at this line program has just printed above statement and wait for any value to come using .send function
    while True:
        print(f"{name} is granted admission to The Pathify")
        name=yield # this now again waits for new value, id dont added this will keep running loop

student = admission_cell()
next(student) # run and wait to get data (till line 3)
student.send("Sahil")