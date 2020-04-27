num1 = input("please enter a number: ")
power = len(num1)
sum = 0

if ("." in num1) or ("," in num1):
    print("please enter an integer number") 
elif ("-" in num1):
    print("please enter a positive number")
elif not num1.isdigit():
    print("please enter a numeric value")
elif int(num1) >= 0 :
    for i in range(power):
       sum += int(num1[i])**power
    if sum == int(num1):
        print(f"{num1} is an Armstrong number")
    else:
        print(f"{num1} is not an Armstrong number")    
