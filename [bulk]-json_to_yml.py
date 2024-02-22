import json
import yaml
import os
import glob
import sys

# Check if directory name is provided as argument
if len(sys.argv) < 2:
    print("Please provide the directory name as an argument.")
    sys.exit(1)

# Directory name provided as argument
directory_name = sys.argv[1]

# Path to JSON files directory
json_files_dir = f'/home/farooq/custom/{directory_name}/'

# Path to save YAML files directory
yml_files_dir = f'/home/farooq/custom-yml/{directory_name}/'

# Find all JSON files in the directory
json_files = glob.glob(os.path.join(json_files_dir, '*.json'))

# Iterate over each JSON file
for json_file_path in json_files:
    # Load JSON data
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Convert to YAML
    yml_file_path = os.path.join(yml_files_dir, os.path.basename(json_file_path).replace('.json', '.yml'))
    with open(yml_file_path, 'w') as f:
        yaml.dump(data, f)

print("Conversion completed.")
