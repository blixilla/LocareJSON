# -*- coding: utf-8 -*-
"""
Created on Thu July 20

@author: blixhavn
"""

def create_locarePoints_from_centroids(data, source_publication, linked_dataset=""):
    locare_dict = {
        "type": "LocareJSON",
        "version": "1.0.0",
        "metadata": {
            "targetAtlas": {
               "commonCoordinateSpaceVersion": "https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/AMB-CCF_v3-RAS",
               "coordinateSpaceSetup": {
                   "dimensions": [456, 528, 320],
                   "resolution": "25um",
                   "orientation": "RAS",
                   "origin": [0, 0, 0]
                }
            },
            "sourcePublication": source_publication,
            "linkedURI": linked_dataset},
        "LocareCollection": []
        }
    if not linked_dataset:
        del locare_dict["metadata"]["linkedURI"]


    iterator = 1
    for element in data:
        if len(element['triplets']) < 3:
            continue

        hex_color_code = "#{:02x}{:02x}{:02x}".format(element['r'], element['g'], element['b'])
        description = "{} {}".format(element['name'], hex_color_code)

        for i in range(0, len(element['triplets']), 3):
            group = element['triplets'][i:i+3]

            geometry_dict = {
                "type": "Point",
                "coordinates": group
            }
            properties_dict = {
                "name": str(iterator),
                "description": description
            }

            locareObjects_dict = {
                "geometry": geometry_dict, "properties": properties_dict
            }
            
            
            locare_dict["LocareCollection"].append(locareObjects_dict)

            iterator += 1

    return locare_dict


    
    
    
    
    
    
    
    
    
    