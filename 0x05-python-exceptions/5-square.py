#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """ 
    Square class defined by geometric shap
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """
        set square square area
        Return:
            the current square area (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter of size
        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size
        Args:
            size (int): size of a side of the square
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
                raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        print a square from the size using ##
        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.size):
                    print("#" * self.size)