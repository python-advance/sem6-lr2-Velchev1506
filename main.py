import numpy as np

def calc_matrix(x,y):
 
 print('Матрица A = [{A}]')
 print('Матрица B = [{B}]')
 
 mult_a_b = None # A x B
    
 return mult_a_b


def  main():
 A = np.array([(1,2,3), (4,5,6), (7,8,9)])
    #print(A)
 B = np.array([(9,8,7), (6,5,4), (3,2,1)])
    #print(B)
 res = calc_matrix(A, B) 

 #res = None
 return res

 print(res())