import numpy as np
import random


class MatrixOperation:
    def __init__(self, n_rows, n_cols, operation):
        self.a = []
        self.b = []
        self.result = []
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.operation = operation

    def generate_values(self, is_random=True):
        for i in range(self.n_rows):
            row = []
            for j in range(self.n_cols):
                v = 1
                if is_random:
                    v = random.randint(0, 9)
                row.append(v)
            self.a.append(row)
        if self.operation == "*":
            for i in range(self.n_cols):
                row = []
                for j in range(self.n_rows):
                    v = 0
                    if is_random:
                        v = random.randint(0, 9)
                    row.append(v)
                self.b.append(row)
        if self.operation == "+":
            for i in range(self.n_rows):
                row = []
                for j in range(self.n_cols):
                    v = 0
                    if is_random:
                        v = random.randint(0, 9)
                    row.append(v)
                self.b.append(row)
        if self.operation == "s":
            for i in range(self.n_rows):
                row = []
                v = 1
                if is_random:
                    v = random.randint(0, 9)
                row.append(v)
                self.b.append(row)


    def print(self):
        print(self.a)
        print(self.b)
        print(list(self.result))

    def multiplication(self):
        self.result = list(np.dot(self.a, self.b))

    def addition(self):
        self.result = list(np.add(self.a, self.b))

    def determinant(self):
        temp = []
        temp.append(round(np.linalg.det(self.a)))
        self.result.append(temp)

    def solve(self):
        self.result = list(np.linalg.solve(self.a, self.b))

    def inverse(self):
        inv = np.linalg.inv(self.a)
        self.result = list(np.round(inv,3))

    def eigenValues(self):
        temp = []
        temp.append(np.linalg.eig(self.a)[0])
        for i in range(len(temp)):
            self.result.append(temp[i])

    def eigenVectors(self):
        eigVec = np.linalg.eig(self.a)[1]
        self.result = list(np.round(eigVec,3))

"""
mo = MatrixOperation(2, 2, "s")
mo.generate_values(True)
mo.solve()
# mo.addition()
# mo.multiplication()
# mo.determinant()
mo.print()
"""