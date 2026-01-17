import random
rows = int(input())
cols = int(input())
matrix = [[random.choice([0, 1]) for i in range(cols)] for i in range(rows)]
print(matrix)


def connectedCell(matrix):

    if len(matrix) < 0 or len(matrix) >= 10 or len(matrix[0]) < 0 or len(matrix[0]) >= 10 : return -1

    def f(i, j, matrix):

        matrix[i][j] = 0
        f.count += 1

        for a in range(-1, 2):

            if i + a < 0 or i + a == len(matrix) : continue

            for b in range(-1, 2):

                if j + b < 0 or j + b == len(matrix[0]) or matrix[i + a][j + b] == 0 : continue
                f(i + a, j + b, matrix)

    maxregion = 0

    for i in range(len(matrix)):

        for j in range(len(matrix[0])):

            if matrix[i][j] == 0 : continue

            f.count = 0
            f(i, j, matrix)
            if f.count > maxregion : maxregion = f.count

    return maxregion

print(connectedCell(matrix))