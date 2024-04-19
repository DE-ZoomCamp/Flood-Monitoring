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

## Dashboard answering the above questions/objectives

Link to the dashboaard: http://localhost:3000/public/dashboard/7b0551b1-230a-4a68-9c67-30083e1cc5ea

or ![Link](http://localhost:3000/public/dashboard/7b0551b1-230a-4a68-9c67-30083e1cc5ea)


![image](https://github.com/DE-ZoomCamp/Flood-Monitoring/assets/55980747/8ec36ce3-ebb0-4231-92e6-a73ddff6c023)

![image](https://github.com/DE-ZoomCamp/Flood-Monitoring/assets/55980747/de062f85-2891-4eba-8673-3fbaeb4df599)





