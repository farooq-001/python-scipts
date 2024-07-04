import gzip
import shutil
import os
############# NEED TO CHANGE THE  if " Authen " in line, BASED ON YOUR KEY WORD  #################


def decompress_and_filter(input_gz_path, log_file_path):
    try:
        # Step 1: Decompress the gzip file directly to a temporary location in memory
        with gzip.open(input_gz_path, 'rt') as f_in:
            # Step 2: Filter lines containing "Authen" and append them to the log file
            with open(log_file_path, 'a') as f_out:
                for line in f_in:
                    if 'Authen' in line:
                        f_out.write(line)
        print(f"Processed file: {input_gz_path}")
    except Exception as e:
        print(f"Error processing file {input_gz_path}: {e}")

def process_directory(base_dir, log_dir):
    for day in range(0, 31):  # From 00 to 31 inclusive
        day_str = f"{day:02d}"  # Format day as two digits
        day_path = os.path.join(base_dir, day_str)
        if os.path.isdir(day_path):
            for hour in os.listdir(day_path):
                hour_path = os.path.join(day_path, hour)
                if os.path.isdir(hour_path):
                    hour_str = f"{day_str}-{hour}"  # Create a unique hour-based log file name
                    for minute in os.listdir(hour_path):
                        minute_path = os.path.join(hour_path, minute)
                        if os.path.isdir(minute_path):
                            for part in os.listdir(minute_path):
                                if part.endswith('.txt.gz'):
                                    input_gz_path = os.path.join(minute_path, part)
                                    log_file_path = os.path.join(log_dir, f"{hour_str}.log")
                                    
                                    decompress_and_filter(input_gz_path, log_file_path)

base_directory = '/home/bfarooq/Downloads/rawevents/06'
log_directory = '/home/bfarooq/Downloads/rawevents-2'

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

process_directory(base_directory, log_directory)

