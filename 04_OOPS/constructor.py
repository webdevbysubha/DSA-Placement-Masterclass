class Student:
  def __init__(self,name,roll,marks):
    self.name = name
    self.roll = roll
    self.marks = marks

  def show(self):
      print(f"Name = {self.name}, Roll = {self.roll}, Marks = {self.marks}")
      print("-----------------------------------------------")

s1 = Student("Subha",104,50)
s1.show()
s2 = Student("Ritu",158,100)
s2.show() 
s3 = Student("ABC",117,95)
s3.show()