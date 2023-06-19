import json
from quicknii_to_locare_utilities import create_locare_dict_from_alignments
######## CHANGE THESE VARIABLES:

file_path = r"/home/harryc/Github/DeMBA_scripts/LocareJSON/datasets/Quint_jsons/"
file = "H108_Timm_Nissl_coronal"
linked_dataset = ""
file_name = file + ".json"

QuickNII_json = open(file_path + file_name)

data = json.load(QuickNII_json)

locare_dict = create_locare_dict_from_alignments(data, linked_dataset)


with open(file_path + file + "_locareJSON-newtest.json", "w") as outfile:
    json.dump(locare_dict, outfile, indent=4)
    
    
    