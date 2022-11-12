from kafka import KafkaConsumer
from config import TOPIC, BOOTSTRAP_SERVER, GROUP_ID


# To consume latest messages from the given topic and auto-commit offsets
consumer = KafkaConsumer(TOPIC,
                         group_id=GROUP_ID,
                         bootstrap_servers=BOOTSTRAP_SERVER,
                         auto_offset_reset='earliest')

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key.decode("utf-8"),
                                         message.value.decode("utf-8")))
