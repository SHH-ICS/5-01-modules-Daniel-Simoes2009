# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.


a = float(input("Value of a(a): "))
if a <= 0:
    print("na ah")
     

b = float(input("value of b(b): "))
if b <= 0:
    print("na ah")
    
c = (a**2)+(b**2)
print(c**2) 