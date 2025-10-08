import datetime
def Intro(name,age,city,profession,hobby):
    print(f"Hey My name is {name} ,You know me, I am {age} years old and working as {profession}. I Love to spend my time productively on {hobby} in my free time. I live in {city}")
    print(datetime.date.today().strftime('%d-%m-%Y'))

name=input("Enter your name : ")
age=int(input("Enter your age : "))
city=input("Enter your city : ")
profession=input("Enter your profession : ")
hobby=input("Enter your hobby : ")

Intro(name,age,city,profession,hobby)