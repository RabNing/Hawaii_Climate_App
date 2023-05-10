# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
app = Flask(__name__)
#################################################

#################################################
# Flask Routes
#################################################
# Start at the homepage & List all the available routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Hawaii Trip Planning Climate API!<br/>"
        f"Available Routes:<br/>"
        f"Daily precipitation record for the last 12 months: /api/v1.0/precipitation<br/>"
        f"List of ovservation stations: /api/v1.0/stations<br/>"
        f"Daily temperature record for the last 12 months:/api/v1.0/tobs<br/>"
        f"Temperature analysis of the records since 2016-08-23: /api/v1.0/2016-08-23<br/>"
        f"Temperature analysis of the records between 2016-08-23 and 2016-12-31: /api/v1.0/2016-08-23/2016-12-31<br/>"
    )

# Return the JSON representation of your dictionary
@app.route("/api/v1.0/precipitation")
def prcp():
    # Calculate the date one year from the last date in data set.
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    prcp_all=session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= query_date).all()

    session.close()
    # Create a dictionary from the row data and append to a list
    precipitation = []
    for date, prcp in prcp_all:
        prcp_all_dict = {}
        prcp_all_dict["date"] = date
        prcp_all_dict["prcp"] = prcp
        precipitation.append(prcp_all_dict)
    
    return jsonify(precipitation)

# Return a JSON list of stations from the dataset
@app.route("/api/v1.0/stations")
def station():
    # Perform a query to retrieve the station data
    stat = session.query(Station.station).all()

    session.close()
    # Convert list of tuples into normal list
    all_station= list(np.ravel(stat))

    return jsonify(all_station)

# Return a JSON list of temperature observations for the previous year
@app.route("/api/v1.0/tobs")
def temp():
    # Calculate the date one year from the last date in data set.
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Perform a query to retrieve the dates and temperature observations of the most-active station for the previous year of data
    year_temp = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= query_date).all()

    session.close()
    # Convert list of tuples into normal list
    all_year_temp= list(np.ravel(year_temp))

    return jsonify(all_year_temp)    

# Return a JSON list of data for a specified start
@app.route("/api/v1.0/2016-08-23")
def start():
    # Using the most active station id from the previous query, calculate the lowest, highest, and average temperature.
    TMIN = session.query(func.min(Measurement.tobs)).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= '2016-8-23').first()
    
    TMAX = session.query(func.max(Measurement.tobs)).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= '2016-8-23').first()
    
    TAVG = session.query(func.avg(Measurement.tobs)).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= '2016-8-23').first()
    
    session.close()
    # Convert your API data to a valid JSON response object
    return jsonify(f"From 2016-08-23, the minimum temperature is {TMIN}, the average temperature is {TAVG}, and the maximum temperature is {TMAX}")

# Return a JSON list of data for a specified start-end range
@app.route("/api/v1.0/2016-08-23/2016-12-31")
def start_end():

    # Using the most active station id from the previous query, calculate the lowest, highest, and average temperature.
    TAVG = session.query(func.avg(Measurement.tobs)).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >='2016-8-23').\
        filter(Measurement.date <='2016-12-31').first()
    
    session.close()
    # Convert your API data to a valid JSON response object
    return jsonify(f"Between 2016-08-23 and 2016-12-31, the minimum temperature is TMIN, the average temperature is {TAVG} , and the maximum temperature is TMAX ")    
    
# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)

