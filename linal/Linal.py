import numpy as np
from numpy import linalg

I = int(input("Введите количество строк:"))
J = int(input("Введите количество столбцов:"))

print("Введите записи в одну строку (разделенную пробелом): ")

matrix1 = list(map(int, input().split()))
matrix2 = list(map(int, input().split()))    

matrix1 = np.array(matrix1).reshape(I, J)
matrix2 = np.array(matrix2).reshape(I, J)
matrix = matrix1 - matrix2
transMatrix = matrix.T
multMatrix = transMatrix.dot(matrix)

w,v = linalg.eig(multMatrix)
for i in range(len(w)):
		w[i] = w[i] ** 0.5

print("Разность А-В = С \n", matrix)
print("Матрица С транспонированная \n", transMatrix)
print("Произведение транспонированной на изначальную \n", multMatrix)
print("Cпектральное расстояние " + str(min(w)))

