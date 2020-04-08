from transport_co2.estimator import estimate_co2
from pytest import approx

# Only distance
def test_estimate_co2_bus():
    co2_estimate = estimate_co2(mode="bus", distance_in_km=10)

    assert co2_estimate == approx(679.5275590551181)


def test_estimate_co2_light_rail():
    co2_estimate = estimate_co2(mode="light_rail", distance_in_km=10)

    assert co2_estimate == approx(140)


def test_estimate_co2_small_car():
    co2_estimate = estimate_co2(mode="small_car", distance_in_km=10)

    assert co2_estimate == approx(1120)


def test_estimate_co2_large_car():
    co2_estimate = estimate_co2(mode="large_car", distance_in_km=10)

    assert co2_estimate == approx(1466.6666666666667)


def test_estimate_co2_scooter():
    co2_estimate = estimate_co2(mode="scooter", distance_in_km=10)

    assert co2_estimate == approx(720)


# Distance and occupancy
def test_estimate_co2_bus_with_occupancy():
    co2_estimate = estimate_co2(mode="bus", distance_in_km=10, occupancy=10)

    assert co2_estimate == approx(863)


def test_estimate_co2_light_rail_with_occupancy():
    co2_estimate = estimate_co2(mode="light_rail", distance_in_km=10, occupancy=100)

    assert co2_estimate == approx(218.4)


def test_estimate_co2_small_car_with_occupancy():
    co2_estimate = estimate_co2(mode="small_car", distance_in_km=10, occupancy=2)

    assert co2_estimate == approx(840.0)


def test_estimate_co2_large_car_with_occupancy():
    co2_estimate = estimate_co2(mode="large_car", distance_in_km=10, occupancy=3)

    assert co2_estimate == approx(733.3333333333334)


def test_estimate_co2_scooter_with_occupancy():
    co2_estimate = estimate_co2(mode="scooter", distance_in_km=10, occupancy=2)

    assert co2_estimate == approx(432.0)
