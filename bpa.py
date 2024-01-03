import math
import datetime
import os

temp = float(input("What is your temperature?: "))
fc = input("Is that F or C?: ")

print("Temperature is: " + str(temp))
print("Temperature unit is: " + fc)


# hardest part to figure out
def if_C():
    if fc == 'C':
        converted_temp = (temp * 9/5) + 32
        print("Converted temperature is: " + str(converted_temp) + " F")
        record_temperature(temp, converted_temp, 'C')


def if_F():
    if fc == 'F':
        converted_temp = (temp - 32) * 5/9
        print("Converted temperature is: " + str(converted_temp) + " C")
        record_temperature(temp, converted_temp, 'F')


def record_temperature(original_temp, converted_temp, unit):
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{current_datetime} - Original Temp: {original_temp} {unit}, Converted Temp: {converted_temp} {'F' if unit == 'C' else 'C'}\n"
    
    if not os.path.exists("temps_recorded.txt"):
        with open("temps_recorded.txt", "w") as file:
            file.write("Date/Time - Original Temp - Converted Temp\n")
    
    with open("temps_recorded.txt", "a") as file:
        file.write(log_entry)


if_C()
if_F()
