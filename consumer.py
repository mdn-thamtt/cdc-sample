from confluent_kafka import Consumer, KafkaException
import os
from dotenv import load_dotenv

load_dotenv()

consumer_group_id = os.getenv('DBZ_CONSUMER_GROUP_ID')
poll_timeout = 2.0 # timeout = 2s

schema = 'inventory'
topic = os.getenv('DBZ_CONNECTOR_TOPIC')
tables = ['customers', 'geom', 'orders', 'products', 'products_on_hand']

subscribe_topics = [
    "{}.{}.{}".format(topic, schema, t) for t in tables
]

consumer = Consumer({
    'bootstrap.servers': 'localhost:29092',
    'group.id': consumer_group_id,
    'auto.offset.reset': 'earliest'  # or 'latest'
})
consumer.subscribe(subscribe_topics)

try:
    print('Consumer is listening...')
    while True:
        msg = consumer.poll(poll_timeout)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            print(f"Received message: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print('Stopping consumer...')
finally:
    consumer.close()
