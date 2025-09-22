def log_activity(func):
    def wrapper(*args,**kwargs):
        print(f"calling function {func.__name__}")
        result=func(*args,**kwargs)
        print(f"Finished calling {func.__name__}")
        return result
    return wrapper

@log_activity
def add(x,y):
    return x+y

print(add(5,4))