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

"""a=int(input("Enter a number: "))    
b=int(input("Enter a number: "))
num3=0

for i in range(a,b):
    if i%3==0 and i%5==0:
        num3=num3+1
print("number divicible by 3 and 5 are =",num3)"""

#Example 6 sum of first 5 natural numbers

'''sum=0
for i in range(1,5+1):
    sum=sum+i
print(sum)'''

#Example 7 getting multiple using list integer and adding it

'''a=[]
for i in range(10):
    num=int(input("Enter number"+str(i+1)))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)'''

#Example 8 get n numbers and print the sum of n numbers

'''num=int(input("Enter a numbers: "))
a=[]
for i in range(num):
    n=int(input("Enter number"+str(i+1)))
    a.append(n)
sum=0
for i in a:
    sum=sum+i
print(sum)'''

#Example 9 get a number and display its cube value

'''n=int(input("Enter a number: "))
for i in range(n):
    print("Number is ",i," cube of the number is ",i*i*i)'''




