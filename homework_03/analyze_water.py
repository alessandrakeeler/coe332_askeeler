#!/usr/bin/env python3
import logging
import json
from statistics import mean
import math


def get_average_values(start_date: str, water_dictionary: dict):
    """This function returns the average water turbidity values for 5 days before a specified start date.

    Expects an input of a start_date of form "YEAR-MM-DD 12:00" (military time), and calculates the
    average of the three numerical values and returns them

    :param start_date: string
    :param water_dictionary: dictionary
    :return: average_volume:float
    :return: average_calibration_constant: float
    :return: average_detector_current: float
    """

    lst = water_dictionary['turbidity_data']
    start_index = next((index for (index, d) in enumerate(lst) if d["datetime"] == start_date), None)

    average_volume = mean([x['sample_volume'] for ind, x in enumerate(lst) if start_index + 1 > ind > start_index - 5])
    average_calibration_constant = mean(
        [x['calibration_constant'] for ind, x in enumerate(lst) if start_index + 1 > ind > start_index - 5])
    average_detector_current = mean(
        [x['detector_current'] for ind, x in enumerate(lst) if start_index + 1 > ind > start_index - 5])

    return average_volume, average_calibration_constant, average_detector_current


def get_turbidity(calibration_constant: float, detector: float) -> float:
    """ This function uses equation 1 to calculate the turbidity of the water to see if it was potable.

    :param calibration_constant: float
    :param detector: float
    :return: float
    """

    return calibration_constant * detector


def check_potability(calibration_constant, detector) -> bool:
    """This function utilizes the get_turbidity function to determine whether or not the water is potable

    Expects an input of the average calibration constant, detector constant, and returns whether or not the water is potable (bool)

    :param calibration_constant: float
    :param detector: float
    :return: potability: boolean

    """

    return get_turbidity(calibration_constant, detector) < 1.0


def minimum_time(calibration_constant, detector) -> float:
    """ This function uses equation 2 to calculate the time in hours it will take for the water to become potable again.

    Expects the average calibration constant and the average detector value, and returns a float time in hours.

    :param calibration_constant: float
    :param detector: float
    :return: float
    """

    t = calibration_constant * detector
    b = math.log((1 / t), 0.98)
    return b


def output_string(data, date):
    """ This function formats the output string and gives the result for a given dictionary and date

    :param data: dict
    :param date: string
    :return: None
    """
    if date == "":
        date = "2022-02-12 06:00"

    volume, calibration, detector = get_average_values(date, data)
    turbidity = get_turbidity(calibration, detector)
    print(f"For date: {date} \n")
    if check_potability(calibration, detector):
        print(f" Average turbidity based on most recent five measurements: {turbidity} ntu")
        print()
        print("Info: Turbidity is below threshold for safe use \n Minimum time required to return below a safe "
              "threshold = 0 hours")

    else:
        print(f" Average turbidity based on most recent five measurements: {turbidity} ntu")
        print(f"Warning: Turbidity is above threshold for safe use \n Minimum time required to return below a safe "
              f"threshold = {minimum_time(calibration, detector)} hours "
              )


def main():
    with open("turbidity_data.json", 'r') as f:
        water_data = json.load(f)

    date = input("Enter the start date/time in the form year-mm-dd tt:00 , where tt is in 24:00 time. Hit enter to "
                 "use default date.  ")

    output_string(water_data, date)

    return


if __name__ == "__main__":
    main()
