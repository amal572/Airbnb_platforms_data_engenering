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


## Data Ingestion: Batch Processing with Mega
![image](https://github.com/amal572/Airbnb_platforms_data_engenering/blob/main/data-source/Mega_Pipline.PNG)
<li>Data Loader: Fetch data from the Kaggle URL and merge the two CSV files for each city (weekends, weekdays) into one CSV file.</li>
<li>Transformer: Change the data type and perform data cleaning on a column, for example, by handling null values.</li>
<li>Load Data: Create a Data Warehouse after the last processing and save it in the Snowflake cloud.</li>


## Technologies and Tools

- Cloud - [**Snowflake**](https://www.snowflake.com/)
- Containerization - [**Docker**](https://www.docker.com), [**Docker Compose**](https://docs.docker.com/compose/)
- Workflow Orchestration - [**mega magic**](https://docs.mage.ai/)
- data loaded - [**DBT Cloud**](https://www.getdbt.com/)
- Data Warehouse - [**Snowflake**](https://www.snowflake.com/)
- Data Visualization - [**Power BI**](https://www.microsoft.com/en-us/power-platform/products/power-bi)
- Language - [**Python**](https://www.python.org)
