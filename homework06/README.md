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
** In the root directory of HOMEWORK_06, run the following command: ** 

``` $ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json ```


### Kubernetes deployment 
** Steps to deploying the application on Kubernetes **

Run the following commands to log in to the kubernetes cluster

``` $ ssh <tacc_username>@coe332-k8s.tacc.cloud ```

Next, repeat the following command for each of the 5 .yml files 

``` [user@f5p ~]$ kubectl apply -f <file name> ```

To find the IP adress of the flask service, run 

``` [user@f5p ~]$ kubectl get services ```

Execute a command in the Python debug pod by running 

``` [user@f5p ~]$ kubectl exec -it <python-debug-NAME> /bin/bash ```

Now you're in the Python pod!

To run the services, use the IP adress gotten above and run 

``` curl <IP_Address>:5000/data -X POST ```

then you can run 

``` curl <IP_Address>:5000/data?start=299 -X GET ``` 


Sample output: 
 
 ```
       [
       {
        "name": "Jennifer",
        "id": "10299",
        "recclass": "L5",
        "mass (g)": "539",
        "reclat": "-84.0579",
        "reclong": "69.9994",
        "GeoLocation": "(-84.0579, 69.9994)"
       }
       ]

      ```