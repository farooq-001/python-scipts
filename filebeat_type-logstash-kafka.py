import subprocess
import logging

# Set up logging configuration
logging.basicConfig(filename='/home/farooq/logstash-kafka.log', level=logging.DEBUG)

def produce_to_kafka(input_file_paths, topic_names):
    """
    Produces data to Kafka topics from specified input files.

    Parameters:
    - input_file_paths (list): List of input file paths.
    - topic_names (list): List of Kafka topic names corresponding to input files.
    """
    for input_file_path, topic_name in zip(input_file_paths, topic_names):
        # Command to run Kafka console producer
        cmd_produce = [
            '/home/farooq/kafka_2.12-3.6.1/bin/kafka-console-producer.sh',
            '--topic',
            topic_name,
            '--bootstrap-server',
            'localhost:9092'
        ]
        try:
            with open(input_file_path, 'r') as f:
                subprocess.run(cmd_produce, stdin=f)
            logging.info(f'Produced data from {input_file_path} to Kafka topic {topic_name} successfully.')
        except Exception as e:
            logging.error(f'Error producing data to Kafka: {e}')

def consume_from_kafka(input_file_paths, topic_names, logstash_host, logstash_port, output_file_path):
    """
    Consumes data from Kafka topics, processes with Logstash, and writes to an output file.

    Parameters:
    - input_file_paths (list): List of input file paths.
    - topic_names (list): List of Kafka topic names corresponding to input files.
    - logstash_host (str): Logstash host for processing.
    - logstash_port (str): Logstash port for processing.
    - output_file_path (str): Output file path for writing processed data.
    """
    for input_file_path, topic_name in zip(input_file_paths, topic_names):
        # Command to run Kafka console consumer
        cmd_consume = [
            '/home/farooq/kafka_2.12-3.6.1/bin/kafka-console-consumer.sh',
            '--topic',
            topic_name,
            '--bootstrap-server',
            'localhost:9092',
            '--from-beginning'
        ]

        try:
            # Run Kafka consumer and pipe the output to Logstash
            kafka_process = subprocess.Popen(cmd_consume, stdout=subprocess.PIPE)

            # Run Logstash with Kafka input and output to stdout and TCP
            logstash_cmd = [
                'logstash',
                '-e', f'input {{"kafka" => {{"bootstrap_servers" => "localhost:9092", "topics" => ["{topic_name}"]}}}}',
                '-e', f'output {{"stdout" => {{"codec" => "json"}}}}',
                '-e', f'output {{"tcp" => {{"host" => "{logstash_host}", "port" => {logstash_port}}}}}'
            ]

            logstash_process = subprocess.run(logstash_cmd, stdin=kafka_process.stdout)
            # Wait for the Logstash process to finish
            logstash_process.wait()

            logging.info(f'Consumed data from Kafka topic {topic_name} and processed with Logstash successfully.')
        except Exception as e:
            logging.error(f'Error consuming data from Kafka and processing with Logstash: {e}')

if __name__ == "__main__":
    # Example input paths and topic names
    input_file_paths = ['/var/log/syslog', '/var/log/auth.log', '/var/log/dmesg']
    topic_names = ['SYSLOG-01', 'AUTH-02', 'DMESG-03']
    
    # Logstash configuration
    logstash_host = 'localhost'
    logstash_port = '9092'  
    
    # Output file path for processed data
    output_file_path = '/home/farooq/Desktop/outputfile.log'

    try:
        # Produce data to Kafka
        produce_to_kafka(input_file_paths, topic_names)
        
        # Consume data from Kafka, process with Logstash, and write to output file
        consume_from_kafka(input_file_paths, topic_names, logstash_host, logstash_port, output_file_path)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

