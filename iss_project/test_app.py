import pytest
from app import *

read_data_to_dict()


def test_help():
    assert isinstance(help(), str) == True


def test_get_all_epochs():
    assert isinstance(get_all_epochs(), str) == True


def test_get_epoch_data():
    assert isinstance(get_epoch_data("hello"), dict) == True


def test_get_all_countries():
    assert isinstance(get_all_countries(), dict) == True


def test_get_country_data():
    assert isinstance(get_country_data("hello"), str) == True


def test_get_all_regions():
    assert isinstance(get_all_regions("hello"), dict) == True


def test_get_region_data():
    assert isinstance(get_region_data("hello", "hello"), str) == True


def test_get_all_cities():
    assert isinstance(get_all_cities("hello", "hello"), dict) == True


def test_get_city_data():
    assert isinstance(get_city_data("hello", "hello", "hello"), str) == True
