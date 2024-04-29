import requests
from sqlalchemy import create_engine
from datetime import datetime
import pandas as pd
from configparser import ConfigParser
from dotenv import load_dotenv
import os



def fetch_weather_data(api_key, city):
    """
    This function will give you current weather data 
    in dataframe format.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    output = {}
    output['Timestamp'] = datetime.now()
    output["City"] = city
    output['Weather_Status'] = data["weather"][0]["main"]
    output['Weather_Description'] = data["weather"][0]["description"]
    output['Temperature'] = data["main"]["temp"]
    output['Feels_Like'] = data["main"]["feels_like"]
    output['Temp_Min'] = data["main"]["temp_min"]
    output['Temp_Max'] = data["main"]["temp_max"]
    output['Pressure'] = data["main"]["pressure"]
    output['Humidity'] = data["main"]["humidity"]
    output['Wind_Speed'] = data["wind"]["speed"]
    output['Wind_Deg'] = data["wind"]["deg"]

    df = pd.DataFrame([output])

    return df


def connect_db(config_file):
    """
    This function for connectiong to database 
    read the necessary informations from
    config file in the same directory as this script.
    """
    config = ConfigParser()
    config.read(config_file)

    # Read database connection parameters from config file
    db_type = config.get('database','type')
    db_user = config.get('database', 'username')
    pwd = config.get('database', 'password')
    host = config.get('database', 'host')
    port = config.get('database', 'port')
    db_name = config.get('database', 'db_name')

    engine = create_engine(f'{db_type}://{db_user}:{pwd}@{host}:{port}/{db_name}')
    connection = engine.connect()
    return connection


def main():
    
    # You can use your api key here
    load_dotenv()
    openweathermap_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    
    # Replace with the city of your choice
    city = "Tehran"

    # Path to config file
    config_file = "config.ini"
    connection = connect_db(config_file)

    current_data = fetch_weather_data(openweathermap_api_key, city)
    current_data.to_sql("weather_data", connection, if_exists='append', index=False)
    connection.close()


if __name__ == "__main__":
    main()