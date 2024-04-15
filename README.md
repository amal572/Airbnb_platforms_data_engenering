# Airbnb Zoomcamp Course Project | Data Engineering

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
