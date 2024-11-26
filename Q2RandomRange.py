# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random 
while True:
   start = input("Enter start number: ")
   if start.isdigit():
       start = int(start)
       break
   print("Please enter a number only.")

while True:
   end = input("Enter end number: ")
   if end.isdigit():
       end = int(end)
       break
   print("Please enter a number only.")

# Generate and print random number
random_number = random.randint(start, end)
print(f"Random number between {start} and {end}: {random_number}")