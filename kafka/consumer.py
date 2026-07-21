from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "traffic_topic",
    "transport_topic",
    "rides_topic",
    "parking_topic",
    "emergency_topic",
    "pollution_topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="smartcity-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("=" * 70)
print(" SmartCityX Kafka Consumer Started")
print("=" * 70)

for message in consumer:

    print("\n" + "=" * 70)
    print("Topic :", message.topic)
    print("=" * 70)

    for key, value in message.value.items():
        print(f"{key:20}: {value}")