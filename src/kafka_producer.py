import json

from kafka import KafkaProducer

from config import BOOTSTRAP_SERVER, TOPIC, INPUT_FILE, COMPRESSION_TYPE, LINGER_MS, BATCH_SIZE


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def string_serializer(data):
    return str(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER,
                         value_serializer=json_serializer, key_serializer=string_serializer,
                         compression_type=COMPRESSION_TYPE, linger_ms=LINGER_MS, batch_size=BATCH_SIZE)


if __name__ == "__main__":
    message_key = 0
    with open(INPUT_FILE, "r") as file_handle:
        for line in file_handle:
            producer.send(topic=TOPIC, value=line, key=message_key)
            message_key = message_key+1

    # Wait until all async messages are sent
    producer.flush()
