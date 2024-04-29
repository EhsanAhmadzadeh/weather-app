# Weather App

## Description
This is a simple weather app that fetches current weather data from the OpenWeatherMap API and stores it in a PostgreSQL database. This project is intended for educational purposes.

## Requirements
- Python 3.x
- SQLAlchemy
- Requests
- Pandas
- Dotenv

## Running Scripts
To run these scripts, you can either activate the virtual environment provided in this repository or run the following command in your terminal:

```bash
pip install -r requirements.txt
```
You can modify the config file according to your needs. Note that the OpenWeatherMap API key is not pushed to this repository. You can sign up on the OpenWeatherMap website to get your own API key for free.

For ease of use, simply run createDB.py followed by createTable.py, and then run main.py to store the data in your database.

You can also create DAG scripts, put them in the Airflow DAGs folder, and activate them in your Airflow webserver to automate the workflows. Alternatively, you can use Cron after running createDB.py and createTable.py once.
