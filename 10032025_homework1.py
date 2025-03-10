# Task-1: 
# Write a short Python program that asks the user to enter 
# Celcius temperature (it can be a decimal number), 
# converts the entered temperature into Fahrenheit degree and prints the result


# Task-2:
# Write a short Python program that asks the user to enter
# a distance (it can be a decimal number) in kilometers, 
# converts the entered distance into miles and prints the results.

print(not 0 and"write me")

year = int(input("Please enter the year?"))
result = False
if year%4 == 0: 
    if year%100 == 0: 
        if year%400 == 0:
            result = True
    else: 
        result = True
print(f"Is year {year} leap? : {result}")
