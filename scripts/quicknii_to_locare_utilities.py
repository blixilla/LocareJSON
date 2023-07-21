# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:39:54 2023

@author: ingvieb
"""
import numpy as np

def calculate_corners(anchoring):
    upper_left_x, upper_left_y, upper_left_z = anchoring[0:3]
    vx1, vy1, vz1 = anchoring[3:6]
    vx2, vy2, vz2 = anchoring[6:9]
    
    upper_right_x = upper_left_x + vx1
    upper_right_y = upper_left_y + vy1
    upper_right_z = upper_left_z + vz1
    
    lower_left_x = upper_left_x + vx2
    lower_left_y = upper_left_y + vy2
    lower_left_z = upper_left_z + vz2
    
    lower_right_x = upper_left_x + vx1 + vx2
    lower_right_y = upper_left_y + vy1 + vy2
    lower_right_z = upper_left_z + vz1 + vz2
    

    upper_left_xyz = np.array([upper_left_x, upper_left_y, upper_left_z])
    upper_right_xyz = np.array([upper_right_x, upper_right_y, upper_right_z])
    lower_left_xyz = np.array([lower_left_x, lower_left_y, lower_left_z])
    lower_right_xyz = np.array([lower_right_x, lower_right_y, lower_right_z])

    return upper_left_xyz, upper_right_xyz, lower_left_xyz, lower_right_xyz

def define_coordinate_space(target):
    if target.startswith("WHS"):
        targetAtlas = {
            "commonCoordinateSpaceVersion": "https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/WHSSD_v1.01",
            "coordinateSpaceSetup": {
               "dimensions": [512, 1024, 512],
               "resolution": "39um",
               "directions": ["left to right", "posterior to anterior", "ventral to dorsal"],
               "origin": [244, 623, 248]
            }
        }

        
    elif target.startswith("ABA"):
        targetAtlas = {
            "commonCoordinateSpaceVersion": "https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/AMB-CCF_v3",
            "coordinateSpaceSetup": {
               "dimensions":  [456, 528, 320],
               "resolution": "25um",
               "directions": ["left to right", "posterior to anterior", "ventral to dorsal"],
               "origin": [0, 0, 0]
            }
        }
        
    ## we assume all targets have resolution in um in the filename
    resolution = target.split("_")[-1].split("um")[0]
    # strip non numeric characters
    resolution = float(''.join(i for i in resolution if i.isdigit()))
    return targetAtlas, resolution


def create_locare_dict_from_alignments(data, source_publication, linked_dataset=""):
    target = data["target"]
    targetAtlas, resolution = define_coordinate_space(target)
    locare_dict = {
        "type": "LocareJSON",
        "version": "1.0.0",
        "metadata": {
            "targetAtlas": targetAtlas,
            "sourcePublication": source_publication,
            "linkedURI": linked_dataset},
        "LocareCollection": []
        }
    if not linked_dataset:
        del locare_dict["metadata"]["linkedURI"]

    for section in data["slices"]:
        name = section["filename"]
        name = name.split(".")[0]
        anchoring = section["anchoring"]
        upper_left_xyz, upper_right_xyz, lower_left_xyz, lower_right_xyz = [v.tolist() for v in calculate_corners(anchoring)]

        # Commenting out this - we want the original resolution
        #upper_left_xyz, upper_right_xyz, lower_left_xyz, lower_right_xyz = calculate_corners(anchoring) 
        #upper_left_xyz = (resolution * upper_left_xyz).tolist()
        #upper_right_xyz = (resolution    * upper_right_xyz).tolist()
        #lower_left_xyz = (resolution * lower_left_xyz).tolist()
        #lower_right_xyz = (resolution * lower_right_xyz).tolist()

        geometry_dict = {
            "type": "Polygon",
            "coordinates": [upper_left_xyz, upper_right_xyz, lower_left_xyz, lower_right_xyz],
            }
        
        properties_dict = {
            "name": name,
            "description": "position of brain section image"
            }
        
        locareObjects_dict = {
            "geometry": geometry_dict, "properties": properties_dict
        }
        
        
        locare_dict["LocareCollection"].append(locareObjects_dict)

    return locare_dict


    
    
    
    
    
    
    
    
    
    