class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return '\n'.join(['  '.join([str(j) for j in i]) for i in self.matr])

    def __add__(self, other):
        for i in range(len(self.matr)):
            for i_2 in range(len(other.matr[i])):
                self.matr[i][i_2] = self.matr[i][i_2] + other.matr[i][i_2]
        return Matrix.__str__(self)


my_matrix_1 = Matrix([[1, 2, 3], [1, 2, 3]])
my_matrix_2 = Matrix([[2, 2, 2], [2, 2, 2]])
print(my_matrix_1 + my_matrix_2)