class Book :            # สร้างคลาส Book
    # สร้างเมธอด __init__ เพื่อกำหนดค่าพารามิเตอร์ที่รับเข้ามา
    def __init__(self, title, author, page, year):
        #ค่าพารามิเตอร์ที่รับเข้ามา
        self.title = title
        self.author = author
        self.page = page
        self.year = year
        
    def summary(self):
        return f"{self.title} by {self.author} ({self.year})"

    def Name(self):
        return f"Book(title='{self.title}', author='{self.author}', page={self.page} year={self.year})"
    def read(self, pages):
        if pages < 0:
            print("Cannot read a negative number of pages.")
            return
        self.page -= pages
        print(f"You read {pages} pages. Total pages read: {self.page}")

print("Book class created successfully.")
# Example usage:
# ตัวแปร = ClassName(ค่าพารามิเตอร์)
book1 = Book("Half", "Gojo satoto",100 , 1999)
book2 = Book("Best Friend Gone", "Kim jungo",123 , 2000)

print(book1.summary())
book1.read(20)
print(book2.summary())
book2.read(30)