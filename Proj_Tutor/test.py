from hidding import *
from point import Point
import math
###1. Test Private Attributes -----------------------------------------------
demo = Demo()

# demo._b=9
# print(demo.a) # freely accessible
# print(demo._b) # still accessible, as long as you know what you are doing
# print(demo.__c) # not accessible

###2. Test Getter/Setter Methods ---------------------------------------------
r = Rectangle(Point(3, 4), 5, 6)

# r.corner # the corner attribute is no longer directly accessible
# r.__corner # the __corner attribute is private, which is also inaccessible

r.get_corner() # use a getter method to read __corner
r.get_width() # use a getter method to read __width
r.set_width(300) # use a setter method to update __width
r.get_width()

# print(r.get_width())

###3. Test Property Decorator ---------------------------------------------
r = Rectangle2(Point(32, 42), 52, 62)
# r.width # get the width
# r.width = -6.5
# r.height = "aa"
# print(r.width)
# print(r.height)
#
help(Rectangle2)

