train_coach= "General"

match train_coach:
    case "General":
        print("You have no fixed seat")
    case "First_Ac":
        print("You have got best seat")
    case "Sleeper":
        print("You can sleep but no ac")
    case _:
        print("This is default case")