import psycopg2
from configparser import ConfigParser

def create_database(config_file):
    """
    This function for creating database 
    read the necessary informations from
    config file in the same directory as this script.
    """
    config = ConfigParser()
    config.read(config_file)

    # Read database connection parameters from config
    db_user = config.get('database', 'username')
    pwd = config.get('database', 'password')
    host = config.get('database', 'host')
    port = config.get('database', 'port')
    db_name = config.get('database', 'db_name')

    try:
        # Connect to PostgreSQL server
        conn = psycopg2.connect(
            dbname='postgres', 
            user=db_user, 
            password=pwd, 
            host=host, 
            port=port
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Create database
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' created successfully!")

    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        
        if 'conn' in locals():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    
    # Path to config file
    config_file = "config.ini"

    create_database(config_file)
