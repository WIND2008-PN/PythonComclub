class Student:
    def __init__(self, firstname, lastname, age, courses, pocket_money):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.courses = courses
        self.pocket_money = pocket_money
        
    def display_info(self):
        print("Name:", self.firstname, self.lastname)
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("Pocket Money:", self.pocket_money)
        print("-" * 20)
        
    def __str__(self):
        return f"Name: {self.firstname}{self.lastname},  Age: {self.age}, Courses: {', '.join(self.courses)}, Pocket Money: {self.pocket_money}"
    


student1 = Student("Alice" ,"Arai", 20, ["Math", "English"], 50)
student2 = Student("Bob" ,"Roini", 22, ["Physics", "History"], 30)

student1.display_info()
student2.display_info()