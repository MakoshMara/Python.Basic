class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position.capitalize()
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = ' '.join([self.name, self.surname])
        print(full_name)

    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get('bonus')
        print(total_income)


position_1 = Position('вася', 'пупкин', 'менеджер', 50000, 50)
position_1.get_full_name()
position_1.get_total_income()
