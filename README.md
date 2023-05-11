# sqlalchemy-challenge
The SurfsUp folder contains a climate_starter.ipynb script and a app_NG.py scrupt. The Resources folder contains original data in csv forms and a hawaii.sqlite file.
The climate_starter.ipynb script contains exploration and analysis results of the Hawaii Clinate Data, including Precipitation Analysis of the previous 12 months, and Temperature Analysis of the previous 12 months from the most acitve station. Analysis.
The app_NG.py is a Climate App designed with Flask API based on the queries from the climate_starter.ipynb script. The app has a landing page and 5 routes:
	A precipitation route that returns json with the date as the key and the value as the precipitation;
	A stations route that returns jsonified data of all of the stations in the database;
	A tobs route that returns jsonified data for the most active station (USC00519281);
	A dynamic start route that returns the min, max, and average temperatures calculated from the given start date to the end of the dataset;
	A dynamic start/end route that returns the min, max, and average temperatures calculated from the given start date to the given end date.
