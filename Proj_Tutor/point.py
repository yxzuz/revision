class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self,x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self,y):
        self.y = y

    def is_on_x_axis(self):
        return self.y == 0

    def is_on_y_axis(self):
        return self.x == 0

    def translate(self, distX, distY):
        self.x += distX
        self.y += distY

    def __str__(self):
        return f'({self.x}, {self.y})'