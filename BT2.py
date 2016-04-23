print('Height in inches')
height = float(input())*0.0254
print('Weight in pounds')
weight = float(input())*0.45359237
BMI = float
BMI = weight / (height*height)
if BMI < 18.5:
    print('Underweight')
elif 18.5 <= BMI <25.0:
    print('Normal')
elif 25.0 <= BMI <30.00:
    print('Overweight')
else: print('Obese')
