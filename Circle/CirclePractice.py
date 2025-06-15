# 🔵 Practice: Circle Touch Checker (OOP)
# Goal: Create a Circle class and write methods to check if two circles touch or overlap

# 👉 Step 1: Define your Circle class
# - It should store x, y, and radius
# - Write a method `touches()` that takes another Circle and returns True if the circles touch or overlap
# - You can calculate distance using:
#   distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

class Circle:
    # TODO: Write your constructor here
    # def __init__(...):

    def touches(self, other):
        # TODO: Calculate distance between centers
        # Compare to sum of radii
        pass

    def overlaps(self, other):
        # TODO: Return True only if the circles overlap (not just touch)
        pass

# 🧪 Step 2: Try it out
c1 = Circle(0, 0, 5)
c2 = Circle(6, 0, 4)
c3 = Circle(20, 0, 1)

print("c1 touches c2:", c1.touches(c2))  # Expect True
print("c1 touches c3:", c1.touches(c3))  # Expect False
print("c1 overlaps c2:", c1.overlaps(c2))  # Expect True
print("c1 overlaps c3:", c1.overlaps(c3))  # Expect False