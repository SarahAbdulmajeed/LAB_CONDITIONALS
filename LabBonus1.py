weight:float = float(input("Weight(kg): "))
height:float = float(input("Height(cm): "))
BMI:float = weight / (height/100)**2

print(f"BMI: {round(BMI,2)}")

if BMI >= 18.5 and BMI < 25:
    print("You are fit & healthy.")
elif BMI < 18.5:
    print("underweight. Watch your health.")
else: 
    print("You are overwieght you need to work out more and watch your diet.")