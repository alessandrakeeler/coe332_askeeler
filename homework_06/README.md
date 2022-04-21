# Watch out for meteors in the Kubernetes-verse!

This project utilizes Kubernetes to deploy a Flask API that uses Redis to create a testing environment for the application. The app itself is the same as HW5, reading in meteorite data from a json file and outputs the results to the user. 

### Files in this repository
- app.py: from homework 5, utilizes GET and POST to query the meteor data
- askeeler-test-redis-deplpoyment.yml: deploys the redis database 
- askeeler-test-redis-volume.yml: data storage from deployment
- askeeler-test-redis-service.ymp: provides an IP address to interact with Redis 
- askeeler-test-flask-deployment.yml: creates a deployment for the Flask API
- askeeler-test-flask-service.yml: provides an IP address to interact with Redis 

### Getting the data for the application 
In the root directory of HOMEWORK_06, run the following command:

``` $ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json ```