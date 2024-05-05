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
To run these scripts, you can create and activate the virtual environment and then install dependencies via requirement.txt file.
for doing that open a terminal, change directory the the place you want clone the repository.
do the following commands in your terminal:

1. First create a virtual environment, here you can install and use virtualenv:
'''bash
pip install virtualenv
'''
'''bash
virtualenv weatherappenv
'''

2. You can then clone the repository using this command::

```bash
git clone https://github.com/Ehsan457/weather-app.git
```

3. Install dependencies with this command:
```bash
pip install -r requirements.txt
```

4. Finally, you can modify the config file according to your needs and run the scripts. For ease of use, simply run createDB.py followed by createTable.py, and then run main.py to store the data in your database.

   
Note: The OpenWeatherMap API key is not pushed to this repository. You can sign up on the OpenWeatherMap website to get your own API key for free.

You can also create DAG scripts, put them in the Airflow DAGs folder, and activate them in your Airflow webserver to automate the workflows. Alternatively, you can use Cron after running createDB.py and createTable.py once.
