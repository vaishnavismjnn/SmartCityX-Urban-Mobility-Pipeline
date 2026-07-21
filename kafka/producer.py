import json
import time
import psycopg2
from kafka import KafkaProducer
from config import DB_CONFIG, KAFKA_SERVER

# -----------------------------
# PostgreSQL Connection
# -----------------------------
conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

# -----------------------------
# Kafka Producer
# -----------------------------
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    api_version=(3, 9, 0),
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
    request_timeout_ms=30000,
    connections_max_idle_ms=60000
)

# ==========================================================
# Traffic
# ==========================================================
def stream_traffic():

    print("\nStreaming Traffic Data...\n")

    cursor.execute("""
        SELECT sensor_id,
               junction_id,
               vehicle_count,
               average_speed,
               congestion_level,
               timestamp,
               weather_condition
        FROM warehouse.fact_traffic
        LIMIT 50;
    """)

    rows = cursor.fetchall()

    for row in rows:

        message = {
            "sensor_id": row[0],
            "junction_id": row[1],
            "vehicle_count": row[2],
            "average_speed": row[3],
            "congestion_level": row[4],
            "timestamp": str(row[5]),
            "weather_condition": row[6]
        }

        # ----------------------------
        # Live Traffic Events
        # ----------------------------

        alert = ""

        if message["vehicle_count"] > 450:
            alert = "🚨 Vehicle Count Spike Detected!"

        elif message["congestion_level"] == "High":
            alert = "🚦 Congestion Alert!"

        elif message["average_speed"] < 20:
            alert = "🚑 Possible Accident Alert!"

        # Add alert to Kafka message
        message["alert"] = alert

        # Send to Kafka
        producer.send("traffic_topic", value=message)

        # Print in terminal
        print(message)

        if alert:
            print(alert)

        time.sleep(0.5)


# ==========================================================
# Transport
# ==========================================================
def stream_transport():

    print("\nStreaming Transport Data...\n")

    cursor.execute("""
        SELECT bus_id,
               route_id,
               latitude,
               longitude,
               delay_minutes,
               passenger_count,
               fuel_consumption
        FROM warehouse.fact_transport
        LIMIT 20;
    """)

    rows = cursor.fetchall()

    for row in rows:

        message = {
            "bus_id": row[0],
            "route_id": row[1],
            "latitude": row[2],
            "longitude": row[3],
            "delay_minutes": row[4],
            "passenger_count": row[5],
            "fuel_consumption": row[6]
        }

        # ----------------------------
        # Transport Events
        # ----------------------------

        alert = ""

        if message["delay_minutes"] > 10:
            alert = "⏰ Delay Update!"

        elif message["passenger_count"] > 60:
            alert = "🚌 Passenger Load Event!"

        else:
            alert = f"📍 GPS Location: ({message['latitude']}, {message['longitude']})"

        # Add alert to Kafka message
        message["alert"] = alert

        # Send to Kafka
        producer.send("transport_topic", value=message)

        # Print in terminal
        print(message)

        if alert:
            print(alert)

        time.sleep(0.5)
# ==========================================================
# Rides
# ==========================================================

def stream_rides():

    print("\nStreaming Ride Data...\n")

    cursor.execute("""
        SELECT ride_id,
               pickup_zone,
               drop_zone,
               fare,
               wait_time,
               trip_duration,
               driver_rating
        FROM warehouse.fact_rides
        LIMIT 20;
    """)

    rows = cursor.fetchall()

    for row in rows:

        message = {
            "ride_id": row[0],
            "pickup_zone": row[1],
            "drop_zone": row[2],
            "fare": row[3],
            "wait_time": row[4],
            "trip_duration": row[5],
            "driver_rating": row[6]
        }

        producer.send("rides_topic", value=message)
        print(message)
        time.sleep(0.5)


# ==========================================================
# Parking
# ==========================================================

def stream_parking():

    print("\nStreaming Parking Data...\n")

    cursor.execute("""
        SELECT parking_id,
               zone,
               occupancy,
               hourly_revenue,
               available_slots,
               peak_hour
        FROM warehouse.fact_parking
        LIMIT 20;
    """)

    rows = cursor.fetchall()

    for row in rows:

        message = {
            "parking_id": row[0],
            "zone": row[1],
            "occupancy": row[2],
            "hourly_revenue": row[3],
            "available_slots": row[4],
            "peak_hour": row[5]
        }

        producer.send("parking_topic", value=message)
        print(message)
        time.sleep(0.5)


# ==========================================================
# Emergency
# ==========================================================
def stream_emergency():

    print("\nStreaming Emergency Data...\n")

    cursor.execute("""
        SELECT incident_id,
               incident_type,
               response_time,
               location,
               severity_level,
               dispatch_status
        FROM warehouse.fact_emergency
        LIMIT 20;
    """)

    rows = cursor.fetchall()

    for row in rows:

        message = {
            "incident_id": row[0],
            "incident_type": row[1],
            "response_time": row[2],
            "location": row[3],
            "severity_level": row[4],
            "dispatch_status": row[5]
        }

        # ----------------------------
        # Emergency Events
        # ----------------------------

        alert = ""

        if message["severity_level"] == "High":
            alert = "🚑 High Severity Emergency!"

        elif message["dispatch_status"] != "Dispatched":
            alert = "🚨 Dispatch Pending!"

        message["alert"] = alert

        producer.send("emergency_topic", value=message)

        print(message)

        if alert:
            print(alert)

        time.sleep(1)


# ==========================================================
# Pollution
# ==========================================================
def stream_pollution():

    print("\nStreaming Pollution Data...\n")

    cursor.execute("""
        SELECT sensor_id,
               aqi,
               co2_level,
               pm2_5,
               temperature,
               humidity
        FROM warehouse.fact_pollution
        LIMIT 20;
    """)

    rows = cursor.fetchall()

    for row in rows:

        message = {
            "sensor_id": row[0],
            "aqi": row[1],
            "co2_level": row[2],
            "pm2_5": row[3],
            "temperature": row[4],
            "humidity": row[5]
        }

        # ----------------------------
        # Pollution Events
        # ----------------------------

        alert = ""

        if message["aqi"] > 150:
            alert = "🌍 AQI Spike!"

        elif message["co2_level"] > 450:
            alert = "⚠ Pollution Alert!"

        elif message["humidity"] < 10:
            alert = "❌ Sensor Failure!"

        message["alert"] = alert

        producer.send("pollution_topic", value=message)

        print(message)

        if alert:
            print(alert)

        time.sleep(1)
# ==========================================================
# Main
# ==========================================================

def main():

    try:

        stream_traffic()
        stream_transport()
        stream_rides()
        stream_parking()
        stream_emergency()
        stream_pollution()

        producer.flush()

    finally:

        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()