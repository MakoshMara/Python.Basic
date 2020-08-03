class Complex:
    def __init__(self,real, complex):
        self.real = real
        self.complex = complex

    def __str__(self):
        return f'{self.real} + {self.complex}i'

    @classmethod
    def set_param(cls, user_str):
        user_str = user_str.split()
        real = int(user_str[0])
        complex = int(user_str[2][:-1])
        return cls(real, complex)

    def __add__(self, other):
        return Complex(self.real + other.real, self.complex + other.complex)

    def __mul__(self, other):
        return Complex((self.real*other.real - self.complex*other.complex),(self.real*other.complex + self.complex*other.real))


complex_1 = Complex.set_param(input('Введите комплексное число в формате a + bi:'))
complex_2 = Complex.set_param(input('Введите второе комплексное число в формате a + bi:'))
print(complex_1 * complex_2)