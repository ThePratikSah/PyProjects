import cmath

a = 7
b = 8
c = -11

d = (b**2) - (4 * a * c)

sol1 = (-b + cmath.sqrt(d)) / (2 * a)
sol2 = (-b - cmath.sqrt(d)) / (2 * a)

print(sol1, sol2)
