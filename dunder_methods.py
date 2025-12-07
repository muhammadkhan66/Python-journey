#Question1
#Create a class Person with attributes name and age. Implement str so that printing the object displays:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person:\n(name: {self.name} , age: {self.age})" 
    
p = Person("Muhammad Abdul Rehman Khan", 22)
print(p)

#Question2
# Create a class Book with attributes title and author. Implement the repr method to return: "Book('', '<author>')"</p>
class Book:
    def __init__(self,title,author):
        self.author = author
        self.title = title
    def __repr__(self):
        return f"Book: {self.title}, {self.author}"
    
b = Book("Rich Dad Poor Dad", "Tim Robinson")
print(b)

#Question3
# Create a class Number with an attribute value. Implement the add method to allow adding two Number objects.
class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self,other):
        return self.value + other.value

num1 = Number(3)
num2 = Number(8)
print(num1 + num2)

#Question4
# Create a class Circle with an attribute radius. Implement the len method to return the integer value of the radius.
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def __len__(self):
        return int(self.radius)
    
cir = Circle(34)
print(len(cir))

#Question5
# Create a class Student with an attribute grades (a list). Implement getitem to allow accessing grades by index.
class Student:
    def __init__(self,grades):
        self.grades = grades
    def __getitem__(self,index):
        return self.grades[index]
    
grade = Student([89,45,23,32])
print(grade[0])
print(grade[1])
print(grade[2])
