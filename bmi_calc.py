# BMI CALCULATOR



weight = int(input("Enter the weight: "))
height = float(input("Enter the height: "))
# Calculate the weight and height here - weight / (height * height)
result = weight / (height * height)

# Condition where it belongs
if result < 18.5:
    print("Underweight")
elif result >= 18.5 and result < 25:
    print("Normal")
elif result >= 25 and result < 30:
    print("Overweight")
else:
    print("Obesity")