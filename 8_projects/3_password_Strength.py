import re

weak_passwords = {
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "123123", "admin", "letmein", "welcome"
}

def check_password(password):
    score=0
    feedback=[]
    if password.lower() in password:
        feedback.append("This password is too common. Please use another password")
    else:
        score+=1
    
    # check length
    if(len(password)>8):
        score+=1
    else:
        feedback.append("Password should be at least of 8 letters. ")

    # check lower case and upper case
    if re.search(r'[a-z]',password) and re.search(r'[A-Z]',password):
        score+=1
    else:
        feedback.append("Password should have atleast 1 lowercase and 1 uppercase")
    
    # check digit
    if re.search(r'[\d]',password):
        score+=1
    else:
        feedback.append("Password should have atleast 1 number")
    
    # check special characters
    if re.search(r'[!@#$%^&*()<>?;:{}]',password):
        score+=1
    else:
        feedback.append("Password should have at least 1 special charcter")

    # strength level
    strength_level = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }

    return {
        'password':password,
        'score':score,
        'strength':strength_level[score],
        'feedback':feedback
    }

if __name__=="__main__":
    print("🔐 Password Strength Checker")
    password = input("Enter your password : ")
    result = check_password(password)

    print(f"\n Your password strength is {result['strength']} and score is {result['score']}")
    if result['feedback']:
        print('-'*50)
        for feedback in result['feedback']:
            print(" - ",feedback)
    else:
        print("Great Job your password is strong")