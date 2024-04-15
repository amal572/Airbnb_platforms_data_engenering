# Airbnb Zoomcamp Course Project | Data Engineering

#### Note: I chose Snowflake over Google Cloud because my free account expired. Similarly, my free account in DBT Cloud expired, leading me to use my friend's account.

### Problem statement
The project aims to build an end-to-end data pipeline that extracts Airbnb prices in some of the most popular European cities from [**Kaggle**]([https://earthquake.usgs.gov/fdsnws/event/1/](https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities)). Each listing is evaluated for various attributes such as room types, cleanliness and satisfaction ratings, bedrooms, distance from the city center, and more to capture an in-depth understanding of Airbnb prices on both weekdays and weekends.
There will be one running pipeline (DAG):
<li> Weekly_DAG: this DAG will run weekly to extract new data starting from the installation time. </li>

### Data schema

| Column | Type | 
|--------|-------------|
| realSum |  FloatType |
| room_type | StringType |
| is_shared_room | BooleanType |
| is_private_room | BooleanType |
| person_capacity | IntegerType  |
| is_superhost | BooleanType |
| is_multi_rooms | BooleanType |
| is_business | BooleanType |
| bedrooms | IntegerType |
| person_capacity | IntegerType |
| cleanliness_rating | IntegerType |
| guest_satisfaction_rating | IntegerType |
| central_distance | FloatType |
| metro_distance | FloatType |
| longitude | FloatType |
| latitude | FloatType |
| city | StringType |

### Data Pipeline
![image](https://github.com/amal572/Airbnb_platforms_data_engenering/blob/main/Airbnb_Pipline_final.gif)

## Technologies and Tools

- Cloud - [**Snowflake**](https://www.snowflake.com/)
- Containerization - [**Docker**](https://www.docker.com), [**Docker Compose**](https://docs.docker.com/compose/)
- Workflow Orchestration - [**mega magic**](https://docs.mage.ai/)
- data loaded - [**DBT Cloud**](https://www.getdbt.com/)
- Data Warehouse - [**Snowflake**](https://www.snowflake.com/)
- Data Visualization - [**Power BI**](https://www.microsoft.com/en-us/power-platform/products/power-bi)
- Language - [**Python**](https://www.python.org)


## Data Ingestion: Batch Processing with Mega
![image](https://github.com/amal572/Airbnb_platforms_data_engenering/blob/main/data-source/Mega_Pipline.PNG)
<li>Data Loader: Fetch data from the Kaggle URL and merge the two CSV files for each city (weekends, weekdays) into one CSV file.</li>
<li>Transformer: Change the data type and perform data cleaning on a column, for example, by handling null values.</li>
<li>Load Data: Create a Data Warehouse after the last processing and save it in the Snowflake cloud.</li>

## Data Modeling:
![image](https://github.com/amal572/Airbnb_platforms_data_engenering/blob/main/dbt_DGA.PNG)
After transforming and loading the data into Snowflake using Mega pipelines, we utilize the Data Build Tool (dbt) to combine or join the dimension tables with the fact tables. This process generates specific reporting tables in another schema within BigQuery. These reporting tables are optimized for querying and analysis, providing insights into various aspects of the data

## Analytics Dashboard
Some screenshots from the dashboards to get you the full knowledge:
This dashboard compares the total listings for weekends and weekdays, depending on the city and the type of room.

![image](https://github.com/amal572/Airbnb_platforms_data_engenering/blob/main/Dashboard1.PNG)

You can determine the average listing price by city and room type, as well as the distance between the city and the metro, and between the city and downtown.

![image](https://github.com/amal572/Airbnb_platforms_data_engenering/blob/main/Dashboard2.PNG)

Also, you can filter by specifics such as city or room type.

![image](https://github.com/amal572/Airbnb_platforms_data_engenering/blob/main/Filter.PNG)

You can download the dashboard and try it using Power BI by using this file

![file](https://github.com/amal572/Airbnb_platforms_data_engenering/blob/main/Airbnb_Dashboard.pbix)


## Setup
1. create an account in Snowflake [step1](https://www.snowflake.com/)
2. create an account in dbt Cloud [step2](https://www.getdbt.com/)
3. Clone the repo to your Google Compute engine VM
    ```bash
    git clone https://github.com/amal572/Airbnb_platforms_data_engenering.git
    ```
4. Setup docker  + docker-compose with all services 
     ```bash
    cd Airbnb_platforms_data_engenering
    docker compose up
    ```
5. run the mega Navigate to http://localhost:6789 in your browser and run the last pipeline after changing the config.io with your username, password, service name

6. check your data warehouse in Snowflake and push the project to your GitHub 
   
7. open your account in dbt cloud and clone your repository on it then run
     ```bash
        dbt build
    ```
8. Check your Snowflake schema; you will find a new database with fact and dimension tables. Then check the job; you can find it, just run it and verify if everything works.

9. Connect Snowflake with Power BI following these steps:
   ![file](https://learn.microsoft.com/en-us/power-bi/connect-data/service-connect-snowflake)

## Reference
[DataTalks Club](https://datatalks.club/)<br>
[Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp#week-1-introduction--prerequisites)<br>
    
