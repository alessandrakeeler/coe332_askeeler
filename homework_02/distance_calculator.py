import json 
import math 

composition_times = {'stony': 1, 'iron' : 2, 'stony-iron': 3}

def compute_time(distance):
    return distance / 10



def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    mars_radius = 3389.5
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )



def main():
    with open('ml_data.json', 'r') as f:
        ml_data = json.load(f)

    total_travel_time = 0
    total_travel_distance = 0
    last_latitude = 16.0
    last_longitude = 82.0 
    stop = 1 

    for s in ml_data['sites']:
        
        next_latitude = s['latitude']
        next_longitude = s['longitude']
        composition = s['composition']



        dist = calc_gcd(last_latitude, next_latitude, last_longitude, next_longitude)
        time = compute_time(dist)
        
            ## shouldn't be bigger than 17 hours 
        collection_time = composition_times[composition]


        print(f"leg =  {stop} , distance traveled = {dist}, time to travel = {time} hrs, time to sample = {collection_time} hrs")
        print()
        total_travel_time = total_travel_time + time + collection_time
        total_travel_distance +=dist

        stop +=1
        last_latitude = next_latitude
        last_longitude = next_longitude

        

main()