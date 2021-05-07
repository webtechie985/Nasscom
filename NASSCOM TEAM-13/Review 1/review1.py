#Eqn = (X^3)*y-r*y(x^2)+x*y=1
#α = ((((e ^ 3) * y) + (3 * (x ^ 2) * y) - ((e ^ 2) * r * y) - (2 * e * r * x * y) + (e * y) + y) % sn)
#key = (((e^2)*y) + (3*y*(x^2))+(3*x*e*y)-(r*e*y)-(2*r*x*y)+y)


def hcfnaive(a, b):
 if (b == 0):
  return a
 else:
  return hcfnaive(b, a % b)
r = int(input("Enter the r: "))
for x in range(5, 500):
 for y in range(5, 500):
  if ((x ^ 3)*y - (((x ^ 2) * y) * r) + (y * x) == 1):
   print(x, y, r)
p = int(input("Enter the p: "))
q = int(input("Enter the q: "))
N = p * q
sn = (p - 1) * (q - 1)
h = []
for i in range(int(sn / 2), sn):
 if (hcfnaive(i, sn) == 1):
  h.append(i)
e = h[1]
alpha = ((((e ^ 3) * y) + (3 * (x ^ 2) * y) - ((e ^ 2) * r * y) - (2 * e * r * x * y) + (e * y) + y) % sn)
print(alpha)
k = (((e^2)*y) + (3*y*(x^2))+(3*x*e*y)-(r*e*y)-(2*r*x*y)+y)
M = int(input("Enter the message: "))
ct1 = ((M ** alpha) % N)
z = k % sn
ct2 = ((M ** z) % N)
print("ct-1 is: ", ct1)
print("ct-2 is: ", ct2)
l = (-e) % sn
dt = dt=((ct1)*(ct2**e)*(ct2**l))%N
print("The Decrypted message is: ", dt)
if (M == dt):
 print("The message and decrypted message are same")
else:
 print("The message and decrypted message are not same")
