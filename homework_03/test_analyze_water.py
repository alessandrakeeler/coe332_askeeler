from analyze_water import *
import pytest

with open("turbidity_data.json", 'r') as f:
    water_data = json.load(f)

date = "2022-02-12 06:00"


def test_get_average_values():
    volume, calibration, detector = get_average_values(date, water_data)
    assert isinstance(volume, float)
    assert isinstance(calibration, float)
    assert isinstance(detector, float)

    with pytest.raises(KeyError):
        get_average_values(date, {})

    with pytest.raises(TypeError):
        get_average_values("2022-09-39", water_data)


def test_get_turbidity():
    volume, calibration, detector = get_average_values(date, water_data)
    t = get_turbidity(calibration, detector)
    assert isinstance(t, float)
    assert (get_turbidity(0, 0) == 0)
    with pytest.raises(TypeError):
        get_turbidity(True, False)



