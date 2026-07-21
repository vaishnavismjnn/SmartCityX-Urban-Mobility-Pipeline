--SELECT * FROM silver.traffic LIMIT 10;
--SELECT COUNT(*) FROM traffic;
--SELECT COUNT(*) FROM emergency;
--SELECT COUNT(*) FROM parking;
--SELECT COUNT(*) FROM pollution;
--SELECT COUNT(*) FROM publictransport;
--SELECT COUNT(*) FROM ride;
--SELECT * FROM silver.clickstream limit 5;
--SELECT * FROM silver.ride limit 5;

--CREATE SCHEMA silver;
--ALTER TABLE public.ride
--SET SCHEMA silver;

--SELECT timestamp
--FROM silver.traffic
--LIMIT 5;

--CREATE SCHEMA gold;
--CREATE SCHEMA warehouse;

-- CREATE TABLE warehouse.dim_time (
--     time_id SERIAL PRIMARY KEY,
--     full_timestamp TIMESTAMP,
--     day INT,
--     month INT,
--     year INT,
--     hour INT
-- );
-- INSERT INTO warehouse.dim_time
-- (full_timestamp, day, month, year, hour)

-- SELECT DISTINCT
-- timestamp,
-- EXTRACT(DAY FROM timestamp),
-- EXTRACT(MONTH FROM timestamp),
-- EXTRACT(YEAR FROM timestamp),
-- EXTRACT(HOUR FROM timestamp)
-- FROM silver.traffic;


-- CREATE TABLE warehouse.dim_weather (

-- weather_id SERIAL PRIMARY KEY,

-- weather_condition VARCHAR(30)

-- );

-- INSERT INTO warehouse.dim_weather(weather_condition)

-- SELECT DISTINCT weather_condition

-- FROM silver.traffic;


-- CREATE TABLE warehouse.dim_route (

-- route_id VARCHAR(20) PRIMARY KEY

-- );

-- INSERT INTO warehouse.dim_route

-- SELECT DISTINCT route_id

-- FROM silver.publictransport;


-- CREATE TABLE warehouse.dim_zone(

-- zone_name VARCHAR(30) PRIMARY KEY

-- );

-- INSERT INTO warehouse.dim_zone

-- SELECT DISTINCT pickup_zone

-- FROM silver.ride

-- ON CONFLICT DO NOTHING;

-- INSERT INTO warehouse.dim_zone

-- SELECT DISTINCT drop_zone

-- FROM silver.ride

-- ON CONFLICT DO NOTHING;

-- INSERT INTO warehouse.dim_zone

-- SELECT DISTINCT zone

-- FROM silver.parking

-- ON CONFLICT DO NOTHING;


-- CREATE TABLE warehouse.dim_location(

-- location_name VARCHAR(30) PRIMARY KEY

-- );

-- INSERT INTO warehouse.dim_location

-- SELECT DISTINCT location

-- FROM silver.emergency;


-- CREATE TABLE warehouse.dim_vehicle(

-- bus_id VARCHAR(20) PRIMARY KEY

-- );

-- INSERT INTO warehouse.dim_vehicle

-- SELECT DISTINCT bus_id

-- FROM silver.publictransport;

-- CREATE TABLE warehouse.fact_traffic AS

-- SELECT

-- sensor_id,

-- junction_id,

-- vehicle_count,

-- average_speed,

-- congestion_level,

-- timestamp,

-- weather_condition

-- FROM silver.traffic;


-- CREATE TABLE warehouse.fact_transport AS

-- SELECT *

-- FROM silver.publictransport;



-- CREATE TABLE warehouse.fact_rides AS

-- SELECT *

-- FROM silver.ride;



-- CREATE TABLE warehouse.fact_parking AS

-- SELECT *

-- FROM silver.parking;


-- CREATE TABLE warehouse.fact_pollution AS

-- SELECT *

-- FROM silver.pollution;

CREATE TABLE warehouse.fact_emergency AS

SELECT *

FROM silver.emergency;

-- SELECT * FROM warehouse.fact_traffic limit 5;