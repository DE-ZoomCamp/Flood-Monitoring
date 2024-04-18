CREATE OR REPLACE TABLE `floodmonitoring.floodsdata_partitioned`
PARTITION BY dateRaised
CLUSTER BY eaAreaName AS (
  SELECT * FROM `floodmonitoring.floodsdata`
);



SELECT * FROM `floodmonitoring.floodsdata_partitioned`;