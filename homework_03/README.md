## Homework 3
Exploring the potability of water by calculating the turbidity of hourly samples. 

### Getting started! 
1. Download the turbidity data from [this link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json)
2. Place it in the */homework_03* folder, and name it turbidity_data.json 

### Functions

     get_average_values(start_date, water_dictionary) -> float
This function computes the average values of volume, calibration constant, and detector constant, given a starting date in the format  *"YEAR/MM/DD HR:00"*, where the time is in military format (24:00 clock).
The function then averages the most recent 5 datapoints, starting from that date. It returns 3 float values, *average_volume, average_calibration, and average_detector* which are used in later functions. 


    get_turbidity(calibration_constant, detector) -> float
This function calculates the turbidity of the water sample, from the average calculated values of calibration_constant and detector. It is used by check_potability to determine where a sample is drinkable or not. 

    `minimum_time(calbration_constant, detector) -> float`
This function determines the minimum time the water sample needs to return to a drinkable turbidity level again. 

    `output_string(data, date)`
This function is where all the magic happens. It accepts the start date and the dictionary of data, then runs all other functions and formats output strings for easy readibilty of results. 
### Using this repository 
All functions must be run from the directory level homework_03

Running the analysis script
1. Run `chmod u+x analyze_water.py` in the terminal to create an executable version of the water analysis script 
2. Run ` ./python analyze_water.py` in the terminal. You will be prompted to enter a date, either enter one in the form desired, or hit enter to use the default date.

Running the testing script
1. Run `pytest test_analyze_water.py` in the terminal


### Interpreting results 

    From date: 2022-02-12 06:00 
    Average turbidity based on most recent five measurements: 1.16896116 ntu
    WARNING:root:Turbidity is above threshold for safe use
    Minimum time required to return below a safe threshold = 7.727452291702236 hours 

In this example, the start date was the default date set by me, 2022-02-12 06:00,
the average turbidity is above the desired limit (1.0 ntu), so there is a warning that the turbidity is above the drinkable threshold. 
The last line shows how long it will take for the water to become drinkable again. 
