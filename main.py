import pandas as pd
import numpy as np
clickstream = pd.read_csv(r"C:\SmartCityx\datasets\clickstream.csv")
emergency = pd.read_csv(r"C:\SmartCityx\datasets\emergency_response_data.csv")
parking = pd.read_csv(r"C:\SmartCityx\datasets\parking_management_data.csv")
pollution = pd.read_csv(r"C:\SmartCityx\datasets\pollution_monitoring_data.csv")
publictransport = pd.read_csv(r"C:\SmartCityx\datasets\public_transport_gps.csv")
ride = pd.read_csv(r"C:\SmartCityx\datasets\ride_booking_data.csv")
traffic = pd.read_csv(r"C:\SmartCityx\datasets\traffic_sensor_data.csv") 
print("dataset loaded succesfully")

"""dataset head and info"""
"""print("\nclickstream")
print(clickstream.head())
print(clickstream.info())
print("\nemergency")
print(emergency.head())
print(emergency.info())
print("\nparking")
print(parking.head())
print(parking.info())
print("\npollution")
print(pollution.head())
print(pollution.info())
print("\npublictransport")
print(publictransport.head())
print(publictransport.info())
print("\nride")
print(ride.head())
print(ride.info())
print("\nTraffic")
print(traffic.head())
print(traffic.info())"""


"""dataset duplicate checking"""
"""print("Traffic:", traffic.duplicated().sum())
print("Emergency:", emergency.duplicated().sum())
print("Parking:", parking.duplicated().sum())
print("Pollution:", pollution.duplicated().sum())
print("Public Transport:", publictransport.duplicated().sum())
print("Ride:", ride.duplicated().sum())
print("Clickstream:", clickstream.duplicated().sum())"""

"""time stamp conversion"""
"""traffic["Timestamp"] = pd.to_datetime(
    traffic["Timestamp"],
    format="%d-%m-%Y %H:%M"
)
clickstream["event_timestamp"] = pd.to_datetime(
    clickstream["event_timestamp"],
    format="%d-%m-%Y %H:%M"
)
print(traffic.info())
print(clickstream.info())"""

"""validating numeric columns"""
print(traffic["Vehicle_Count"].min())
print(traffic["Average_Speed "].min())
print(pollution["AQI"].min(), pollution["AQI"].max())
print(ride["Driver_Rating"].min(), ride["Driver_Rating"].max())
print(publictransport["Delay_Minutes"].min())

traffic.to_csv("cleaneddataset/traffic_clean.csv", index=False)
emergency.to_csv("cleaneddataset/emergency_clean.csv", index=False)
parking.to_csv("cleaneddataset/parking_clean.csv", index=False)
pollution.to_csv("cleaneddataset/pollution_clean.csv", index=False)
publictransport.to_csv("cleaneddataset/publictransport_clean.csv", index=False)
ride.to_csv("cleaneddataset/ride_clean.csv", index=False)
clickstream.to_csv("cleaneddataset/clickstream_clean.csv", index=False)