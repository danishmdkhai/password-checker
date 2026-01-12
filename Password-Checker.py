import pwinput

# Intro/starter
print("Welcome to The Password Checker\n")

# Enter password(pwinput hides the password with *)
while True:
   Password = pwinput.pwinput("Please input your password:\n")

   has_letter = False
   has_number = False
   has_symbol = False

   # Minimum 7 word password
   if len(Password) <= 7:
      print("Please make your password longer")
      continue


   # Checks if alphabest,letters,symbols are missing from your password
   for char in Password:
      if char.isalpha():
         has_letter = True
      elif char.isdigit():
         has_number = True
      else:
         has_symbol = True

   # Tells you what's missing from the password
   if has_letter == False:
      print("Your Password needs alphabets")
   if has_number == False:
      print("Your Password requires a number")
   if has_symbol == False:
      print("Your Password requires a Symbol")

   if has_letter and has_number and has_symbol:
      print("Your password is safe")
      break
