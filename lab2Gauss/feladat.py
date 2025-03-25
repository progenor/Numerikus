import numpy as np

A=[[0,2, 1],[1, -2, -3],[-1, 1, 2]]
B=[-8, 0, 3]
l=[[0, 0, 0],[0, 0, 0],[0, 0, 0]]
print(f"csere elott:\n {np.array(A)}")

#Sorcsere:
csere=0
for z in range(len(A)-1):
  if(A[z][z]==0):
    if(A[z+1][z]!=0):
      for ch in range(len(A)):
        A[z][ch],A[z+1][ch] =A[z+1][ch], A[z][ch]
        B[z],B[z+1] = B[z+1], B[z]
      csere=csere+1
print(csere)

print(f"A csere utan:{A}")

for k in range (len(A)-1):
  for i in range(k+1, len(A)):
    l[i][k]=(A[i][k]/A[k][k])
    B[i]=(B[i]-l[i][k]*B[k])
    for j in range (k, len(A)):
      A[i][j]=A[i][j]-l[i][k]*A[k][j]

print(f"A haromszoges matrix{A}")
print(f"Az uj megoldasok:{B}")
print(f"Mivel osztottunk:{l}")

#visszahelyettesites

X=[0,0,0]

X[len(X)-1]=B[len(B)-1]/A[len(A)-1][len(A)-1]

for i in range (len(A)-2, -1, -1):
  s=0
  for j in range(i+1, len(A)):
    s=s+A[i][j]*X[j]
  X[i]=((B[i]-s)/A[i][i])

print(f"A megoldasok:{X}")


#determinans:
print(csere)
if(csere%2==0):
  sum=1
else:
  sum=-1
for i in range(len(A)):
  sum=sum*A[i][i]



print(f"a matrix determinansa: {sum}")