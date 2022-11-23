#### BMI = weight/(height^2)
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

BMI = float(weight / (height ** 2))
print(BMI)
if BMI <= 18.5:
    print(f"Your BMI is {BMI.__round__(1)}. You are Underweight.")
elif 18.5 < BMI <= 25:
    print(f"Your BMI is {BMI.__round__(1)}. You are Normal.")
elif 25 < BMI <= 30:
    print(f"Your BMI is {BMI.__round__(1)}. You are Overweight.")
elif BMI > 30:
    print(f"Your BMI is {BMI.__round__(1)}. You are Obese.")
