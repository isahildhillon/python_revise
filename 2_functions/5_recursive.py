def print_numbers(n):
    if n==0:
        return "Printed All Numbers"
    print(n)
    return print_numbers(n-1)

print(print_numbers(5))