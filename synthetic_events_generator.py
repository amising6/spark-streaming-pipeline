import json, random, time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
for i in range(10):
    event = {"user_id": i, "event": "feature_use", "timestamp": time.time()}
    producer.send('events', event)
    print("Sent:", event)
