
#to classify age of person .some basic logic of if and else is used in this code.
iclass Person:
    def __init__(self, initial_Age):
        if initial_Age < 0:
            self.age = 0
            print("This person is not valid, setting age to 0.")
        else:
            self.age = initial_Age

    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
