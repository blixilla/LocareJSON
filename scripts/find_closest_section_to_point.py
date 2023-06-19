

import json
import numpy as np

def find_plane_equation(plane):
    """
    Finds the plane equation of a plane
    :param plane: the plane to find the equation of
    :type plane: :any:`numpy.ndarray`
    :returns: the normal vector of the plane and the constant k
    :rtype: :any:`numpy.ndarray`, float
    """
    a, b, c = (
        np.array(plane[0:3], dtype=np.float64),
        np.array(plane[3:6], dtype=np.float64),
        np.array(plane[6:9], dtype=np.float64),
    )
    cross = np.cross(b, c)
    cross /= 9
    k = -((a[0] * cross[0]) + (a[1] * cross[1]) + (a[2] * cross[2]))
    return (cross, k)


def shortest_distance_to_plane(point, plane_equation):
    """
    Returns the shortest distance from a point to a plane.
    
    Parameters
    ----------
    point : array_like
        The point to which the distance is measured. X, Y, Z coordinates.
    plane_equation : array_like
        The equation of the plane. A, B, C, D.
    
    """
    a, b, c, d = plane_equation
    x, y, z = point
    numerator = abs(a*x + b*y + c*z + d)
    denominator = np.sqrt(a**2 + b**2 + c**2)
    return numerator / denominator


locare_path = r"/home/harryc/Github/DeMBA_scripts/LocareJSON/datasets/Quint_jsons_locare/H108_Timm_Nissl_coronal_locareJSON-newtest.json"
sands_annotation_path = input("please input the path to the sands file for your point of interest: \n")

with open(locare_path) as f:
    quint_data = json.load(f)

alignments = quint_data["LocareCollection"]
alignment_resolution = quint_data["metadata"]["scale"]




with open(sands_annotation_path) as f:
    sands_data = json.load(f)

# check if units are mm
if  np.all([i['unit']['@id']=='id.link/mm' for i in sands_data["coordinates"]]):
    # convert to um
    for coord in sands_data["coordinates"]:
        coord['unit']['@id'] = 'id.link/um'
        coord['value'] *= 1000





coord_xyz = np.array([i['value'] for i in sands_data["coordinates"]])
coord_xyz += np.array([268 * 39,623 * 39,248 * 39])
distances = []
for alignment in alignments:
    O,U,V = alignment['LocareObject']['geometry']['coordinates'][:3]
    O = np.array(O)
    U = np.array(U) - O
    V = np.array(V) - O
    plane = np.array([O,U,V]).flatten()
    cross, k = find_plane_equation(plane)
    plane_eq = np.array([cross[0], cross[1], cross[2], k])
    distances.append(shortest_distance_to_plane(coord_xyz, plane_eq))

closest_alignment = alignments[np.argmin(distances)]
print("\n----------------------------------------\nResults:\n")
print(f"The closest section is {closest_alignment['LocareObject']['properties']['name']} and can be viewed at \n {quint_data['metadata']['viewerLink']}&section={closest_alignment['LocareObject']['properties']['name']}")