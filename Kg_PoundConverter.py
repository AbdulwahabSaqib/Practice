Weight = int(input("Weight: "))
X = input("(K)g or (L)bs:")
if X == "l":
    converted = Weight / 0.45
    print("Weight is pounds:" +str(converted))
else:
    converted = Weight * 0.45
    print("Weight in Kgs :"+ str(converted))
