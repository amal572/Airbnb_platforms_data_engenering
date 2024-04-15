# Airbnb Zoomcamp Course Project | Data Engineering

#### Note: I chose Snowflake over Google Cloud because my free account expired. Similarly, my free account in DBT Cloud expired, leading me to use my friend's account. Consequently, you may notice two users in this repository. 

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
1. Setup your google cloud project and service account [step1](setup/gcp_account.md)
2. install terraform on your local machine [step2](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp)
3. Setup terraform to create pipeline required infrastructure [step3](setup/terraform_vm.md)
4. SSH to your google compute engine VM [step4](setup/gcp_vm.md)
5. Clone the repo to your google compute engine VM
    ```bash
    git clone https://github.com/AliaHa3/data-engineering-zoomcamp-project.git
    ```
6. Setup Anaconda + docker  + docker-compose
     ```bash
    cd data-engineering-zoomcamp-project
    bash scripts/vm_setup.sh
    ```
7. Update the enviroment variables in below file with your specific project_id and buckets
    ```bash
    cat data-engineering-zoomcamp-project/scripts/setup_config.sh
    ```
8. Setup pipeline docker image (airflow+spark)
     ```bash
    cd data-engineering-zoomcamp-project
    bash scripts/airflow_startup.sh
    ```
9. in Visual Studio code click on ports and forward port 8080<br>
  ![ForwardPort](https://user-images.githubusercontent.com/7443591/160403735-7c40babc-7d63-4b51-90da-c065e5b254a0.png)

go to localhost:8080<br>
  
and login with (airflow:airflow) for the credentials<br>
![AirflowLogin](https://user-images.githubusercontent.com/7443591/160413081-4f4e606f-09f6-4d4f-9b94-5241f37091a6.png)

9. Enable the historical_DAG and you should see it run. It takes 10-15 minutres to finish
10. Enable the hourly_DAG
11. You can check your data in bigquery tables.
12. if you want to stop docker image you can run below command
    ```bash
    cd data-engineering-zoomcamp-project
    bash scripts/airflow_stop.sh
    ```
    or to delete and clean all docker image related file
    ```bash
    cd data-engineering-zoomcamp-project
    bash scripts/airflow_clear.sh
    ```
