class student:
    def __init__(self,name):
        self.name = name

    def show(self):
        print("name is: ",self.name)

ob = student("Rahul")
ob.show()