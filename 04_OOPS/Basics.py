# name = 'panchu'
# roll = 104

# def display():
#     print(f"Name = {name}, Roll = {roll}")

# display()

class Student:
    name = 'panchu'
    roll = 104

    def display(self):
        print("Name = ", self.name)
        print("Roll No. = ", self.roll)

s1 = Student() # object creation
s1.display() # Student.display(s1)
