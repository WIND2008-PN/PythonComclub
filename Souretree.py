class Student:
    def __init__(self, firstname, lastname, age, courses, pocket_money, salary, tax):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.courses = courses
        self.pocket_money = pocket_money
        self.salary = salary
        self.tax = tax
        salary = 0
        
        if self.age < 18:
            salary = 15000
        elif self.age < 25:
            salary = 20000
        else:
            salary = 30000
        
        if self.courses:
            salary += 5000 * len(self.courses)
            
        self.tax = tax = 0.07 * salary
        
        pocket_money = pocket_money + salary - self.tax
        self.pocket_money = pocket_money
        
            
        self.salary = salary
        print(f"Student {self.get_fullname()} created with salary: {self.salary} EUR and pocket money: {self.pocket_money} EUR")
        
    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"
    def pocket_money_after_tax(self):
        return self.pocket_money - self.tax
        
    def display_info(self):
        print("Name:", self.get_fullname())  
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("Pocket Money:", self.pocket_money)
        print("Salary:", self.salary)
        print("Pocket Money after Tax:", self.pocket_money_after_tax())
        print("Tax:", self.tax)
        print("-" * 20)
        
    def __str__(self):
        return f"Name: {self.get_fullname()},  Age: {self.age}, Courses: {', '.join(self.courses)}, Pocket Money: {self.pocket_money} EUR, Salary: {self.salary} EUR, Tax: {self.tax} EUR"
    

student1 = Student("Alice", "Arai", 20, ["Math", "English"], 50 , 20000 , 2000)
student2 = Student("Bob", "Roini", 22, ["Physics", "History"], 30 , 20000 , 2000)

student1.display_info()
student2.display_info()