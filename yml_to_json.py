import json
import yaml
import os

def yaml_to_json(yaml_file_path, json_file_path):
    with open(yaml_file_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

# Path to YAML file change it source
yml_file_path = '/home/farooq/custom-yml/blu08f44f82/fb62d790-301d-44f7-b35c-72b3507533a8.yml'

# Destination for JSON file change it destination
json_file_path = '/home/farooq/' + os.path.basename(yml_file_path).replace('.yml', '.json')

yaml_to_json(yml_file_path, json_file_path)

print("Conversion completed.")
