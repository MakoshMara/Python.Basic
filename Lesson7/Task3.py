class Cell:
    def __init__(self, unit):
        self.unit = unit

    def __add__(self, other):
        return Cell(self.unit + other.unit)

    def __sub__(self, other):
        return Cell(max(self.unit, other.unit) - min(self.unit, other.unit))

    def __mul__(self, other):
        return Cell(self.unit * other.unit)

    def __truediv__(self, other):
        return Cell(self.unit // other.unit)

    def make_order(self, count):
        i = 1
        new_str = ''
        while i <= self.unit // count:
            new_str = new_str + '*' * count + '\n'
            i += 1
        return new_str + '*' * (self.unit % count)

    def __str__(self):
        return str(self.unit)


cell_1 = Cell(50)
cell_2 = Cell(12)
print(cell_1.make_order(5))
