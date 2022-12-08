# Get year to check from user
year = int(input("Which year do you want to check? "))

# Check if year is leap year and return result
if year % 4 == 0:
   if year % 100 != 0:
       print("Leap year.")
   else:
       if year % 400 == 0:
           print("Leap year.")
       else:
           print("Not leap year.")
else:
    print("Not leap year.")