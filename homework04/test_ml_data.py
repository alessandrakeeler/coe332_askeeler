from ml_data_analysis import *
import pytest

ml_data = {}
ml_data['info'] = []
ml_data['info'].append({'mass': 2})
ml_data['info'].append({'mass': 4})


def test_compute_average_mass():
    mass = compute_average_mass(ml_data['info'], 'mass')
    assert (mass != 0)
    assert (mass > 0)
    assert isinstance(mass, float)
    assert (mass == 3)


def test_compute_mass_exception():
    with pytest.raises(KeyError):
        compute_average_mass([{'mass': 1}], 'mss')


def test_check_hemisphere():
    assert check_hemisphere(1, 5) == "Northern & Eastern"
    assert check_hemisphere(0.1, 5) == "Northern & Eastern"
    assert check_hemisphere(2, -1) == "Northern & Western"
    assert check_hemisphere(1, 1) == "Northern & Eastern"


def test_count_classes():
    assert isinstance(count_classes(ml_data['info'], 'mass'), dict) == True
    assert isinstance(count_classes(ml_data['info'], 'mass'), str) == False
    assert isinstance(count_classes(ml_data['info'], 'mass'), float) == False


def count_classes_exceptions():
    with pytest.raises(KeyError):
        count_classes([{'mass': 1}], 'mas')
