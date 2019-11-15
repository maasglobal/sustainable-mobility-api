# -*- coding: utf-8 -*-

"""Library to calculate CO2 (equivalent) emissions for a given transport trip."""

from .__version__ import VERSION, __version__
from .model import Mode
from .estimator import estimate_co2
