#solve the quadratic equation ax**2+bx+c = 0

#import complex math module
import cmath

a = 1
b = 6
c = 7

#calculate the diccriminant
d = (b**2) - (4*a*c)

#find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
