#The program takes a person's weight and height as input and outputs the corresponding BMI category.
weight=float(input())
height=float(input())
bmi=weight/(height*height)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obesity")
