import random
random.seed(100)
matrix=[[random.randint(10,30) for i in range(0,5)] for o in range(0,10)]
print("原始矩阵：")
for i in matrix:
    print(i,end="\n")
trans=[[raw[i] for raw in matrix] for i in range(len(matrix[0]))]
print("转置矩阵：")
for i in trans:
    print(i,end="\n")