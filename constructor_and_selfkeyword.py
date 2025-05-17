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

#Example
class student:
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
s2.display()
