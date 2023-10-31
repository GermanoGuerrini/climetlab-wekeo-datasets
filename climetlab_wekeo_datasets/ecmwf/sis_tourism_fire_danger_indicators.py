#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.ecmwf.main import Main


class sis_tourism_fire_danger_indicators(Main):
    name = "EO:ECMWF:DAT:SIS_TOURISM_FIRE_DANGER_INDICATORS"
    dataset = "EO:ECMWF:DAT:SIS_TOURISM_FIRE_DANGER_INDICATORS"

    choices = [
        "time_aggregation",
        "product_type",
        "experiment",
        "version",
        "format_",
    ]

    string_selects = [
        "gcm_model",
        "period",
        "variable",
    ]

    @normalize(
        "gcm_model",
        [
            "cnrm_cm5",
            "ec_earth",
            "hadgem2_es",
            "ipsl_cm5a_mr",
            "mpi_esm_lr",
            "noresm1_m",
        ],
        multiple=True,
    )
    @normalize(
        "period",
        [
            "1970",
            "1971",
            "1971_1975",
            "1972",
            "1973",
            "1974",
            "1975",
            "1976",
            "1976_1980",
            "1977",
            "1978",
            "1979",
            "1980",
            "1981",
            "1981_1982",
            "1981_1985",
            "1981_2000",
            "1981_2005",
            "1982",
            "1983",
            "1984",
            "1985",
            "1986",
            "1986_1990",
            "1987",
            "1988",
            "1989",
            "1990",
            "1991",
            "1991_1995",
            "1992",
            "1993",
            "1994",
            "1995",
            "1996",
            "1996_2000",
            "1997",
            "1998",
            "1999",
            "2000",
            "2001",
            "2001_2005",
            "2002",
            "2003",
            "2004",
            "2005",
            "2006",
            "2006_2010",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2011_2015",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2016_2020",
            "2017",
            "2018",
            "2019",
            "2020",
            "2021",
            "2021_2025",
            "2021_2040",
            "2022",
            "2023",
            "2024",
            "2025",
            "2026",
            "2026_2030",
            "2027",
            "2028",
            "2029",
            "2030",
            "2031",
            "2031_2035",
            "2032",
            "2033",
            "2034",
            "2035",
            "2036",
            "2036_2040",
            "2037",
            "2038",
            "2039",
            "2040",
            "2041",
            "2041_2045",
            "2041_2060",
            "2042",
            "2043",
            "2044",
            "2045",
            "2046",
            "2046_2050",
            "2047",
            "2048",
            "2049",
            "2050",
            "2051",
            "2051_2055",
            "2052",
            "2053",
            "2054",
            "2055",
            "2056",
            "2056_2060",
            "2057",
            "2058",
            "2059",
            "2060",
            "2061",
            "2061_2065",
            "2062",
            "2063",
            "2064",
            "2065",
            "2066",
            "2066_2070",
            "2067",
            "2068",
            "2069",
            "2070",
            "2071",
            "2071_2075",
            "2072",
            "2073",
            "2074",
            "2075",
            "2076",
            "2076_2080",
            "2077",
            "2078",
            "2078_2097",
            "2079",
            "2079_2098",
            "2080",
            "2081",
            "2081_2085",
            "2082",
            "2083",
            "2084",
            "2085",
            "2086",
            "2086_2090",
            "2087",
            "2088",
            "2089",
            "2090",
            "2091",
            "2091_2095",
            "2092",
            "2093",
            "2094",
            "2095",
            "2096",
            "2096_2098",
            "2097",
            "2098",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "daily_fire_weather_index",
            "number_of_days_with_high_fire_danger",
            "number_of_days_with_moderate_fire_danger",
            "number_of_days_with_very_high_fire_danger",
            "seasonal_fire_weather_index",
        ],
        multiple=True,
    )
    @normalize(
        "time_aggregation",
        [
            "annual_indicators",
            "daily_indicators",
            "seasonal_indicators",
        ],
    )
    @normalize(
        "product_type",
        [
            "multi_model_best_case",
            "multi_model_mean_case",
            "multi_model_worst_case",
            "single_model",
        ],
    )
    @normalize(
        "experiment",
        [
            "historical",
            "rcp2_6",
            "rcp4_5",
            "rcp8_5",
        ],
    )
    @normalize(
        "version",
        [
            "v1_0",
            "v2_0",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        gcm_model,
        period,
        variable,
        time_aggregation=None,
        product_type=None,
        experiment=None,
        version=None,
        format_=None,
    ):
        super().__init__(
            gcm_model=gcm_model,
            period=period,
            variable=variable,
            time_aggregation=time_aggregation,
            product_type=product_type,
            experiment=experiment,
            version=version,
            format_=format_,
        )
