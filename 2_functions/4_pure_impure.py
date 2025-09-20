msg="Hello Everybody"

def view_msg():
    """This is a pure function"""
    print(msg)

def update_msg():
    """this is a impure function"""
    global msg
    msg="This is new Value"
    print(msg)

view_msg()
update_msg()