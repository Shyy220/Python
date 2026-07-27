class MyClass:

    __privateVar = 27;

    def __privMeth(self):
        print("I'm inside class MyClass")

    def hello(self):
        print("Private Variable Value: ",MyClass.__privateVar)

foo = MyClass()
foo.hello()
foo.__privMeth


    
      