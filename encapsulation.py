class company():
    def __init__(self):
        self.__companyname="google" #__ private variable only has assecc inside class
    def companyname(self):
        print(self.__companyname)
c1=company()
c1.companyname()
#print(c1.__companyname)
