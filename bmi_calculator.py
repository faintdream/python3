#!/usr/bin/env python

#This program can calculate BMI using metric as well as imperial unit.
# formula 
# Metric system   - BMI= (weight in kg/height in meter **2)  
# Imperial system - BMI = BMI*703


def get_info():
    """
    get_info() method is used to collect 
    necessary user input. 
    """
    height = float(raw_input("User's height - ")) 
    weight = float(raw_input("User's weight - "))
    system = raw_input("Preferred measurement unit (m|M) metric / (i|I) Imperial - ").lower().strip()
    return (height, weight, system)

def validate_input(system):
    """
    validate_input() is used to sanitize 
    user input for metric system.
    """
    print("System : " + system )
    if system == "m" or system == "i":
        return True
    else:
        print("Available measurement unit are m or i")
        return False
def calculate_bmi(height, weight, system):
    """
    calculate_bmi function is used to calculate bmi.
    """
    bmi = (weight/(height**2))
    if system == "i" :
        bmi = bmi*703
    else:
        print("Measuring System set to " + system )
    return bmi
           
height,weight,system = get_info()
if validate_input(system):
    result = calculate_bmi(height=height, weight=weight, system=system)
    print("User' BMI - %f" %result) 
    


