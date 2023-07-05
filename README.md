# sqlalchemy-challenge
![image](https://github.com/RabNing/Hawaii_Climate_App/assets/126477871/e6c01d4d-9b21-488e-a079-bee8fb64af64)

# Project Instructions
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task:
# Part 1:
Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib.
# Part 2: 
Design Your Climate App
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed.


The SurfsUp folder contains a climate_starter.ipynb script and a app_NG.py scrupt. The Resources folder contains original data in csv forms and a hawaii.sqlite file.
The climate_starter.ipynb script contains exploration and analysis results of the Hawaii Clinate Data, including Precipitation Analysis of the previous 12 months, and Temperature Analysis of the previous 12 months from the most acitve station. Analysis.
The app_NG.py is a Climate App designed with Flask API based on the queries from the climate_starter.ipynb script. The app has a landing page and 5 routes:
	A precipitation route that returns json with the date as the key and the value as the precipitation;
	A stations route that returns jsonified data of all of the stations in the database;
	A tobs route that returns jsonified data for the most active station (USC00519281);
	A dynamic start route that returns the min, max, and average temperatures calculated from the given start date to the end of the dataset;
	A dynamic start/end route that returns the min, max, and average temperatures calculated from the given start date to the given end date.
