# -i-u-ki-n-if-then-else
#bài 1
score = int(input())
if score >= 90:
    print('Grade is A')
elif score >= 80:
    print('Grade is B')
elif score >= 70:
    print('Grade is C')
elif score >= 60:
    print('Grade is D')
else: print('Grade is F')

#bài 2
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
