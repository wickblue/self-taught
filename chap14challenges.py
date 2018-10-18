'''
Chapter 14: More OOP. Challenges
'''

class Square():
    square_list = []
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)
    def __repr__(self):
        return "{0} by {1}".format(self.s1, self.s1)

def equal(a, b):
    return a is b

x = Square(7)
y = Square(5)
z = Square(7)
a = x

##print(Square.square_list)

##print(x)
##print(y)

print(equal(x,y))
print(equal(x,z))
print(equal(x,a))


