import copy


###1. Test Private Attributes -----------------------------------------------
class Demo:
    def __init__(self):
        self.a = 1  # public
        self._b = 2  # protected
        self.__c = 3.14  # private
        self._b = self.__c*5*5

# xx = Demo()
# print(xx.__c)

###2. Test Getter/Setter Methods ---------------------------------------------
class Rectangle:
    """A class to manufacture rectangle objects."""

    def __init__(self, pos, w, h):
        """Initialize rectangle at pos, with width w, height h."""
        self.set_corner(pos)
        self.set_width(w)
        self.set_height(h)

    def get_corner(self): return self.__corner

    def set_corner(self, pos): self.__corner = copy.copy(pos)

    def get_width(self): return self.__width

    def set_width(self, w): self.__width = w

    def get_height(self): return self.__height

    def set_height(self, h): self.__height = h


###3. Test Property Decorator ---------------------------------------------
class Rectangle2:
    def __init__(self, pos, w, h):
        self.corner = pos
        self.width = w
        self.height = h

    @property
    def corner(self):
        return self.__corner

    @corner.setter
    def corner(self, pos):
        self.__corner = copy.copy(pos)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if not isinstance(w, (int, float)):
            raise TypeError("width must be a number")
        if w < 0:
            raise ValueError("width must not be negative")

        self.__width = w
        # if w < 0:
        #     print("WARNING: width must not be negative")
        #     self.__width = 0
        # else:
        #     self.__width = w

    @property
    def height(self):
        """Get the height of rectangle
        ddddd"""

        return self.__height

    @height.setter
    def height(self, h):
        self.__height = h

###4. Test NO SETTER Property Decorator ---------------------------------------------
class Effect:
    def __init__(self, text: str, mag: int):
        self.mag = mag
        self.__text = text
    @property
    def mag(self):
        return self.__mag
    @mag.setter
    def mag(self, val):
        self.__mag = val
    @property
    def text(self):
        return self.__text

    def __str__(self):
        return str(self)

