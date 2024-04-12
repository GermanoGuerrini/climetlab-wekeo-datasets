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


class sis_water_level_change_indicators_cmip6(Main):
    name = "EO:ECMWF:DAT:SIS_WATER_LEVEL_CHANGE_INDICATORS_CMIP6"
    dataset = "EO:ECMWF:DAT:SIS_WATER_LEVEL_CHANGE_INDICATORS_CMIP6"

    @normalize(
        "variable",
        [
            "annual_mean_of_highest_high_water",
            "annual_mean_of_lowest_low_water",
            "highest_astronomical_tide",
            "lowest_astronomical_tide",
            "mean_sea_level",
            "surge_level",
            "tidal_range",
            "total_water_level",
        ],
        multiple=True,
    )
    @normalize(
        "derived_variable",
        [
            "absolute_change",
            "absolute_value",
            "percentage_change",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "multi_model_ensemble",
            "reanalysis",
            "single_model",
        ],
        multiple=True,
    )
    @normalize(
        "multi_model_ensemble_statistic",
        [
            "ensemble_mean",
            "ensemble_median",
            "ensemble_range",
            "ensemble_standard_deviation",
            "negative_ensemble_counts",
            "positive_ensemble_counts",
        ],
        multiple=True,
    )
    @normalize(
        "model",
        [
            "cmcc_cm2_vhr4",
            "ec_earth3p_hr",
            "hadgem3_gc31_hm",
            "hadgem3_gc31_hm_sst",
        ],
        multiple=True,
    )
    @normalize(
        "statistic",
        [
            "100_year",
            "10_year",
            "10th",
            "1_year",
            "25_year",
            "25th",
            "2_year",
            "50_year",
            "50th",
            "5_year",
            "5th",
            "75_year",
            "75th",
            "90th",
            "95th",
        ],
        multiple=True,
    )
    @normalize(
        "confidence_interval",
        [
            "best_fit",
            "high_bound_confidence_interval",
            "low_bound_confidence_interval",
        ],
        multiple=True,
    )
    @normalize(
        "experiment",
        [
            "future",
            "historical",
        ],
        multiple=True,
    )
    @normalize(
        "period",
        [
            "1950",
            "1951",
            "1951-1980",
            "1952",
            "1953",
            "1954",
            "1955",
            "1956",
            "1957",
            "1958",
            "1959",
            "1960",
            "1961",
            "1962",
            "1963",
            "1964",
            "1965",
            "1966",
            "1967",
            "1968",
            "1969",
            "1970",
            "1971",
            "1972",
            "1973",
            "1974",
            "1975",
            "1976",
            "1977",
            "1978",
            "1979",
            "1980",
            "1981",
            "1982",
            "1983",
            "1984",
            "1985",
            "1985-2014",
            "1986",
            "1987",
            "1988",
            "1989",
            "1990",
            "1991",
            "1992",
            "1993",
            "1994",
            "1995",
            "1996",
            "1997",
            "1998",
            "1999",
            "2000",
            "2001",
            "2002",
            "2003",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
            "2019",
            "2020",
            "2021",
            "2021-2050",
            "2022",
            "2023",
            "2024",
            "2025",
            "2026",
            "2027",
            "2028",
            "2029",
            "2030",
            "2031",
            "2032",
            "2033",
            "2034",
            "2035",
            "2036",
            "2037",
            "2038",
            "2039",
            "2040",
            "2041",
            "2042",
            "2043",
            "2044",
            "2045",
            "2046",
            "2047",
            "2048",
            "2049",
            "2050",
        ],
        multiple=True,
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
        variable,
        derived_variable,
        product_type,
        multi_model_ensemble_statistic,
        model,
        statistic,
        confidence_interval,
        experiment,
        period,
        format_=None,
        limit=None,
    ):
        super().__init__(
            variable=variable,
            derived_variable=derived_variable,
            product_type=product_type,
            multi_model_ensemble_statistic=multi_model_ensemble_statistic,
            model=model,
            statistic=statistic,
            confidence_interval=confidence_interval,
            experiment=experiment,
            period=period,
            format_=format_,
            limit=limit,
        )
