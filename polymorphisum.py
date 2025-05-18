'''def add(a,b):
    print(a+b)

add(10,20)'''

'''def add(a,b,c=0):
    print(a+b+c)

add(10,20,30)
add(10,20)'''

'''class animal:
    def sound(self):                   
        print("Aminal makes sound")          
class dog(animal):
    def sound(self):
        print("Dog barks")
class bird(animal):
    def sound(self):
        print("Bird chirps")

d1=dog()
d1.sound()
b1=bird()
b1.sound()'''

#Example 1

'''class shape:
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        return l*b
    
#s1=shape()
#print(s1.area())
r1=rectangle()
print(r1.area())'''

#Example 2

'''class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade=0):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print("Name :",self.name,"\nGrade:",self.grade)

s1=student("john","A")
s1.display()'''

#Example 3 

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print("Name       :",self.name,"\nsalary     :",self.salary,"\nDepartment :",self.department)

e1=manager("sri",100000,"Admin")
e1.display()
