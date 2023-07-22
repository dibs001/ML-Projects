import numpy as np
A=np.array([[1,5,3],[2,1,3],[0,0,1]])
print(f"Rank Of A:{np.linalg.matrix_rank(A)}")
print("\nTrance of A:",np.trace(A))
print("\n Determinant of A:",np.linalg.det(A))
print("\n Invese of A:\n",np.linalg.inv(A))
print("\n Matrix raised to power 3:\n",np.linalg.matrix_power(A,3))