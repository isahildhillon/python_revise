# this is a decorator
def movie_hall(func): 
    def wrapper():
        print("Movie starts")
        func()
        print("Movie ends")
    return wrapper
    

@movie_hall # defining decorator for interval func. 
def interval():
    print("Interval")

interval()

# when we call interval first movie hall decorator run when we call func() interval will exceute and then remaining movie hall will execute


