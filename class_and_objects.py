'''////////////////////////classed and objects//////////////////////////'''

'''class goa():
    name=""
    drink = ""
    def party(self): #self is used to access the class variables
        print("Let's party")
    def beach(self): #self is used to access the class variables
        print("Super beachu")

ramesh = goa()
suresh = goa()

ramesh.name="Ramesh"
ramesh.drink = "Beer"
suresh.drink = "Lemonade"
suresh.name="Suresh"
print(ramesh.name,":",ramesh.drink)
ramesh.party()
print(suresh.name,":",suresh.drink)
suresh.beach()'''

#Example

class lap():
    price=""
    ram=""
    processor=""

hp=lap()
dell=lap()
asus=lap()
hp.price = 20000
hp.ram="8GB"
hp.processor="i5"
dell.price=23000
dell.ram="8GB"
dell.processor="i7"
asus.price=18000
asus.ram="8GB"
asus.processor="i3"

print("price of hp laptop is:",hp.price)
print("ram of dell laptop is:",dell.ram)
print("processor of asus laptop is:",asus.processor)