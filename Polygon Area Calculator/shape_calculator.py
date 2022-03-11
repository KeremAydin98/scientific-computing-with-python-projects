class Rectangle():

    def __init__(self, width, height):

        self.width = width

        self.height = height

    def get_area(self):

        return self.width * self.height

    def set_width(self, width):

        self.width = width

    def set_height(self, height):

        self.height = height

    def get_perimeter(self):

        return 2 * self.width + 2 * self.height

    def get_picture(self):

        for i in range(self.height):

            print("*" * self.width)


class Square(Rectangle):

    def __init__(self, side):

        super().__init__(side, side)

    def set_side(self, side):

        self.width = side

        self.height = side

    def get_diagonal(self):

        return (self.width ** 2 + self.height ** 2) ** .5