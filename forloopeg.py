#example 1 printing numbers inbetween two numbers

'''a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
for i in range(a+1,b):
    print(i)'''

#example 2 printing even numbers inbetween two numbers

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))    
for i in range(a,b):
    if i%2==0:
        print(i)