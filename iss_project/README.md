
# Wranging the International Space Station

There is a plethora of data that comes from the ISS, and this project wrangles the data given in difficult, if not impossible, to read XML files into a queryable Flask app. This app allows for the user to search for sightings of the ISS at certain epochs, and then when it's above certain countries, regions, and cities!




## Data Download

Instructions for downloading the data!

1. Click [here](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq) to visit the NASA open data portal. 
2. From here, get the URL of the XML public distribution file, and the XMLsightingData_citiesUSA08 file. (Do this by right clicking on the XML box and selecting open in new tab)
3. On ISP, inside of the iss_project directory, run wget <url> (Where URL is the link to the data source)
    
## Building the Docker Container

To run the Docker Contain for this project, there is a Makefile to streamline the process

Just enter the command 
```make all ```
 into the command line, and it will run! 

 ### Pull a Working Container from DockerHub
 Run the command ```docker pull <username>/<file-name>:latest ```


 





## Using the Flask App

Use curl to interact with the Flask App. 
To begin, run 
```
export FLASK_APP = app.py
export FLASK_ENV = development
flask run -p 5000
```

Then, in a second terminal, you must read in the data 
Run 
```
localhost:5000/read_data -X post
```

After running that command, you can run any of the routes and get results. 
Possible routes:

```
/EPOCH --> lists all epochs 
/EPOCH/<user_specified_epoch> --> lists all data for user specified epochs
/countries --> get a list of all countries 
/COUNTRY/<user_speciified_country> --> lists all data for user specified countries 
/COUNTRY/<country>/regions --> lists all regions in a specified country 
/COUNTRY/<country>/regions/<regions>  --> lists all data for a user specified region within a user specified country 
/COUNTRY/<country>/regions/<regions>/cities  --> lists all cities within a user specified region within a user specified country 
/COUNTRY/<country>/regions/<regions>/cities/<city> --> lists all data within a user specified city within a specified region and country 


```

If running any of the above commands using curl doesn't work, just rerun the fourth command above (/read_data)

Sample input:

```
curl localhost:5000/COUNTRY/United_States/regions/Oregon/cities/Burns
```

Sample input: 
```
curl localhost:5000/COUNTRY/United_States/regions/Oregon/cities/Burns
```

Truncated sample output:

```
[
  {
    "spacecraft": "ISS",
    "sighting_date": "Thu Feb 17/05:47 AM",
    "duration_minutes": "4",
    "max_elevation": "16",
    "enters": "10 above S",
    "exits": "10 above E",
    "utc_offset": "-8.0",
    "utc_time": "13:47",
    "utc_date": "Feb 17, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Sat Feb 19/05:46 AM",
    "duration_minutes": "6",
    "max_elevation": "41",
    "enters": "10 above SSW",
    "exits": "10 above ENE",
    "utc_offset": "-8.0",
    "utc_time": "13:46",
    "utc_date": "Feb 19, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Sun Feb 20/05:00 AM",
    "duration_minutes": "4",
    "max_elevation": "25",
    "enters": "18 above S",
    "exits": "10 above E",
    "utc_offset": "-8.0",
    "utc_time": "13:00",
    "utc_date": "Feb 20, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Mon Feb 21/04:14 AM",
    "duration_minutes": "1",
    "max_elevation": "14",
    "enters": "14 above ESE",
    "exits": "10 above E",
    "utc_offset": "-8.0",
    "utc_time": "12:14",
    "utc_date": "Feb 21, 2022"
  },
  {
    "spacecraft": "ISS",
    "sighting_date": "Mon Feb 21/05:47 AM",
    "duration_minutes": "6",
    "max_elevation": "77",
    "enters": "16 above WSW",
    "exits": "10 above NE",
    "utc_offset": "-8.0",
    "utc_time": "13:47",
    "utc_date": "Feb 21, 2022"
```

Don't forget to add curl before the Flask requests!





## Citations

1. Goodwin, S. (n.d.). ISS_COORDS_2022-02-13. NASA. https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml Retrieved March 20, 2022, from https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq

2. Goodwin, S. (n.d.). XMLsightingData_citiesUSA08. NASA. Retrieved March 20, 2022, from https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA08.xml

