# Homework 4- Containerizing the investigation into meteorite landing data
## This repository explores the hemispheres in which meteorites were found, as well as computes the average mass of all meteorites found 

### Items in this repository
1. ml_data_analysis.py -> This is the main function file of the repository. It calculates average mass of samples as well as what hemisphere they were found in 
2. test_data_analysis.py -> This is a pytest file that tests ml_data_analysis.py
3. Meteorite_Landing.json -> This is the data that you will need to download and place in the repo (instructions below)
4. Dockerfile -> This is the file that contains the build commands for this repository 


### Step 1: Configuring the data 
To get the data needed for this project (or your own data) go about it this way 
Run the command (to get the data for this project)

```wget https://raw.githubusercontent.com/tacc/coe-332-sp22/main/docs/unit04/scripts/Meteorite_Landings.json```

Or add your custom data with the name ```Meteorite_Landing.json```


### Step 2: Setting up the docker image. (Option 1)
If you choose to pull from a pre-existing docker image, run the command 
```docker pull alessandrakeeler/hw4```

```docker build -t username-docker/hw4:1.0 . ```

This will build the docker image locally. To run the interactive shell, use the command 
Your output should look like this:
```[+] Building 0.7s (12/12) FINISHED                                                                        
 => [internal] load build definition from Dockerfile                                                 0.0s
 => => transferring dockerfile: 340B                                                                 0.0s
 => [internal] load .dockerignore                                                                    0.0s
 => => transferring context: 2B                                                                      0.0s
 => [internal] load metadata for docker.io/library/centos:7.9.2009                                   0.0s
 => [internal] load build context                                                                    0.0s
 => => transferring context: 76B                                                                     0.0s
 => [1/7] FROM docker.io/library/centos:7.9.2009                                                     0.0s
 => CACHED [2/7] RUN yum update -y &&     yum install -y python3                                     0.0s
 => CACHED [3/7] RUN pip3 install pytest==7.0.0                                                      0.0s
 => CACHED [4/7] COPY ml_data_analysis.py /code/ml_data_analysis.py                                  0.0s
 => CACHED [5/7] COPY test_ml_data.py /code/test_ml_data.py                                          0.0s
 => CACHED [6/7] RUN chmod +rx /code/ml_data_analysis.py                                             0.0s
 => [7/7] RUN pytest /code/test_ml_data.py                                                           0.6s
 => exporting to image                                                                               0.0s
 => => exporting layers                                                                              0.0s
 => => writing image sha256:0748acf88d37cf417d52f31762c7b3d2e6116c36e1ed3b5b50fa6b0eb11f64ce         0.0s
 => => naming to docker.io/alessandrakeeler/hw4:1.0                                                  0.0s
```


Next, enter the interactive shell by running

```docker run --rm -it alessandrakeeler/hw4:1.0 /bin/bash```



### Step 3: Running the ml_data_analysis.py script 
The command to run the script is

```ml_data_analysis.py /code/Meteorite_Landings.json```

The output should look like this:


### Step 4: Testing ml_data_analalysis.py 
Run the pytest command while in the code directory! 





