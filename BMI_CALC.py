import os
valueW = float(input("please enter your weight in kg: "))
valueH = float(input("please enter your height in cm : "))
BMI = valueW / (valueH/100)**2 

print( "Your BMI is: " + str(round(BMI,2))  )
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")

os.system("pause")
