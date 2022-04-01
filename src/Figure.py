class Figure:
    def __init__(self, name, area, perimeter):
        self.name = name
        self.area = area
        self.perimeter = perimeter

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError
