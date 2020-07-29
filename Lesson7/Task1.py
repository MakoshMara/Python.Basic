import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        new_str = ''
        for i in self.matrix:
            i = list(map(str, i))
            new_str = new_str + " ".join(i) + '\n'
        return new_str

    def __add__(self, other):
        """Уравниваем размерность матриц"""
        matr1 = np.array(self.matrix)
        matr2 = np.array(other.matrix)
        j = 0
        while j < max(matr1.shape[0], matr2.shape[0]) - min(matr1.shape[0], matr2.shape[0]):
            if matr1.shape[0] > matr2.shape[0]:
                other.matrix.append([0 for el in range(0, matr2.shape[1])])
                j += 1
            if matr1.shape[0] < matr2.shape[0]:
                self.matrix.append([0 for el in range(0, matr1.shape[1])])
                j += 1
        if matr1.shape[1] > matr2.shape[1]:
            for i in other.matrix:
                i.extend([0 for el in range(0, matr1.shape[1] - matr2.shape[1])])
        if matr1.shape[1] < matr2.shape[1]:
            for i in self.matrix:
                i.extend([0 for el in range(0, matr2.shape[1] - matr1.shape[1])])
        """Сложение матриц"""
        return Matrix(np.array(self.matrix) + np.array(other.matrix))


matrix_1 = Matrix([[3, 4, 5,0], [6, 7, 8, 0]])
matrix_2 = Matrix([[1, 2], [4, 5], [7, 8], [7, 8]])
print(matrix_1 + matrix_2)
