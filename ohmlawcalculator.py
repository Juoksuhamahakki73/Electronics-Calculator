# This program was written by Juokuhamakk73 and debugged by ChatGPT (hyperlink:https//openai.com/index/chatgpt)

# This import the math library into this code

import math

# This import the numpy library into this code
import numpy

#This will calculate the resistance with the given Amps and Voltage
def resistor(user_give_num1, user_give_num2):
    total_resistor = user_give_num1 / user_give_num2
    return(total_resistor)

#This will calculate the current with the given resistance and Voltage
def current(user_give_num1, user_give_num2):
    total_currents = user_give_num1 / user_give_num2
    return total_currents

#This will calculate the voltage with the given Amps and resistance
def voltage(user_give_num1, user_give_num2):
    total_voltage = (user_give_num1 * user_give_num2)
    return total_voltage

# Now We will ask the user what is needed to be calculated

print("Hello user! Welcome to Juokuhamakk73 Oh's law calculator")

while True:
    print("I would like to ask what is the unknown component that needs to be solved?")
    input_unknown = input("Please enter here (resistance, voltage, current): ").strip().lower()

    if input_unknown not in ["resistance", "voltage", "current"]:
        print("Sorry, the unknown component is invalid. Please enter 'resistance', 'voltage', or 'current'.")
        continue

    print("Great, now can you input the two given components to solve that unknown?")

    try:
        user_give_num1 = float(input("Please enter the first number: "))
        user_give_num2 = float(input("Please enter the second number: "))

        if input_unknown == "resistance":
            result = resistor(user_give_num1, user_give_num2)
            print(f"The unknown Resistance is: {result}")
            break

        elif input_unknown == "voltage":
            result = voltage(user_give_num1, user_give_num2)
            print(f"The unknown Voltage is: {result}")
            break

        elif input_unknown == "current":
            result = current(user_give_num1, user_give_num2)
            print(f"The unknown Current is: {result}")
            break

    except ValueError:
        print("Sorry, you gave me an invalid number. Please try again.")
