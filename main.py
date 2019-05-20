import numpy as np
import threading as tg

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
    #print(A)
B = np.array([[9,8,7], [6,5,4], [3,2,1]])
    #print(B)
C = np.array([[0,0,0],[0,0,0],[0,0,0]])

def calc_matrix(a,b,i):
    for j in range(len(A)):
        C[i][j] = sum(map(lambda x,y: x*y, a[i], b[j]))

for i in range(len(A)):
    tg.Thread(target=calc_matrix, args=(A,B,i)).start()

print(C)    


"""

row1 = A[:1] # Взять первую строку матрицы A  / [1,2,3]
col1 = B[:, 0] # Взять первый столбец матрицы  / [9, 6, 3]
res1 = row1 * col1

el1_1 = sum(sum(res1))

row2 = A[:2] 
col2 = B[:, 1]
res2 = row2 * col2

el1_2 = sum(sum(res2))

row3 = A[:3]
col3 = B[:, 2]
res3 = row3 * col3

el1_3 = sum(sum(res3))

mass_list = [] 

def diagonal_el1():
    return res

def diagonal_el2():
    return el1_2

def diagonal_el3():
    return el1_3

def calc_matrix_res():
	return el1_1 * el1_2 *el1_3

t1 = tg.Thread(target = diagonal_el1,  args = (row1 , col1))
t2 = tg.Thread(target = diagonal_el2,  args = (row2 , col2))
t3 = tg.Thread(target = diagonal_el3,  args = (row3 , col3))
t4 = tg.Thread(target = calc_matrix_res,  args = (el1_1, el1_2, el1_3))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(t1)
print(t2)
print(t3)	

print(diagonal_el1)


def calc_matrix(x,y):
	return x * y

def  main():
	A = np.array([(1,2,3), (4,5,6), (7,8,9)])
    #print(A)
    B = np.array([(9,8,7), (6,5,4), (3,2,1)])
    #print(B)
    res = A + B
    return res
A = np.array([[1,2,3], [4,5,6], [7,8,9]]) 
print(A)
B = np.array([[9,8,7], [6,5,4], [3,2,1]])
print(B)
print(calc_matrix(A,B))

t1 = tg.Thread(target = calc_matrix,  args = (3, ))

t2 = tg.Thread(target = sum,  args = (3, ))
t3 = tg.Thread(target = calc_matrix,  args = (3, ))

t1.start()
row1 = A[:1] # Взять первую строку матрицы A  / [1,2,3]
col1 = B[:, 0] # Взять первый столбец матрицы  / [9, 6, 3]

res1 = row1 * col1
el1_1 = calc_matrix(row1,col1)

t2.start()
row2 = A[:2] 
col2 = B[:, 1]

res2 = row2 * col2
el1_2 = calc_matrix(row2,col2)

t3.start()
row3 = A[:3]
col3 = B[:, 2]

res3 = row3 * col3
el1_3 = calc_matrix(row3,col3)

print(el1_1)

print(el1_2)

print(el1_3)
"""