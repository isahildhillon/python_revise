n = 3
while n > 0:
    print(n)
    n -= 1
else:
    print("Loop finished without break")

"""Output
3
2
1
Loop finished without break
"""

n = 3
while n > 0:
   if n%2==0:
       break
   else :
       print(n)
       n-=1
else:
    print("Loop finished without break")

"""output
3

"""

# here else dont run