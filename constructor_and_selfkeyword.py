class lap:
   
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
dell.display()
