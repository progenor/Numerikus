# import numpy as np

# A=[[0,2, 1],[1, -2, -3],[-1, 1, 2]]
# B=[-8, 0, 3]
# l=[[0, 0, 0],[0, 0, 0],[0, 0, 0]]
# print(f"csere elott:\n {np.array(A)}")

# #Sorcsere:
# csere=0
# for z in range(len(A)-1):
#   if(A[z][z]==0):
#     if(A[z+1][z]!=0):
#       for ch in range(len(A)):
#         A[z][ch],A[z+1][ch] =A[z+1][ch], A[z][ch]
#         B[z],B[z+1] = B[z+1], B[z]
#       csere=csere+1
# print(csere)

# print(f"A csere utan:{A}")

# for k in range (len(A)-1):
#   for i in range(k+1, len(A)):
#     l[i][k]=(A[i][k]/A[k][k])
#     B[i]=(B[i]-l[i][k]*B[k])
#     for j in range (k, len(A)):
#       A[i][j]=A[i][j]-l[i][k]*A[k][j]

# print(f"A haromszoges matrix{A}")
# print(f"Az uj megoldasok:{B}")
# print(f"Mivel osztottunk:{l}")

# #visszahelyettesites

# X=[0,0,0]

# X[len(X)-1]=B[len(B)-1]/A[len(A)-1][len(A)-1]

# for i in range (len(A)-2, -1, -1):
#   s=0
#   for j in range(i+1, len(A)):
#     s=s+A[i][j]*X[j]
#   X[i]=((B[i]-s)/A[i][i])

# print(f"A megoldasok:{X}")


# #determinans:
# print(csere)
# if(csere%2==0):
#   sum=1
# else:
#   sum=-1
# for i in range(len(A)):
#   sum=sum*A[i][i]



# print(f"a matrix determinansa: {sum}")


import numpy as np

def gaussian_elimination(A, b):
    """
    Solves a system of linear equations using Gaussian elimination with partial pivoting.
    
    Parameters:
        A: coefficient matrix
        b: right-hand side vector
    
    Returns:
        x: solution vector
        det: determinant of A
    """
    # Convert inputs to numpy arrays if they aren't already
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)
    
    # Combine A and b for augmented matrix operations
    Ab = np.column_stack((A, b)) 
    
    # Track row swaps for determinant calculation
    swaps = 0
    
    # Forward elimination with partial pivoting
    for k in range(n-1):
        # Find pivot (max element in current column)
        pivot_row = k + np.argmax(abs(Ab[k:, k]))
        
        # Swap rows if needed
        if pivot_row != k:
            Ab[[k, pivot_row]] = Ab[[pivot_row, k]]
            swaps += 1
        
        # Skip if pivot is zero (matrix is singular)
        if abs(Ab[k, k]) < 1e-10:
            print("Warning: Matrix appears to be singular")
            return None, 0
        
        # Eliminate entries below pivot
        for i in range(k+1, n):
            factor = Ab[i, k] / Ab[k, k]
            Ab[i, k:] -= factor * Ab[k, k:]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.sum(Ab[i, i+1:n] * x[i+1:])) / Ab[i, i]
    
    # Calculate determinant
    det = (-1) ** swaps
    for i in range(n):
        det *= Ab[i, i]
    
    return x, det

# Test with the example from the original code
A = [[0, 2, 1], [1, -2, -3], [-1, 1, 2]]
b = [-8, 0, 3]

solution, determinant = gaussian_elimination(A, b)

print("Coefficient matrix:")
print(np.array(A))

print("\nRight-hand side:")
print(b)

print("\nSolution:")
print(solution)

print("\nDeterminant:")
print(determinant)

# Verify solution
A_np = np.array(A)
b_np = np.array(b)
verification = np.allclose(np.dot(A_np, solution), b_np)
print("\nSolution verification:", verification)

# Compare with numpy's built-in solver
np_solution = np.linalg.solve(A_np, b_np)
print("\nNumPy's solution:")
print(np_solution)

np_det = np.linalg.det(A_np)
print("\nNumPy's determinant:")
print(np_det)