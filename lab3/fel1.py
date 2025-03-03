import matplotlib.pyplot as plt
import math as mt


S = 1/2
n=1

En = mt.pi/4 - 0.5 * mt.atan(n*n)- (n+1)/(2*pow(n+1, 4)+2)

while n <= 1000:
    S = S + n/(pow(n,4)+1)
    n += 1


print("S: ", S)
print("n", n)
print("En: ", En)
print("S-En: ", S-En)