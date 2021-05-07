import time
import sys
start=time.time()
def hctfi(a, b):
    if (b == 0):
        return a
    else:
        return hctfi(b, a % b)
r = int(input("Enter the r: "))#z=3
for x in range(1, 1000):
    for y in range(1, 1000):
        if ((x ^ 3)*y - (((x ^ 2) * y) * r) + (y * x) == 1):
            print("Value of x is",x)
            print("Value of y is",y)
            print("Value of r is",r)
p = int(input("Enter the p: "))#p=5
q = int(input("Enter the q: "))#q=7
N = p * q
sn = (p - 1) * (q - 1)
d = []
for i in range(int(sn / 2), sn):
    if (hctfi(i, sn) == 1):
        d.append(i)
e = d[1]
alpha =  ((((e ^ 3) * y) + (3 * (x ^ 2) * y) - ((e ^ 2) * r * y) - (2 * e * r * x * y) + (e * y) + y) % sn)
print("Alpha value is",alpha)
k =  (((e^2)*y) + (3*y*(x^2))+(3*x*e*y)-(r*e*y)-(2*r*x*y)+y)
print("k value is",k)
M = int(input("Enter the data value:"))
ct1 = ((M ** alpha) % N)
z = k % sn
ct2 = ((M ** z) % N)
print("Ciphertext-1 is:", ct1)
original_stdout = sys.stdout 

with open('ct1.txt', 'w') as f:
    sys.stdout = f 
    print(ct1)
    sys.stdout = original_stdout
print("Ciphertext-2 is:", ct2)
original_stdout = sys.stdout 

with open('ct2.txt', 'w') as f1:
    sys.stdout = f1 
    print(ct2)
    sys.stdout = original_stdout
l = (-e) % sn
dt = dt=((ct1)*(ct2**e)*(ct2**l))%N
print("The decrypted message is:", dt)
if (M == dt):
    print(" Message and decrypted message are same and ciphered text values are stored")
else:
    print(" Message and decrypted message are not same and ciphered text values are stored")
end=time.time()
print(f"runtime is:{end - start}")
