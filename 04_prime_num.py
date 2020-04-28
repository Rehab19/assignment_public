num = input("please enter a number: ")

if not num.isdigit():
    print("please enter a positive number: ")
    
elif  int(num) > 1:
    num = int(num)
    for i in range(2, num):
        if (num % i) == 0:
           print(f"{num} is not a prime number")
           break
    else:
        print(f"{num} is a prime number")  
else:
    print("please enter a number bigger than 1")          
