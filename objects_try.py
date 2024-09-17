class VGLUG:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = VGLUG('Bharathi')
p.say_hi()


# A Sample class with init method
class Sagasoft:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def welcome(self):
        print('Hello, my name is', self.name)


# Creating different objects
p1 = Sagasoft('Bharathi')
p2 = Sagasoft('Senkathir')
p3 = Sagasoft('Thamizh')
p4 = Sagasoft('Mathu')

p1.welcome()
p2.welcome()
p3.welcome()
p4.welcome()


# Python program to
# demonstrate init with
# inheritance

class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something


class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something


obj = B("Something")


# class Myvillage:
#     def __init__(self,name):
#         self.name=name

#     def mystreet(self):
#         print("welcome ",self.name)

# village_name=Myvillage("Brammadesam")

# village_name.mystreet()

class bharathi(object):
    def __init__(self, something):
        print("bharathis is called the function")
        self.something =something
class ragav(bharathi):
    def __init__(self, something):
        bharathi.__init__(self, something)
        print("ragav is called the functon")
        self.something=something

obj=ragav("somethig")



class Dog:
    def __init__(self, name, breed,age=1):
        self.name=name
        self.breed=breed
        self.age=age

dog1=Dog("Dommy","Cow",3)

print(dog1.name)
print(dog1.breed)
print(dog1.age)