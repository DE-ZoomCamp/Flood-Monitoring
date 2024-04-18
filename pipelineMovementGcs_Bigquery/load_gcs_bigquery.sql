CREATE OR REPLACE EXTERNAL TABLE `floodmonitoring.floodsdata`
OPTIONS (
  format = 'csv',
  uris = ['gs://flood-bucket24/floods.csv']
);
