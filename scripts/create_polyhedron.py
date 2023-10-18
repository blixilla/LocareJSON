# -*- coding: utf-8 -*-
"""
Created on Thu July 20

@author: blixhavn, blixilla
"""

import numpy as np

# Given values
r2 = np.array([405.2, 322.5, 277.2])
r4 = np.array([405.2, 146.5, 277.2])

l = 176
alpha = 5 * np.pi / 180  # converting degrees to radians

# Calculate displacement vector
displacement = np.array([-l * np.cos(alpha), 0, l * np.sin(alpha)])

# Determine the other two corners
r1 = r2 + displacement
r3 = r4 + displacement

# Calculate unit vector normal to rectangle
un = np.cross((r3-r4), (r2-r4)) / (np.linalg.norm(r2-r4) * np.linalg.norm(r3-r4))

# Calculate angle between rectangle and xy-plane
alpha = np.rad2deg(np.arcsin(np.dot(-un, [1, 0, 0])))

# Calculate corners of cuboid with height 50
r11 = r1 + 50*un
r21 = r2 + 50*un
r31 = r3 + 50*un
r41 = r4 + 50*un


def meshprint(np_array):
    print("%s %s %s" % (np.round(np_array[0], 3), np.round(np_array[1], 3), np.round(np_array[2], 3)))

print("Unit vector: %s" % un)
print(alpha)

meshprint(r1)
meshprint(r2)
meshprint(r3)
meshprint(r4)

meshprint(r11)
meshprint(r21)
meshprint(r31)
meshprint(r41)
