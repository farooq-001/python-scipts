import os
import json

def split_json_file(input_file, num_parts):
    # Get the size of the input file
    total_size = os.path.getsize(input_file)
    
    # Determine the size of each chunk
    chunk_size = total_size // num_parts
    
    file_num = 1
    buffer = []
    buffer_size = 0

    def write_chunk(buffer, file_num):
        with open(f'winevent-{file_num}.json', 'w') as outfile:
            json.dump(buffer, outfile)
        print(f'Created winevent-{file_num}.json with {len(buffer)} entries.')

    with open(input_file, 'r') as infile:
        for line in infile:
            json_line = json.loads(line.strip())
            buffer.append(json_line)
            buffer_size += len(json.dumps(json_line))

            if buffer_size >= chunk_size:
                write_chunk(buffer, file_num)
                buffer = []
                buffer_size = 0
                file_num += 1

        # Write remaining buffer if any
        if buffer:
            write_chunk(buffer, file_num)
################
#  inpu file   #
################
input_file = 'winevent-2024-07.json'
num_parts = 4  # Specify the number of parts you want to split the file into

split_json_file(input_file, num_parts)
