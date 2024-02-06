#!/usr/bin/python3

class Square:
    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """Calculate the area of the square."""
        return self.width * self.width

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return 4 * self.width

    def __str__(self):
        return "Square(width={}, height={})".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())

