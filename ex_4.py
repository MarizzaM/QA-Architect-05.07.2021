class BaseColor:
    def __init__(self, color_name):
        self.color_name = color_name

    def __str__(self):
        return f'base_color : {self.color_name}'


class SpecificColor(BaseColor):
    def __init__(self, color_name, color_shape):
        BaseColor.__init__(self, color_name)

        self.color_shape = color_shape

    def __str__(self):
        return super().__str__() + f'\n the color shape {self.color_shape} '


sun = SpecificColor('white', 'yellow')
print(sun)

lemon = SpecificColor('lemon', 'yellow')
print(lemon)
