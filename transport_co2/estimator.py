from typing import Optional, Union
from .model import Mode


def estimate_co2(
    mode: Union[str, Mode], distance_in_km: float, occupancy: Optional[float] = None
) -> float:
    """
        Estimate CO2 usage for transport mode based on KM and optional vehicle occupancy.

        Keyword arguments:
            mode -- vehicle mode (limited to allowed values)
            distance_in_km -- distance for the trip in kilometers
            occupancy -- optional vehicle occupancy (uses average occupancy if falsey)
        """
    if isinstance(mode, str):
        mode = Mode[mode.upper()]

    return mode.estimate_co2(distance_in_km, occupancy)

