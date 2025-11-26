
class Rectangle:
    """ 
    class that represents a rectangle
    It provides methods to calculate the area and the perimeter
    """
    def __init__(self, width, length):
        """
        Args : 
            width : the width of the rectangle
            length : the length of the rectangle
        """
        self.width = width
        self.length = length

    def calculate_area(self) :
        """ return the area """
        return self.width * self.length

    def calculate_perimeter(self) :
        "return the perimeter"
        return 2 * (self.width + self.length)


# Test de la classe Rectangle
rectangle = Rectangle(5, 3) # 5:width & 3:length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
