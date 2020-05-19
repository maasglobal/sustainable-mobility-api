from pytest import approx, fail
from transport_co2.model import Fuel, Mode


# Get list of supported transport modes and fuel types
# by excluding Python API methods
transport_modes = [
    transport_mode
    for transport_mode in Mode.__members__
    if not transport_mode.startswith("_")
]

fuel_types = [
    fuel_type for fuel_type in Fuel.__members__ if not fuel_type.startswith("_")
]


# Mode
def test_allowed_transport_modes():
    """
    Mode enum should only have allowed transport modes
    """

    allowed_transport_modes = [
        "LIGHT_RAIL",
        "SMALL_CAR",
        "LARGE_CAR",
        "SCOOTER",
        "BUS",
        "WALK",
        "BICYCLE",
        "CAR",
        "TRAM",
        "SUBWAY",
        "RAIL",
        "FERRY",
        "CABLE_CAR",
        "GONDOLA",
        "FUNICULAR",
        "TRANSIT",
        "LEG_SWITCH",
        "AIRPLANE",
    ]

    assert transport_modes == allowed_transport_modes


def test_mode_estimate_co2():
    """
    Test CO2 estimates for default transport mode values
    """

    for transport_mode in transport_modes:
        co2_estimate = Mode[transport_mode].estimate_co2(distance_in_km=10)

        if transport_mode == "LIGHT_RAIL":
            assert co2_estimate == approx(140)
        elif transport_mode == "SMALL_CAR":
            assert co2_estimate == approx(1_120)
        elif transport_mode == "LARGE_CAR":
            assert co2_estimate == approx(1_466.6666666666667)
        elif transport_mode == "SCOOTER":
            assert co2_estimate == approx(720)
        elif transport_mode == "BUS":
            assert co2_estimate == approx(679.5275590551181)
        elif transport_mode == "WALK":
            assert co2_estimate == approx(0)
        elif transport_mode == "BICYCLE":
            assert co2_estimate == approx(0)
        elif transport_mode == "CAR":
            assert co2_estimate == approx(1_293.3333333333333)
        elif transport_mode == "TRAM":
            assert co2_estimate == approx(140.0)
        elif transport_mode == "SUBWAY":
            assert co2_estimate == approx(62.400000000000006)
        elif transport_mode == "RAIL":
            assert co2_estimate == approx(140.0)
        elif transport_mode == "FERRY":
            assert co2_estimate == approx(816.0)
        elif transport_mode == "CABLE_CAR":
            assert co2_estimate == approx(140.0)
        elif transport_mode == "GONDOLA":
            assert co2_estimate == approx(140.0)
        elif transport_mode == "FUNICULAR":
            assert co2_estimate == approx(140.0)
        elif transport_mode == "TRANSIT":
            assert co2_estimate == approx(162.26539809714575)
        elif transport_mode == "LEG_SWITCH":
            assert co2_estimate == approx(0)
        elif transport_mode == "AIRPLANE":
            assert co2_estimate == approx(2_850.0)
        else:
            # Make sure we don't miss any test cases
            # or have unexpected members
            fail(f"No test case for { transport_mode }")


def test_mode_estimate_co2_with_occupancy():
    """
    Make sure we get correct result
    when user provides occupancy count
    """

    for transport_mode in transport_modes:
        co2_estimate = Mode[transport_mode].estimate_co2(distance_in_km=10, occupancy=1)

        if transport_mode == "LIGHT_RAIL":
            assert co2_estimate == approx(21_840.0)
        elif transport_mode == "SMALL_CAR":
            assert co2_estimate == approx(1_680.0)
        elif transport_mode == "LARGE_CAR":
            assert co2_estimate == approx(2_200.0)
        elif transport_mode == "SCOOTER":
            assert co2_estimate == approx(864.0)
        elif transport_mode == "BUS":
            assert co2_estimate == approx(8_630.0)
        elif transport_mode == "WALK":
            assert co2_estimate == approx(0)
        elif transport_mode == "BICYCLE":
            assert co2_estimate == approx(0)
        elif transport_mode == "CAR":
            assert co2_estimate == approx(1_940.0)
        elif transport_mode == "TRAM":
            assert co2_estimate == approx(21_840.0)
        elif transport_mode == "SUBWAY":
            assert co2_estimate == approx(1_934.4)
        elif transport_mode == "RAIL":
            assert co2_estimate == approx(21_840.0)
        elif transport_mode == "FERRY":
            assert co2_estimate == approx(74_256.0)
        elif transport_mode == "CABLE_CAR":
            assert co2_estimate == approx(21_840.0)
        elif transport_mode == "GONDOLA":
            assert co2_estimate == approx(21_840.0)
        elif transport_mode == "FUNICULAR":
            assert co2_estimate == approx(21_840.0)
        elif transport_mode == "TRANSIT":
            assert co2_estimate == approx(10801.466666666667)
        elif transport_mode == "LEG_SWITCH":
            assert co2_estimate == approx(0)
        elif transport_mode == "AIRPLANE":
            assert co2_estimate == approx(250800.0)
        else:
            # Make sure we don't miss any test cases
            # or have unexpected members
            fail(f"No test case for { transport_mode }")


# Fuel
def test_allowed_fuel_types():
    """
    Mode enum should only have allowed fuel types
    """

    allowed_fuel_types = [
        "PETROL",
        "ETHANOL_10",
        "ETHANOL_85",
        "DIESEL",
        "BIODIESEL_5",
        "BIODIESEL_20",
    ]

    assert fuel_types == allowed_fuel_types


def test_estimate_fuel_co2_g():
    """
    Make sure we get correct result for default CO2/litre values
    """

    for fuel_type in fuel_types:
        co2_estimate = Fuel[fuel_type].estimate_co2_g(litres=1)

        if fuel_type == "PETROL":
            assert co2_estimate == approx(2_290)
        elif fuel_type == "ETHANOL_10":
            assert co2_estimate == approx(2_210)
        elif fuel_type == "ETHANOL_85":
            assert co2_estimate == approx(1_610)
        elif fuel_type == "DIESEL":
            assert co2_estimate == approx(2_660)
        elif fuel_type == "BIODIESEL_5":
            assert co2_estimate == approx(2_650)
        elif fuel_type == "BIODIESEL_20":
            assert co2_estimate == approx(2_620)
        else:
            # Make sure we don't miss any test cases
            # or have unexpected members
            fail(f"No test case for { fuel_type }")


# Custom co2_g_per_litre
def test_fuel_co2_estimate_custom_co2_g_per_litre():
    co2_g_per_litre = 1_000

    # Test using one litre,
    # so value will match variable
    co2_estimate_g = Fuel.BIODIESEL_20.estimate_co2_g(
        litres=1, co2_g_per_litre=co2_g_per_litre
    )

    assert co2_estimate_g == approx(co2_g_per_litre)
