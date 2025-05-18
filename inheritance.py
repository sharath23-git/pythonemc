'''///////////////////////////inheritance////////////////////////'''

'''class dad():
    def phone(self):
        print("DADS PHONE")

class son():
    def lap (self):
        print("SONS LAPTOP")


    
ram=son()
ram.lap()'''

'''//////////////////single inheritance//////////////////////'''
'''class dad():
    def phone(self):
        print("DADS PHONE")


class son(dad):
    def lap (self):
        print("SONS LAPTOP")


    
ram=son()
ram.lap()
ram.phone()'''

'''//////////////////multiple inheritance//////////////////////'''

'''class dad():
    def phone(self):
        print("DADS PHONE")

class mom():
    def sweet(self):
        print("SWEETS")

class son(dad,mom):
    def lap (self):
        print("SONS LAPTOP")

    
ram=son()
ram.lap()
ram.phone()
ram.sweet()'''

'''//////////////////multilevel inheritance//////////////////////'''

'''class dad():
    def phone(self):
        print("DADS PHONE")

class mom(dad):
    def sweet(self):
        print("SWEETS")

class son(mom):
    def lap (self):
        print("SONS LAPTOP")


    
ram=son()
m1=mom()
m1.phone()
ram.lap()
ram.phone()
ram.sweet()'''

'''//////////////////hierarchical inheritance//////////////////////'''

'''class dad():
    def money(self):
        print("DADS money")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass

ram=son1()
ram.money()'''

'''//////////////////hybrid inheritance//////////////////////'''

'''class dad():
    def money(self):
        print("DADS money")
class land():
    def land(self):
        print("LAND")
class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(son1):
    pass
ram=son1()
ram.money()
ram.land()'''