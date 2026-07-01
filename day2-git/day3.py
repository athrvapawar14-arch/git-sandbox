"""
class Dog:
    species = "canine"

d1 = Dog()
d2 = Dog()

d1.species = "wolf"

print(d1.species)
print(d2.species)
print(Dog.species)

The first print will give us wolf.
As would 2nd and 3rd prints. 
the class variables are shared by all the object/instances.
here we did not use constructor __init__ and self for the object instances.
Hence i can conclude that species is a class variable. 
Normally we need to do call.class_variable_name for accesing class variable.
But we can also access them using the respective objects.


"""

class Student:
    
    # Instance Variables
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance Methods

    def average(self):

        n = len(self.marks)
        tot = 0 
        for i in range(n):
            tot = tot + self.marks[i]

        return tot/n


    def highest(self):

        a = self.marks[0]
        n = len(self.marks)

        for i in range(n):
            if a >= self.marks[i]:
                i = i + 1

            else:
                a = self.marks[i]
        
        return a

    def result(self):
        avg = self.average() # not sure here cause i don't know how methods call each other in class
        if avg >= 40:
            return 'Pass' 
        else:
            return 'Fail'

        pass



    