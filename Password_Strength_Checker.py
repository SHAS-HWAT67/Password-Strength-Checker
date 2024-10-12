#Password Strength Checker

import re

password=input("Enter your password:" )

#Password must be of 8 to 16 characters long
if len(password)<8:
   print("Password is short. Password must be 8 characters long")
elif len(password)>16:
    print("Password is too long. Password must be 16 characters only")

#Password must contain atleast one uppercase letter
elif not re.search("[A-Z]",password):
    print("Password must contain atleast one uppercase letter")
     
#Password must conatin atleast one lowercase letter
elif not re.search("[a-z]",password):
    print("Password must conatin atleast one lowercase letter")
     
#Password must contain atleast one number
elif not re.search("[0-9]",password):
    print("Password must contain atleast one number")
else:
    print("Password is strong")
