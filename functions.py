'''////////////////////////////FUNCTIONS////////////////////////////////'''

'''def painter():
    print("This is a painter function.")
painter()'''

#Example to create functon to get a number add(),sub(),mul(),div()

'''def getnum():
    num=int(input("Enter a number1: "))    
    return num
def add(a,b):
    print("Addition of number 1 and 2: ",a+b)
def sub(a,b):
    print("subraction of number 1 and 2: ",a-b)
def mul(a,b):
    print("Multiplicarion of number 1 and 2: ",a*b)
def div(a,b):
    print("Division of number 1 and 2: ",a//b)

a=getnum()
b=getnum()
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)'''

#Another example

'''def painter(msg):
    print("paint my",msg)

painter("house")'''

#Example to find odd or even

'''def get_num():
    num=int(input("Enter a number : "))
    return num
def find_odd_even(num):
    if num%2==0:
        print("Even number")
    else:
        print("Odd number")

a=get_num()
find_odd_even(a)'''

#Example to get name and age

'''def getname():
    name=input("Enter your name: ")
    return name
def getage():
    age=input("Enter your age : ")
    return age
def op(n,a):
    print("Name is:",n,"\nAge is: ",a)
name=getname()
age=getage()
op(name,age)'''

#Example to print between range

'''def get_num():
    num=int(input("Enter a number : "))
    return num
def find_range(a,b):
    for i in range(a,b):
        print(i)

a=get_num()
b=get_num()
find_range(a,b)'''

#Example return

'''def painter():
    return "I am painter"

print(painter())'''

#Example to check login

'''def get_user_name():
    usr=input("Enter your user name: ")
    return usr
def get_password():
    pas=input("Enter password: ")
    return pas
def validate(usr,pas):
    if usr=="sha" and pas=="2306":
        return True
             "OR"
        #print("valid")
    else:
        return False
            "OR"
        #print("Invalid")
user=get_user_name()
pas=get_password()
a=validate(user,pas)
print(a)'''

#Example to return

'''def add(a,b):
    return a+b
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
ans=add(a,b)
print(ans*c)'''