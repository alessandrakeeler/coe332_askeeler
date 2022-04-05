# Utilizing Redis with Flask and Docker 

## This homework utilizes the Redis container to run a Flask app to query data. 

## Using the repository. 
### Explanation of files.
```app.py``` contains the code to run the flask app. It as a route to load the data and a route to query the data.

```Dockerfile``` contains the commands for the Docker container this project is running on.

### Steps to run. 
1. ```docker run -d -p 6379:6379 -v $(pwd)/data:/data:rw --name=<DockerUsername>-redis redis:6 save 1 1```
2. ```export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run -p 5000```

3. ``` curl localhost:5000/data -X POST ```

4. ```curl localhost:5000/data```

### Sample data output

```    "name": "Shannon",
            "id": "10157",
            "recclass": "CR2-an",
            "mass (g)": "7587",
            "reclat": "-67.0981",
            "reclong": "-66.0576",
            "GeoLocation": "(-67.0981, -66.0576)"
       
            "name": "Edith",
            "id": "10158",
            "recclass": "EH4",
            "mass (g)": "9239",
            "reclat": "11.3539",
            "reclong": "24.9350",
            "GeoLocation": "(11.3539, 24.9350)"

```


