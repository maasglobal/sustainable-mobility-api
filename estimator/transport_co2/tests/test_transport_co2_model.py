from pytest import approx
from transport_co2.model import Fuel, Mode

# Mode

# Only distance


def test_estimate_co2_bus():
    co2_estimate = Mode.BUS.estimate_co2(distance_in_km=10)

    assert co2_estimate == approx(679.5275590551181)


def test_estimate_co2_light_rail():
    co2_estimate = Mode.LIGHT_RAIL.estimate_co2(distance_in_km=10)

    assert co2_estimate == approx(140)


def test_estimate_co2_small_car():
    co2_estimate = Mode.SMALL_CAR.estimate_co2(distance_in_km=10)

    assert co2_estimate == approx(1120)


def test_estimate_co2_large_car():
    co2_estimate = Mode.LARGE_CAR.estimate_co2(distance_in_km=10)

    assert co2_estimate == approx(1466.6666666666667)


def test_estimate_co2_scooter():
    co2_estimate = Mode.SCOOTER.estimate_co2(distance_in_km=10)

    assert co2_estimate == approx(720)


## Distance and occupancy
def test_estimate_co2_bus_with_occupancy():
    co2_estimate = Mode.BUS.estimate_co2(distance_in_km=10, occupancy=10)

    assert co2_estimate == approx(863)


def test_estimate_co2_light_rail_with_occupancy():
    co2_estimate = Mode.LIGHT_RAIL.estimate_co2(
        distance_in_km=10, occupancy=100)

    assert co2_estimate == approx(218.4)


def test_estimate_co2_small_car_with_occupancy():
    co2_estimate = Mode.SMALL_CAR.estimate_co2(distance_in_km=10, occupancy=2)

    assert co2_estimate == approx(840.0)


def test_estimate_co2_large_car_with_occupancy():
    co2_estimate = Mode.LARGE_CAR.estimate_co2(distance_in_km=10, occupancy=3)

    assert co2_estimate == approx(733.3333333333334)


def test_estimate_co2_scooter_with_occupancy():
    co2_estimate = Mode.SCOOTER.estimate_co2(distance_in_km=10, occupancy=2)

    assert co2_estimate == approx(432.0)


# Fuel

# Only litres
def test_fuel_co2_estimate_petrol():
    co2_estimate_g = Fuel.PETROL.estimate_co2_g(litres=1)

    assert co2_estimate_g == approx(2_290)


def test_fuel_co2_estimate_ethanol_10():
    co2_estimate_g = Fuel.ETHANOL_10.estimate_co2_g(litres=1)

    assert co2_estimate_g == approx(2_210)


def test_fuel_co2_estimate_ethanol_85():
    co2_estimate_g = Fuel.ETHANOL_85.estimate_co2_g(litres=1)

    assert co2_estimate_g == approx(1_610)


def test_fuel_co2_estimate_diesel():
    co2_estimate_g = Fuel.DIESEL.estimate_co2_g(litres=1)

    assert co2_estimate_g == approx(2_660)


def test_fuel_co2_estimate_biodiesel_5():
    co2_estimate_g = Fuel.BIODIESEL_5.estimate_co2_g(litres=1)

    assert co2_estimate_g == approx(2_650)


def test_fuel_co2_estimate_biodiesel_20():
    co2_estimate_g = Fuel.BIODIESEL_20.estimate_co2_g(litres=1)

    assert co2_estimate_g == approx(2_620)


# Custom co2_g_per_litre
def test_fuel_co2_estimate_custom_co2_g_per_litre():
    co2_g_per_litre = 1_000
    co2_estimate_g = Fuel.BIODIESEL_20.estimate_co2_g(
        litres=1, co2_g_per_litre=co2_g_per_litre)

    assert co2_estimate_g == approx(1_000)
