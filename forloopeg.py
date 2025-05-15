#example 1 printing numbers inbetween two numbers

'''a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
for i in range(a+1,b):
    print(i)'''

#example 2 printing even numbers inbetween two numbers

'''a=int(input("Enter a number: "))
b=int(input("Enter a number: "))    
for i in range(a,b):
    if i%2==0:
        print(i)'''

#example 3 counting odd numbers inbetween two numbers

'''a=int(input("Enter a number: "))
b=int(input("Enter a number: "))  
c=0
for i in range(a,b):
    if i%2!=0:
        c=c+1
print(c) '''

#Example for count the odd and even numbers inbetween two numbers

'''a=int(input("Enter a number: "))        
b=int(input("Enter a number: "))
even=0
odd=0
for i in range(a,b):
    if i%2==0:
        even=even+1
    elif i%2!=0:
        odd=odd+1
print("even=",even,"\nodd=",odd)'''

#Example for printing the numbers which are divisible by 3 and 5

a=int(input("Enter a number: "))    
b=int(input("Enter a number: "))
num3=0

for i in range(a,b):
    if i%3==0 and i%5==0:
        num3=num3+1
print("number divicible by 3 and 5 are =",num3)

