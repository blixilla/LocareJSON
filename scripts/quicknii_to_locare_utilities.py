# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:39:54 2023

@author: ingvieb
"""


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
    
    upper_left_xyz = [upper_left_x, upper_left_y, upper_left_z]
    upper_right_xyz = [upper_right_x, upper_right_y, upper_right_z]
    lower_left_xyz = [lower_left_x, lower_left_y, lower_left_z]
    lower_right_xyz = [lower_right_x, lower_right_y, lower_right_z]

    return upper_left_xyz, upper_right_xyz, lower_left_xyz, lower_right_xyz

def define_coordinate_space(target):
    if target == "WHS_Rat_v3_39um.cutlas":
        commonCoordinateSpaceVersion = "https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/WHSSD_v1.01"
        
    elif target == "ABA_Mouse_CCFv3_2017_25um.cutlas":
        commonCoordinateSpaceVersion = "https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/AMB-CCF_v3"
        
    else:
        commonCoordinateSpaceVersion = "Unknown"
    return commonCoordinateSpaceVersion

def create_locare_dict_from_alignments(data, linked_dataset=""):
    target = data["target"]
    commonCoordinateSpaceVersion = define_coordinate_space(target)
    locare_dict = {
        "type": "LocareJSON",
        "version": "0.1",
        "metadata": {
            "commonCoordinateSpaceVersion": commonCoordinateSpaceVersion,
            "linkedDataset": linked_dataset},
        "LocareCollection": []
        }
    for section in data["slices"]:
        name = section["filename"]
        name = name.split(".")[0]
        anchoring = section["anchoring"]
        upper_left_xyz, upper_right_xyz, lower_left_xyz, lower_right_xyz = calculate_corners(anchoring)

        geometry_dict = {
            "type": "Polygon",
            "coordinates": [upper_left_xyz, upper_right_xyz, lower_left_xyz, lower_right_xyz],
            }
        
        properties_dict = {
            "name": name,
            "description": "position of brain section image"
            }
        
        locareObjects_dict = {"LocareObject":
            {"geometry": geometry_dict, "properties": properties_dict}}
        
        
        locare_dict["LocareCollection"].append(locareObjects_dict)

    return locare_dict


    
    
    
    
    
    
    
    
    
    