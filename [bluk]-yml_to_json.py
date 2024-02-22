import json
import yaml
import os
import glob

# Source directory for YAML files
source_dir = '/home/farooq/custom-yml/blu8b14096c/'

# Destination directory for JSON files
destination_dir = '/home/farooq/blu8b14096c/'

# Find all YAML files in the source directory
yaml_files = glob.glob(os.path.join(source_dir, '*.yml'))

# Iterate over each YAML file
for yaml_file_path in yaml_files:
    # Load YAML data
    with open(yaml_file_path, 'r') as f:
        data = yaml.safe_load(f)

    # Convert to JSON
    json_file_path = os.path.join(destination_dir, os.path.basename(yaml_file_path).replace('.yml', '.json'))
    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=2)

print("Conversion completed.")
