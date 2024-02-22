import json
import yaml
import os

# Path to JSON file change it source
json_file_path = '/home/farooq/fb62d790-301d-44f7-b35c-72b3507533a8.json'

# Path to save YAML file change it destination
yml_file_path = '/home/farooq/' + os.path.basename(json_file_path).replace('.json', '.yml')

# Load JSON data
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Convert to YAML
with open(yml_file_path, 'w') as yml_file:
    yaml.dump(data, yml_file)

print("Conversion completed.")
