#Homework #2, COE 332 
###Investigating the distance/time traveled by the mars rover between different collection sites.

####How to use this folder.

- random_generator.py
  - This file generates a random dictionary with arguments latitude (range 16.0-18.0), longitude (range 82.0-84.0), and composition (stony, iron, or stony iron)
  - When executed, this file generates ml_data.json

To run this file, use 
```
  python3 random_generator.py
```

- distance_calculator.py
  - This file contains the methods compute_time and calc_gcd
    - compute_time takes the argument of the distance between two points, calc_gcd takes 2 latitiudes and longitudes and calculates the distances between them 
    
To run this file, use 
```
  python3 distance_calculator.py
```