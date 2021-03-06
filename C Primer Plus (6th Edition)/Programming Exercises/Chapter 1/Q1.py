'''
You have just been employed by MacroMuscle, Inc. (Software for Hard Bodies). The 
company is entering the European market and wants a program that converts inches 
to centimeters (1 inch = 2.54 cm). The company wants the program set up so that it 
prompts the user to enter an inch value. Your assignment is to define the program 
objectives and to design the program (steps 1 and 2 of the programming process).
'''

inch_value = float(input("Please enter the value of Inches: "))
cm_value = inch_value * 2.54
print(f'{str(inch_value)} in = {str(cm_value)} cm')
