class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_perimeter(self):
        return 2*(self.width + self.length)

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def calculate_perimeter(self):
        return 4*self.length
    def change_size(self, n):
        self.length += n

class Rider():
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Horse():
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider

    

a_rectangle = Rectangle(10, 30)
# print(a_rectangle.calculate_perimeter())

a_square = Square(10)
# print(a_square.calculate_perimeter())

# a_rectangle.what_am_i()
# a_square.what_am_i()

phil = Rider("Phil", 26)
george = Horse("George", "shepherd", phil)

print(george.rider.name)


    
