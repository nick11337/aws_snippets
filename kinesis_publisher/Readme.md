<h1>Kinesis Publisher</h1>
Class to publish events to a kinesis stream. 

**DON'T FORGET TO GIVE THE RIGHT PERMISSIONS TO THE LAMBDA**

<hr>

***How to use:***
1. Import the class KinesisPublisher and the function kinesis_publisher
```py
 from kinesis import KinesisPublisher, kinesis_publisher
 ```
2. Initiate the class with the function kinesis_publisher()
```py
kinesis_publish = kinesis_publisher()
```
3. Use the class-function publish() with your parameters
```py
kinesis_publish.publish(data=example_dictionary, partition_key=partition_key, stream_name=STREAM_NAME)
```
