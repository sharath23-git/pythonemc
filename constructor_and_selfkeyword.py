'''class lap:
   
    def __init__(self):
        self.name=""
        self.price=0
        self.ram=""
        self.processor=""
        
    def display(self):
        print("Name of laptop: ",self.name)
        print(self.price)
        print(self.ram)
        print("New display")

hp=lap()
dell=lap()
dell.name="DELL"
dell.ram="16GB"
dell.price=30000
dell.processor="i7"
hp.name="HP"
hp.ram="8GB"
hp.price=20000
hp.processor="i5"
hp.display()
dell.display()'''

#Example 1
'''class student:
    def __init__(self):
       self.name="sel"
       self.regno="9876"
    def display(self):
        print("Name of the student: ",self.name)
        print("Register number: ",self.regno)

s1=student()
s2=student()
s1.name="sri"
s1.regno="1234"
s2.name="ram"
s2.regno="5678"
print(s1.name)
print(s1.regno)
s1.display()
s2.display()'''

#Example 2

'''class fruit:
    def __init__(self,col,nam):
        self.name=nam
        self.colou=col
    def colour(self):
        print("Name of the fruit: ",self.name,"\nColour of the fruit: ",self.colou)

apple=fruit("red","Apple") #red is the colour and apple is the name send in an argument
mango=fruit("Yellow","Mango")
orange=fruit("Orange","Orange")
apple.colour()
orange.colour()'''

#Example 3

'''class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self,sub):
        subject=sub
        print("Name of the teacher: ",self.name)
        print("Register number: ",self.regno)
        print("Subject: ",subject)

t1=teacher("sri",123)
t2=teacher("ram",456)
t1.display("science")
t2.display("Maths")'''

#Example 4

'''class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("Addition:       ",self.num1+self.num2)
    def sub(self):
        print("Subtraction:    ",self.num1-self.num2)
    def mul(self):
        print("Multiplication: ",self.num1*self.num2)
    def div(self):
        print("Division:       ",self.num1/self.num2)

def sol():
    print("--------------------------------------")
    obj1.add()
    obj1.sub()
    obj1.mul()
    obj1.div()
num1=int(input("Enter first number:  "))
num2=int(input("Enter second number: "))
obj1=calculator(num1,num2)
sol()'''

'''//////////////////////////type of class methods/////////////////////////////'''
'''class lap:
    chargertype="Ctype"
    def __init__(self,name):
        self.name=name
        self.price=34
    def setprice(self,price):
        self.price=price
    @classmethod
    def chartyp(typ):
        typ.charger="USB"
        print("Type of charger:     ",typ.charger)
    def display(self):
        print("Name of the laptop:  ",self.name)
        print("Price of the laptop: ",self.price)
        print("Type of charger:     ",self.chargertype)
    @staticmethod
    def infer():
        print("This is a static method")
   
     
hp=lap("HP")
hp.setprice(20000)
hp.display()
lap.chartyp()
hp.infer()'''



