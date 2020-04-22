
# Takes "Yes" or "No" from the user as an answer to the following questions :

# Are you a cigarette addict older than 75 years old? Variable → age

# Do you have a severe chronic disease? Variable → chronic

# Is your immune system too weak? Variable → immune

age = input("Are you a cigarette addict older than 75 years old? yes/no: " ).lower()
chronic = input("Do you have a severe chronic disease? yes/no: ").lower()
immune = input("Is your immune system too weak? yes/no: ").lower()

if age == "yes":
    age = True
else:
    age = False

if chronic == 'yes':
  chronic = True
else:
  chronic = False

if immune == 'yes':
  immune = True
else:
  immune = False

if age or chronic or immune == True :
   print("you're in risky group")
else:
   print("you're not in riskey group")