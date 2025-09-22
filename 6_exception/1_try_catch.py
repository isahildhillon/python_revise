try:
    print(5/0)
except:
    print("Error occurred")
else: # will run if no error
    print("Run perfectlly")
finally:
    print("The task is over")