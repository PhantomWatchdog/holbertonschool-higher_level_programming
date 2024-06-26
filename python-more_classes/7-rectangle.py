#!/usr/bin/python3
"""
This is the "1-rectangle" module.
"""


class Rectangle:
    """
    This is the Rectangle class.

    It represents a rectangle with a width and height attributes.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with a given width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.

        return: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        If either the width or height is 0, an empty string is returned.
        Otherwise, a string is generated with '#' characters representing
        the width of the rectangle, repeated for the height of the rectangle.

        Returns:
            str: A string representation of the Rectangle object.
        """
        result = []
        if self.width == 0 or self.height == 0:
            return ""
        for _ in range(self.height):
            result.append(str(self.print_symbol) * self.width)
        return "\n".join(result)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object.

        The returned string includes the width and
        height of the Rectangle object.

        Returns:
            str: A string representation of the Rectangle object.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor method for the Rectangle class.

        Prints a farewell message and decrements
        the number_of_instances attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
