## FLOOD MONITORING

## Problem statement
Flood events pose significant risks to communities, infrastructure, and the environment. The environmental agency responsible for managing and responding to these flood events needs to develop a comprehensive dashboard to monitor, analyze, and optimize their flood event management operations.

The enviromental agency in UK is tasked to develop this dashboard and contacted me to do the consulation and provide a user resposnive and early wwarning alerts dashboard that can be used to asses floods in diffrent regions.

The key goals of the dashboard are to:
- Assess the overall flood risk across different regions and areas, identify high-risk locations, and understand  tidal influences.
- Closely monitor the severity of flood events, track changes in severity over time, and identify areas with consistently high or increasing severity levels.
- Analyze the geographical distribution of flood events, and understand how flood patterns vary across different regions.
- Analyze the flood severity and severity levels
- Check most types of floods istidal True or false
- Develop a dashboard of this.

The project has a Batch Pipeline that runs @daily 2000hrs.

## Dataset

Flood Monitoring dataset : https://environment.data.gov.uk/flood-monitoring/doc/reference

The dataset api used: http://environment.data.gov.uk/flood-monitoring/id/floods


# Architecture
![Workflow](https://github.com/DE-ZoomCamp/Flood-Monitoring/blob/master/Floodmonitoring.drawio.png)

# Cloning the Project

To clone this repository use this command.

`
git clone https://github.com/DE-ZoomCamp/Flood-Monitoring.git
`

# Technologies Used

- Docker

- Cloud: GCP

- Infrastructure as code (IaC): Terraform

- Workflow orchestration: Mage AI

- Data Warehouse: BigQuery

- Transformation: DBT CLOUD

- Visualization: Metabase Local

## Data Ingestion -Mage AI -Workflow orchestration

Created the data extration script(Data loader) from the flood monitoring api in Mage.

Code found here:[Link](https://github.com/DE-ZoomCamp/Flood-Monitoring/blob/master/orchestration_Mage/flood-monitoring/data_loaders/extract_py.py)

Loaded/Exported the data to google cloud storage(GCS) after creating a mapping between dataloader and data exporter.

Code found here:[Link](https://github.com/DE-ZoomCamp/Flood-Monitoring/blob/master/orchestration_Mage/flood-monitoring/data_exporters/insert_to_gcs.py)

##  Pipeline for moving the data from the lake to a data warehouse - BIGQUERY

I used SQL scripts to load data to bigquery.
Script here: [Link](https://github.com/DE-ZoomCamp/Flood-Monitoring/blob/master/pipelineMovementGcs_Bigquery/load_gcs_bigquery.sql)

Partitioned data based on the dataRaised of the flood alerts clustering by areaName.
script here:[Link](https://github.com/DE-ZoomCamp/Flood-Monitoring/blob/master/pipelineMovementGcs_Bigquery/partition.sql)

## Transforming the data in the data warehouse - Used DBT

After configuration and connection to Bigquery.

dbt_project.yml configured the name of the project

script here:[Link](https://github.com/DE-ZoomCamp/Flood-Monitoring/blob/master/transformation_DBT/floodmonitoring/dbt_project.yml)

Created a staging area , created schema.yml and defined the dataset in BigQuery, schema and also the tables associated with it.

Script here: [Link](https://github.com/DE-ZoomCamp/Flood-Monitoring/blob/master/transformation_DBT/floodmonitoring/models/staging/schema.yml)

Generate the sql:

Scripts here: [Link](https://github.com/DE-ZoomCamp/Flood-Monitoring/tree/master/transformation_DBT/floodmonitoring/models/staging)


Runs in dbt cloud:

`
dbt deps
`

also

`
dbt build
`

## Dashboard answering the above questions/objectives

I used metabase using docker by running this command.

`
 sudo docker run -d -p 3000:3000 --name metabase metabase/metabase
`

#### Process of setting up Metabase:

- Launched the metabase via localhost:3000

- configured database as Biqquery with the keys-json and used both.

- Selected the transformed(dbt) data partitioned in Biqguery to visualize it.

- Created Questions and added them to Dashboard.
  
- Schedued autorefresh to every 10 minutes.

Please use this link to access the dasboard publicly:

- Link to the dashboaard: http:public/dashboard/7b0551b1-230a-4a68-9c67-30083e1cc5ea

- or [Link](http:public/dashboard/7b0551b1-230a-4a68-9c67-30083e1cc5ea)

Dasboard Overview

![image](https://github.com/DE-ZoomCamp/Flood-Monitoring/assets/55980747/8ec36ce3-ebb0-4231-92e6-a73ddff6c023)

![image](https://github.com/DE-ZoomCamp/Flood-Monitoring/assets/55980747/de062f85-2891-4eba-8673-3fbaeb4df599)


Author:

Christopher




