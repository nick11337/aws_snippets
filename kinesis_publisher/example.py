from kinesis import KinesisPublisher, kinesis_publisher

# Create a stream in AWS and give publish permissions to e.g. a lambda function
STREAM_NAME = "TEST_STREAM"

# Create a dictionary file as a payload
example_dictionary = {
    "example1": "example2",
    "dummy2": "dummy2"
}

# Define a partition key
partition_key = "test_key"

# Initiate Kinesis_publisher() and call .publish function
kinesis_publish = kinesis_publisher()
kinesis_publish.publish(data=example_dictionary, partition_key=partition_key, stream_name=STREAM_NAME)
