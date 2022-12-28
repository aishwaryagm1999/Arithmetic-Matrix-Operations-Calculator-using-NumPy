#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:



def TwoMatrixBasicArithmetic(operation1):

    print()

    print("[Enter details of Matrix A and Matrix B]")
    print("[The matrices must have the same shape]")


    r1= int(input("Enter number of rows for Matrix A and Matrix B: "))
    c1 = int(input("Enter number of columns for Matrix A and Matrix B: "))
    q1 = r1*c1 #number of elements in matrix A and matrix B

    a1 = [] 
    print("Enter the elements of Matrix A: ")
    for i in range(0,q1):
        a1.append(int(input()))
    A = np.array(a1)
    A = A.reshape(r1,c1)
    print("Matrix A: \n", A)
    print()


    b1 = [] 
    print("Enter the elements of Matrix B: ")
    for i in range(0,q1):
        b1.append(int(input()))
    B = np.array(b1)
    B = B.reshape(r1,c1)
    print("Matrix B: \n", B)
    print()

    if operation1 == 1:
        print("Addition of Matrix A and Matrix B: \n")
        add = A+B
        print(add)
        
    elif operation1 == 2:
        print("Subtraction of Matrix A and Matrix B: \n")
        sub = A-B
        print(sub)
    
    elif operation1 == 3:
        print("Multiplication of Matrix A and Matrix B: \n")
        mul = A*B
        print(mul)
    
    elif operation1 == 4:
        print("Division of Matrix A and Matrix B: \n")
        div = A/B
        print(div)
    
    else:
        print("Invalid operation")


# In[3]:


def DotMatrixMultiplication():

    print()

    print("[Enter details of Matrix A and Matrix B]")
    print("[The matrices must either have the same shape or have the number of columns in Matrix A equal to the number of rows in Matrix B]")


    r1= int(input("Enter number of rows for Matrix A: "))
    c1 = int(input("Enter number of columns for Matrix A: "))
    q1 = r1*c1 #number of elements in matrix A
    a1 = [] 
    print("Enter the elements of Matrix A: ")
    for i in range(0,q1):
        a1.append(int(input()))
    A = np.array(a1)
    A = A.reshape(r1,c1)
    print("Matrix A: \n", A)
    print()


    r2= int(input("Enter number of rows for Matrix B: "))
    c2 = int(input("Enter number of columns for Matrix B: "))
    q2 = r2*c2 #number of elements in matrix B
    
    if c1 !=r2:
        return print("The number of columns in Matrix A is not equal to the number of rows in Matrix B")
    
    b1 = [] 
    print("Enter the elements of Matrix B: ")
    for i in range(0,q2):
        b1.append(int(input()))
    B = np.array(b1)
    B = B.reshape(r2,c2)
    print("Matrix B: \n", B)
    print()

    print("Dot Matrix Multiplication of Matrix A and Matrix B: \n")
    print(A.dot(B))
    
    


# In[4]:


def OneMatrixArithmetic(operation2):

    print()

    print("[Enter details of the Matrix]")


    r1= int(input("Enter number of rows: "))
    c1 = int(input("Enter number of columns: "))
    q1 = r1*c1 #number of elements in the matrix

    a1 = [] 
    print("Enter the elements of the Matrix: ")
    for i in range(0,q1):
        a1.append(int(input()))
    A = np.array(a1)
    A = A.reshape(r1,c1)
    print("Matrix: \n", A)
    print()


    if operation2 == 1:
        ele = int(input("Enter the element for addition with the Matrix: "))
        print("Addition of the Matrix with ",ele, ": \n")
        add = A+ele
        print(add)
        
    elif operation2 == 2:
        ele = int(input("Enter the element for subtraction with the Matrix: "))
        print("Subtraction of the Matrix with ",ele, ": \n")
        sub = A-ele
        print(sub)
    
    elif operation2 == 3:
        ele = int(input("Enter the element for multiplication with the Matrix: "))
        print("Multiplication of the Matrix with ",ele, ": \n")
        mul = A*ele
        print(mul)
    
    elif operation2 == 4:
        ele = int(input("Enter the element for division with the Matrix (Non-Zero value for Denominator): "))
        print("Division of the Matrix with ",ele, ": \n")
        div = A/ele
        print(div)
        
    elif operation2 == 5:
        print("Sqaure Root of the Matrix: \n")
        sqr = np.sqrt(A)
        print(sqr)
        
    elif operation2 == 6:
        ele = int(input("Enter the element for Power with the Matrix: "))
        print("Power of the Matrix with ",ele, ": \n")
        pows = A**ele
        print(pows)
        
    elif operation2 == 7:
        print("Sum of all the Matrix Elements: \n")
        sum1 = np.sum(A)
        print(sum1)
        print("Sum of all the Matrix Elements Rowwise: \n")
        sum2 = np.sum(A,axis = 1)
        print(sum2)
        print("Sum of all the Matrix Elements Columnwise: \n")
        sum3 = np.sum(A,axis = 0)
        print(sum3)
        
    elif operation2 == 8:
        print("Maximum Element of the Matrix: \n")
        maxs = A.max()
        print(maxs)
        
    elif operation2 == 9:
        print("Minimum Element of the Matrix: \n")
        mins = A.min()
        print(mins)
        
    elif operation2 == 10:
        print("Transpose of the Matrix: \n")
        tra = A.transpose()
        print(tra)
        
    elif operation2 == 11:
        print("Inverse of the Matrix: \n")
        invs = np.linalg.inv(A)
        print(invs)
    
    else:
        print("Invalid operation")
    


# In[ ]:


#Main Function

print("Arithmetic Matrix Operations calculator using NumPy")
print()
x = True
while(x!=False):
    op = int(input("Enter the Operations Category number to access Calculator: \n 1. Arithmetic Operations for 2 Matrices (same shape)   2. Dot Matrix Multiplication   3. Arithmetic Operations for 1 Matrix   4. Exit: "))

    if op == 1:
        x2 = True
        while(x2!=False):
            print()
            print("Matrix Arithmetic Operations for 2 Matrices (Same Shape)")
            operation1 = int(input("Enter the corresponding operation number for computation: \n 1. Addition  2. Subtraction  3. Multiplication  4. Division  5. Exit: "))
            if operation1 == 5:
                x2 = False
            else:
                TwoMatrixBasicArithmetic(operation1)
    
    elif op == 2:
        print()
        print("Dot Matrix Multiplication for 2 Matrices")
        DotMatrixMultiplication()
    
    elif op == 3:
        x3 = True
        while(x3!=False):
            print()
            print("Matrix Arithmetic Operations for 1 Matrix")
            operation2 = int(input("Enter the corresponding operation number for computation: \n 1. Addition  2. Subtraction  3. Multiplication  4. Division  5. Square Root  \n 6. Power  7. Sum of All Elements  8. Maximum Element Value  9. Minimum Element Value  10. Transpose  11. Inverse  12. Exit: "))
            if operation2 == 12:
                x3 = False
            else:
                OneMatrixArithmetic(operation2)
        
    elif op == 4:
        x = False
    
    else:
        print("Invalid operation")


# In[ ]:




