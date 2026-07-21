-- -- SELECT * FROM warehouse.fact_traffic LIMIT 5;
-- SELECT * FROM warehouse.fact_transport LIMIT 5;
-- SELECT * FROM warehouse.fact_rides LIMIT 5;
-- SELECT * FROM warehouse.fact_parking LIMIT 5;
-- SELECT * FROM warehouse.fact_emergency LIMIT 5;
-- SELECT * FROM warehouse.fact_pollution LIMIT 5;

-- SELECT
--     junction_id,
--     SUM(vehicle_count) AS total_vehicle_count
-- FROM warehouse.fact_traffic
-- GROUP BY junction_id
-- ORDER BY total_vehicle_count DESC;

-- SELECT
--     EXTRACT(HOUR FROM timestamp) AS hour,
--     SUM(vehicle_count) AS total_vehicle_count
-- FROM warehouse.fact_traffic
-- GROUP BY EXTRACT(HOUR FROM timestamp)
-- ORDER BY total_vehicle_count DESC;

-- SELECT
--     junction_id,
--     ROUND(AVG(average_speed)::NUMERIC,2) AS avg_speed
-- FROM warehouse.fact_traffic
-- GROUP BY junction_id
-- ORDER BY avg_speed DESC;

-- SELECT
--     junction_id,
--     congestion_level,
--     COUNT(*) AS total_records
-- FROM warehouse.fact_traffic
-- GROUP BY
-- junction_id,
-- congestion_level
-- ORDER BY total_records DESC;

-- SELECT
--     weather_condition,
--     ROUND(AVG(vehicle_count)::NUMERIC,2) AS avg_vehicle_count,
--     ROUND(AVG(average_speed)::NUMERIC,2) AS avg_speed
-- FROM warehouse.fact_traffic
-- GROUP BY weather_condition
-- ORDER BY avg_vehicle_count DESC;

-- --Most Delayed Routes
-- SELECT
--     route_id,
--     ROUND(AVG(delay_minutes)::NUMERIC,2) AS avg_delay_minutes
-- FROM warehouse.fact_transport
-- GROUP BY route_id
-- ORDER BY avg_delay_minutes DESC;

--Passenger Utilization Trends
-- SELECT
--     route_id,
--     SUM(passenger_count) AS total_passengers
-- FROM warehouse.fact_transport
-- GROUP BY route_id
-- ORDER BY total_passengers DESC;

--Fuel Consumption Analysis
-- SELECT
--     route_id,
--     ROUND(AVG(fuel_consumption)::NUMERIC,2) AS avg_fuel_consumption
-- FROM warehouse.fact_transport
-- GROUP BY route_id
-- ORDER BY avg_fuel_consumption DESC;

--Route Efficiency Ranking
-- SELECT
--     route_id,
--     ROUND(
--         AVG(passenger_count)::NUMERIC /
--         NULLIF(AVG(delay_minutes),0),
--     2) AS efficiency_score
-- FROM warehouse.fact_transport
-- GROUP BY route_id

--10 Peak Passenger Routes
-- SELECT
--     route_id,
--     MAX(passenger_count) AS peak_passenger_count
-- FROM warehouse.fact_transport
-- GROUP BY route_id
-- ORDER BY peak_passenger_count DESC;


--High-Demand Pickup Zones
-- SELECT
--     pickup_zone,
--     COUNT(*) AS total_rides
-- FROM warehouse.fact_rides
-- GROUP BY pickup_zone
-- ORDER BY total_rides DESC;

--Revenue by Region
-- SELECT
--     pickup_zone,
--     ROUND(SUM(fare)::NUMERIC,2) AS total_revenue
-- FROM warehouse.fact_rides
-- GROUP BY pickup_zone
-- ORDER BY total_revenue DESC;

--Wait-Time Analysis
-- SELECT
--     pickup_zone,
--     ROUND(AVG(wait_time)::NUMERIC,2) AS avg_wait_time
-- FROM warehouse.fact_rides
-- GROUP BY pickup_zone
-- ORDER BY avg_wait_time DESC;

--Ride Duration Trends
-- SELECT
--     pickup_zone,
--     ROUND(AVG(trip_duration)::NUMERIC,2) AS avg_trip_duration
-- FROM warehouse.fact_rides
-- GROUP BY pickup_zone
-- ORDER BY avg_trip_duration DESC;

--Driver Performance Analysis
-- SELECT
--     pickup_zone,
--     ROUND(AVG(driver_rating)::NUMERIC,2) AS avg_driver_rating
-- FROM warehouse.fact_rides
-- GROUP BY pickup_zone
-- ORDER BY avg_driver_rating DESC;

--Parking Utilization %
-- SELECT
--     zone,
--     ROUND(AVG(occupancy)::NUMERIC,2) AS avg_occupancy
-- FROM warehouse.fact_parking
-- GROUP BY zone
-- ORDER BY avg_occupancy DESC;

--Peak Occupancy Timings
-- SELECT
--     peak_hour,
--     COUNT(*) AS total_records,
--     ROUND(AVG(occupancy)::NUMERIC,2) AS avg_occupancy
-- FROM warehouse.fact_parking
-- GROUP BY peak_hour;

--Revenue Analysis
-- SELECT
--     zone,
--     ROUND(SUM(hourly_revenue)::NUMERIC,2) AS total_revenue
-- FROM warehouse.fact_parking
-- GROUP BY zone
-- ORDER BY total_revenue DESC;

--Underutilized Parking Zones
-- SELECT
--     zone,
--     ROUND(AVG(occupancy)::NUMERIC,2) AS avg_occupancy
-- FROM warehouse.fact_parking
-- GROUP BY zone
-- ORDER BY avg_occupancy ASC;

--Zone-wise Parking Demand
-- SELECT
--     zone,
--     COUNT(*) AS total_parking_records
-- FROM warehouse.fact_parking
-- GROUP BY zone
--ORDER BY total_parking_records DESC;

--Slowest Response Regions
-- SELECT
--     location,
--     ROUND(AVG(response_time)::NUMERIC,2) AS avg_response_time
-- FROM warehouse.fact_emergency
-- GROUP BY location
-- ORDER BY avg_response_time DESC;

--Incident Frequency Trends
-- SELECT
--     incident_type,
--     COUNT(*) AS total_incidents
-- FROM warehouse.fact_emergency
-- GROUP BY incident_type
-- ORDER BY total_incidents DESC;

--Severity-Level Analysis
-- SELECT
--     severity_level,
--     COUNT(*) AS total_incidents
-- FROM warehouse.fact_emergency
-- GROUP BY severity_level
-- ORDER BY total_incidents DESC;

--Dispatch Efficiency
-- SELECT
--     dispatch_status,
--     COUNT(*) AS total_cases,
--     ROUND(AVG(response_time)::NUMERIC,2) AS avg_response_time
-- FROM warehouse.fact_emergency
-- GROUP BY dispatch_status
-- ORDER BY total_cases DESC;

--High-Risk Zones
-- SELECT
--     location,
--     COUNT(*) AS total_incidents
-- FROM warehouse.fact_emergency
-- GROUP BY location
-- ORDER BY total_incidents DESC;

--AQI Hotspots
-- SELECT
--     sensor_id,
--     aqi
-- FROM warehouse.fact_pollution
-- ORDER BY aqi DESC
-- LIMIT 20;

--Pollution Trends
-- SELECT
--     ROUND(AVG(aqi)::NUMERIC,2) AS avg_aqi,
--     ROUND(AVG(co2_level)::NUMERIC,2) AS avg_co2,
--     ROUND(AVG(pm2_5)::NUMERIC,2) AS avg_pm25
-- FROM warehouse.fact_pollution;

--PM2.5 Analysis
-- SELECT
--     sensor_id,
--     pm2_5
-- FROM warehouse.fact_pollution
-- ORDER BY pm2_5 DESC
-- LIMIT 20;

--Temperature vs AQI Relationship
-- SELECT
--     temperature,
--     ROUND(AVG(aqi)::NUMERIC,2) AS avg_aqi
-- FROM warehouse.fact_pollution
-- GROUP BY temperature
-- ORDER BY temperature;

--High Pollution Areas
-- SELECT
--     sensor_id,
--     aqi,
--     co2_level,
--     pm2_5
-- FROM warehouse.fact_pollution
-- ORDER BY aqi DESC, pm2_5 DESC;
