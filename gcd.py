import  sys
name=input("Enter your name:")
print("Welcome"+name+"for calculating the Gcd of two numbers")
yes=input("If you would like to continue press 1 else press 2")
if(yes=='one'):#Creating Gcd of two numbers without using functions
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    if(b/a!=0):
        r=b%a
        b=a
        a=r
        print(a)
        
    else:
        print("Sorry!!!!")
else:
    print("Thank you for choosing my services")    
