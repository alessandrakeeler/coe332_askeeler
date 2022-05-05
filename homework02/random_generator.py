import json
import random


def generate_random_lat():
    return random.uniform(16.0, 18.0)


def generate_random_long():
    return random.uniform(82.0, 84.0)


def generate_random_composition(compositions):
    return random.choice(compositions)


def generate_json(num_sites):
    site_dictionary_list = []
    compositions = ["stony", "iron", "stony-iron"]

    for i in range(num_sites):
        site_dictionary_list.append(
            {"site_id": i + 1, "latitude": generate_random_lat(), "longitude": generate_random_long(),
             "composition": generate_random_composition(compositions)})

    final_dict = {"sites": site_dictionary_list}

    with open('ml_data.json', 'w') as outfile:
        json.dump(final_dict, outfile)


generate_json(5)
