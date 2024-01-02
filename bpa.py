import math

temp = float(input("What is your temperature?: "))
fc = input("Is that F or C?: ")

print("Temperature is: " + str(temp))
print("Temperature unit is: " + fc)


# hardest part to figure out
def if_C():
    if fc == 'C':
        converted_temp = (temp * 9/5) + 32
        print("Converted temperature is: " + str(converted_temp) + " F")

def if_F():
    if fc == 'F':
        converted_temp = (temp - 32) * 5/9
        print("Converted temperature is: " + str(converted_temp) + " C")

if_C()
if_F()
