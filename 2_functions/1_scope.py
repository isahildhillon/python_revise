
msg='hello' # global scope

def access_global():
    global msg
    print(msg)
    
def sum():
    a = 2 # local scope
    b =3 # local scope
    print(a+b)

def outer():
    msg="this is outer msg" # Enclosed scope for inner function
    def inner():
        nonlocal msg
        msg="This is inner"
    inner()
    print(msg)

access_global()
sum()
outer()