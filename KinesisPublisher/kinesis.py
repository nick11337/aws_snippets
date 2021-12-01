from typing import Dict, Optional
import json
import boto3


class KinesisPublisher:
    def __init__(self, client) -> None:
        self._client = client

    def publish(self, data: Dict, partition_key: str, stream_name: str):
        self._client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data, use_decimal=True),
            PartitionKey=partition_key
        )


_kinesis_publisher_cache: Optional[KinesisPublisher] = None


def kinesis_publisher() -> KinesisPublisher:
    client = boto3.client('kinesis')

    global _kinesis_publisher_cache

    _kinesis_publisher_cache = _kinesis_publisher_cache if _kinesis_publisher_cache is not None else KinesisPublisher(
        client)

    return _kinesis_publisher_cache
