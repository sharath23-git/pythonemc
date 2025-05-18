'''///////////////////////super keyword///////////////////////'''

'''class a():
    def __init__(self):
        print("A")
    def display(self):
        print("CLASS A")
class b(a):
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        super().display()
        print("CLASS B")
class c(b):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("CLASS C")

obj=c()'''