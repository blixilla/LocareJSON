# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:39:54 2023

@author: ingvieb
"""

import json


######## CHANGE THESE VARIABLES:

file_path = r"Z:\NESYS_Lab\PhD_project_Blixhavn_Camilla\Paper 2 - LocaRe\examples/"
file = "H108_Timm_Nissl_coronal"
linked_dataset = ""





file_name = file + ".json"
QuickNII_json = open(file_path + file_name)

data = json.load(QuickNII_json)


if data["target"] == "WHS_Rat_v3_39um.cutlas":
    commonCoordinateSpaceVersion = "https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/WHSSD_v1.01"
    
elif data["target"] == "ABA_Mouse_CCFv3_2017_25um.cutlas":
    commonCoordinateSpaceVersion = "https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/AMB-CCF_v3"
    
else:
    commonCoordinateSpaceVersion = "Unknown"

locare_dict = {
    "type": "LocareJSON",
    "version": "0.1",
    "metadata": {
        "commonCoordinateSpaceVersion": commonCoordinateSpaceVersion,
        "linkedDataset": linked_dataset},
    "LocareCollection": []
    }

for i in data["slices"]:
        
    name = i["filename"]
    name = name.split(".")[0]
    anchoring = i["anchoring"]
    upper_left_x = anchoring[0]
    upper_left_y = anchoring[1]
    upper_left_z = anchoring[2]
    vx1 = anchoring[3]
    vy1 = anchoring[4]
    vz1 = anchoring[5]
    vx2 = anchoring[6]
    vy2 = anchoring[7]
    vz2 = anchoring[8]
    
    upper_right_x = upper_left_x + vx1
    upper_right_y = upper_left_y + vy1
    upper_right_z = upper_left_z + vz1
    
    lower_left_x = upper_left_x + vx2
    lower_left_y = upper_left_y + vy2
    lower_left_z = upper_left_z + vz2
    
    lower_right_x = upper_left_x + vx1 + vx2
    lower_right_y = upper_left_y + vy1 + vy2
    lower_right_z = upper_left_z + vz1 + vz2
    
    upper_left_triplet = [upper_left_x, upper_left_y, upper_left_z]
    upper_right_triplet = [upper_right_x, upper_right_y, upper_right_z]
    lower_left_triplet = [lower_left_x, lower_left_y, lower_left_z]
    lower_right_triplet = [lower_right_x, lower_right_y, lower_right_z]
    
    geometry_dict = {
        "type": "Polygon",
        "coordinates": [upper_left_triplet, upper_right_triplet, lower_left_triplet, lower_right_triplet],
        }
    
    properties_dict = {
        "name": name,
        "description": "position of brain section image"
        }
    
    locareObjects_dict = {"LocareObject":
        {"geometry": geometry_dict, "properties": properties_dict}}
    
     
    locare_dict["LocareCollection"].append(locareObjects_dict)


with open(file_path + file + "_locareJSON.json", "w") as outfile:
    json.dump(locare_dict, outfile)
    
    
    
    
    
    
    
    
    
    
    
    
    