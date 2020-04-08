from transport_co2.estimator import estimate_co2


def test_estimate_co2_bus():
    co2_estimate = estimate_co2(mode="bus", distance_in_km=10)

    assert co2_estimate == 679.5275590551181


def test_estimate_co2_light_rail():
    co2_estimate = estimate_co2(mode="light_rail", distance_in_km=10)

    assert co2_estimate == 140


def test_estimate_co2_small_car():
    co2_estimate = estimate_co2(mode="small_car", distance_in_km=10)

    assert co2_estimate == 1120


def test_estimate_co2_large_car():
    co2_estimate = estimate_co2(mode="large_car", distance_in_km=10)

    assert co2_estimate == 1466.6666666666667


def test_estimate_co2_scooter():
    co2_estimate = estimate_co2(mode="scooter", distance_in_km=10)

    assert co2_estimate == 720
