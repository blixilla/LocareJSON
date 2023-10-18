import json
import sys
from urllib.parse import urlparse
from quicknii_to_locare_utilities import create_locare_dict_from_alignments

def is_valid_uri(uri):
    try:
        result = urlparse(uri)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def main(json_file_path, source_publication, linked_dataset=None):
    if not is_valid_uri(source_publication):
        print(f"Invalid URI: {source_publication}")
        sys.exit(1)

    if linked_dataset and not is_valid_uri(linked_dataset):
        print(f"Invalid URI: {linked_dataset}")
        sys.exit(1)

    file_name = json_file_path.split('/')[-1]
    file = file_name.split('.')[0]
    out_path = "/".join(json_file_path.split('/')[:-1]) + "/"

    with open(json_file_path, 'r') as QuickNII_json:
        data = json.load(QuickNII_json)

    locare_dict = create_locare_dict_from_alignments(data, source_publication, linked_dataset)

    with open(out_path + file + "_locareJSON-newtest.json", "w") as outfile:
        json.dump(locare_dict, outfile, indent=4)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <json_file_path> <source_publication> [<linked_dataset>]")
        sys.exit(1)

    json_file_path = sys.argv[1]
    source_publication = sys.argv[2]

    if len(sys.argv) > 3:
        linked_dataset = sys.argv[3]
    else:
        linked_dataset = None

    main(json_file_path, source_publication, linked_dataset)
