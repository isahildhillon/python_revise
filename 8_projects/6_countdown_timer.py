import time
seconds = int(input("Enter time in seconds : "))

for remaining in range(seconds,0,-1):
    min,sec = divmod(remaining,60) # gives divisor  and modulus
    time_format= f" {min:02}:{sec:02}"
    print(f"Time left : {time_format}" , end='\r')
    time.sleep(1)
