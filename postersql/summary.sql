-- CREATE TABLE gold.most_congested_junctions AS
-- SELECT
--     junction_id,
--     SUM(vehicle_count) AS total_vehicle_count
-- FROM warehouse.fact_traffic
-- GROUP BY junction_id
-- ORDER BY total_vehicle_count DESC;
-- SELECT * FROM gold.most_congested_junctions
-- LIMIT 10;

-- CREATE TABLE gold.peak_traffic_hours AS
-- SELECT
--     EXTRACT(HOUR FROM timestamp) AS hour,
--     SUM(vehicle_count) AS total_vehicles
-- FROM warehouse.fact_traffic
-- GROUP BY hour
-- ORDER BY total_vehicles DESC;
-- SELECT * FROM gold.peak_traffic_hours;

-- CREATE TABLE gold.weather_traffic_analysis AS
-- SELECT
--     weather_condition,
--     ROUND(AVG(vehicle_count)::NUMERIC, 2) AS avg_vehicle_count,
--     ROUND(AVG(average_speed)::NUMERIC, 2) AS avg_speed
-- FROM warehouse.fact_traffic
-- GROUP BY weather_condition;
-- select * from gold.weather_traffic_analysis

-- CREATE TABLE gold.high_risk_congestion AS
-- SELECT
--     junction_id,
--     congestion_level,
--     COUNT(*) AS total_records
-- FROM warehouse.fact_traffic
-- GROUP BY junction_id, congestion_level
-- ORDER BY total_records DESC;
-- select * from gold.high_risk_congestion

-- CREATE TABLE gold.avg_speed_trends AS
-- SELECT
--     junction_id,
--     ROUND(AVG(average_speed)::NUMERIC,2) AS avg_speed
-- FROM warehouse.fact_traffic
-- GROUP BY junction_id
-- ORDER BY avg_speed DESC;
-- select * from gold.avg_speed_trends
SELECT * FROM gold.weather_traffic_analysis;

