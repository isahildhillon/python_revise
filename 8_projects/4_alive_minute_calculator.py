import datetime
def calculate_minutes():
    # get date of birth
    dob=input("Enter your date of birth in dd/mm/yyyy format : ")

    # get time of birth
    tob=input("Enter your time of birth in Hour:Minute in 24 hourFormat : ")
    tob = tob if tob else "00:00"
    print(tob)
    birth_string = dob + " "+ tob
    birth_datetime=datetime.datetime.strptime(birth_string,"%d/%m/%Y %H:%M")
    print(birth_datetime)
    # SPLIT all and change to minutes
    
    #Date and Time Now
    now=datetime.datetime.now()

    alive_time=now- birth_datetime
    minutes= int(alive_time.total_seconds()/60)
    print(f"You are alive for {minutes} minutes on earth")

calculate_minutes()