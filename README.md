# SmartCityX – Urban Mobility & Public Operations Intelligence Platform

## Project Overview

SmartCityX is an end-to-end Data Engineering and Analytics project designed to monitor and analyze urban mobility and public operations.

The project processes multiple city datasets using a modern ETL pipeline, stores the data in PostgreSQL using a Medallion Architecture (Bronze, Silver, Warehouse), streams real-time data with Apache Kafka, schedules pipelines using Apache Airflow, visualizes live events in Streamlit, and provides business insights through Power BI dashboards.

## Features

- End-to-End ETL Pipeline
- PostgreSQL Data Warehouse
- Medallion Architecture (Bronze, Silver, Warehouse)
- Apache Kafka Real-Time Streaming
- Apache Airflow Workflow Scheduling
- Live Streamlit Dashboard
- Power BI Analytics Dashboards
- Docker-based Deployment

## Project Architecture

![Architecture](architecture%20diagram/architecture.png)


## Project Flow

The SmartCityX pipeline processes urban mobility data through a complete data engineering workflow, from ingestion to real-time visualization.

### Step 1: Data Collection
- Multiple CSV datasets are collected from different smart city domains:
  - Traffic Monitoring
  - Public Transport
  - Parking Management
  - Emergency Response
  - Pollution Monitoring
  - Ride Booking

### Step 2: ETL Pipeline
- Python is used to perform Extract, Transform, and Load (ETL) operations.
- Data is cleaned by handling missing values, removing duplicates, correcting data types, and standardizing formats.

### Step 3: PostgreSQL Data Warehouse
The processed data is stored using a Medallion Architecture:
- **Bronze Layer:** Stores raw ingested data.
- **Silver Layer:** Stores cleaned and transformed data.
- **Warehouse Layer:** Stores fact and dimension tables optimized for analytics.

### Step 4: Batch Analytics
- SQL queries generate analytical datasets and KPIs from the warehouse.
- These outputs are used for reporting and dashboard creation.

### Step 5: Workflow Orchestration
- Apache Airflow schedules and automates the Kafka Producer.
- The DAG executes the producer at scheduled intervals without manual intervention.

### Step 6: Real-Time Data Streaming
- The Kafka Producer reads records from PostgreSQL and publishes them to multiple Kafka topics:
  - Traffic
  - Transport
  - Parking
  - Emergency
  - Pollution
  - Ride Booking

### Step 7: Real-Time Data Consumption
- A Kafka Consumer subscribes to all topics.
- Incoming messages are processed continuously for live monitoring.

### Step 8: Visualization
- **Power BI** provides interactive analytical dashboards for historical and business insights.
- **Streamlit** displays live streaming data, KPIs, alerts, and real-time city operations.