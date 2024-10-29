# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
#  Text explaining script usage
# Parameters:
#  d_l_x: x-component of origin-referenced ray direction
#  d_l_y: y-component of origin-referenced ray direction
#  d_l_z: z-component of origin-referenced ray direction
#  c_l_x: x-component offset of ray origin
#  c_l_y: y-component offset of ray origin
#  c_l_z: z-component offset of ray origin
#  ...
# Output:
#    print(l_d[0]) # x-component of intersection point
#    print(l_d[1]) # y-component of intersection point
#    print(l_d[2]) # z-component of intersection point
#
# Written by Olivia Powell
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math as m
import numpy as np

# "constants"
r_e_km = 6378.1363 # radius of the earth
e_e = 0.081819221456 # eccentricity of earth

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
d_l_x = float('nan')
d_l_y = float('nan')
d_l_z = float('nan')
c_l_x = float('nan')
c_l_y = float('nan')
c_l_z = float('nan')

# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
    ...
else:
   print(\
    'Usage: '\
    'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
   )
   exit()

# write script below this line
a = d_l_x**2 + d_l_y**2 + (d_l_z**2)/(1 - e_e**2)
b = 2*(d_l_x*c_l_x + d_l_y*c_l_y + (d_l_z*c_l_z)/(1-e_e**2))
c = c_l_x**2 + c_l_y**2 + (c_l_z**2)/(1 - e_e**2) - r_e_km**2

discr = b**2-4*a*c
if discr>=0:
    d = (-b-m.sqrt(discr))/(2*a)
    if d<0:
        d = (-b+m.sqrt(discr))/(2*a)
        l_d_x = d*d_l_x + c_l_x
        l_d_y = d*d_l_y + c_l_y
        l_d_z = d*d_l_z + c_l_z
    elif d>=0:
        l_d_x = d*d_l_x + c_l_x
        l_d_y = d*d_l_y + c_l_y
        l_d_z = d*d_l_z + c_l_z
else:
    raise ValueError # cannot have a negative determinant as the solution will not exist

l_d = [l_d_x, l_d_y, l_d_z]

print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point

        
