class Rectangle:
    """ A class of Python object that describes the properties of a rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
       

    def __repr__(self):
        return "Rectangle(width={w}, height={h}, center={c})".format(h=self.height,
                                                                     w=self.width)

    def compute_area(self):
        return self.width * self.height
      
      
# Creating Square, a subclass of Rectangle
class Square(Rectangle):
    def __init__(self, width, height):
        # equivalent to `Rectangle.__init__(self, width, height)`
        super().__init__(width, height)   
