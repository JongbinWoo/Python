#선형대수를 python으로 표현
u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [t for t in zip(u, v, z)] #list comprehension과 zip로 vector의 합
print (result)


u = [1, 2, 3]
v = [4, 5, 6]
alpha = 2
result = [alpha *sum(t) for t in zip(u, v)] #scalr곱
print(result)

matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]
result = [[sum(row) for row in zip(*t)]
          for t in zip(matrix_a, matrix_b)] #matrix의 합

print(result)


matrix_a = [[3, 6], [4, 5]]
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a] #scalr matrix preduct

print(result)


matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)] #matrix transpose


matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]#matrix product
print(result)
