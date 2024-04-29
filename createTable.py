from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from configparser import ConfigParser

def create_weather_table(config_file):
    """
    This function for creating table 
    read the necessary informations from
    config file in the same directory as this script.
    """
    
    try:
        
        config = ConfigParser()
        config.read(config_file)

        # Read database connection parameters from config
        db_type = config.get('database','type')
        db_user = config.get('database', 'username')
        pwd = config.get('database', 'password')
        host = config.get('database', 'host')
        port = config.get('database', 'port')
        db_name = config.get('database', 'db_name')

        engine = create_engine(f'{db_type}://{db_user}:{pwd}@{host}:{port}/{db_name}',echo=True)
        metadata = MetaData()


        weather_data = Table(
            'weather_data',
            metadata,
            Column('id', Integer, primary_key=True),
            Column('Timestamp', String),
            Column('City', String),
            Column('Weather_Status', String),
            Column('Weather_Description', String),
            Column('Temperature', Float),
            Column('Feels_Like', Float),
            Column('Temp_Min', Float),
            Column('Temp_Max', Float),
            Column('Pressure', Float),
            Column('Humidity', Integer),
            Column('Wind_Speed', Float),
            Column('Wind_Deg', Float)
        )


        metadata.create_all(engine)
        print("Table 'weather_data' created successfully!")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Path to config file
    config_file = "config.ini"

    create_weather_table(config_file)
