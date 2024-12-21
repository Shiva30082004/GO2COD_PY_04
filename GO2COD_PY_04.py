'''
GO2COD PYTHON PROGRAMMING INTERNSHIP
TASK 04 : BMI CALCULATOR
NAME: SHIV BHAVSAR

This program will ask the user for his/her weight and height and
then the program will calculate and categorize the BMI results.
'''

# title
print("Welcom to the BMI (Body Mass Index) Calculator: ")

print(" ")

# ask user to enter his/her weight and height
weight = eval(input("Enter your weight in kilograms(Kg): "))
height = eval(input("Enter you height in meters(m): "))

print(" ")

# calculate BMI
b_m_i = weight/(height**2)

# display BMI results
print("Your BMI is: ","%.2f"%b_m_i)

# categorize BMI results using if-else condition statements
# if BMI is less than 18.5, the person is underweight.
if (b_m_i < 18.5):
    print("You are Underweight. Gain some weight. ")

# if BMI is greater than or equal to 18.5 and less than 25, the person is normal weight.
elif (b_m_i >= 18.5) and (b_m_i < 25):
    print ("Great! You are Normal weight. Keep it up. ")

# if BMI is greater than or equal to 25 and is less than 30, the person is overweight.
elif (b_m_i >= 25) and (b_m_i < 30):
    print("You are Overweight. Adopt a healthier lifestyle. ")

# if BMI is greater than or equal to 30, the person is obese.
else:
    print("You are a Obese. Consult a healtcare expert.")
    
print(" ")
print("Thank you for using our BMI Calculator.")
print("Have a good day. Visit again....")
