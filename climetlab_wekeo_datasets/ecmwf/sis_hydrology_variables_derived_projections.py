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


class sis_hydrology_variables_derived_projections(Main):
    name = "EO:ECMWF:DAT:SIS_HYDROLOGY_VARIABLES_DERIVED_PROJECTIONS"
    dataset = "EO:ECMWF:DAT:SIS_HYDROLOGY_VARIABLES_DERIVED_PROJECTIONS"

    choices = [
        "product_type",
        "variable_type",
        "time_aggregation",
        "rcm",
        "gcm",
        "format_",
    ]

    string_selects = [
        "ensemble_member",
        "experiment",
        "hydrological_model",
        "period",
        "variable",
    ]

    @normalize(
        "ensemble_member",
        [
            "r12i1p1",
            "r1i1p1",
            "r2i1p1",
        ],
        multiple=True,
    )
    @normalize(
        "experiment",
        [
            "degree_scenario",
            "historical",
            "rcp_2_6",
            "rcp_4_5",
            "rcp_8_5",
        ],
        multiple=True,
    )
    @normalize(
        "hydrological_model",
        [
            "e_hypecatch_m00",
            "e_hypecatch_m01",
            "e_hypecatch_m02",
            "e_hypecatch_m03",
            "e_hypecatch_m04",
            "e_hypecatch_m05",
            "e_hypecatch_m06",
            "e_hypecatch_m07",
            "e_hypegrid",
            "vic_wur",
        ],
        multiple=True,
    )
    @normalize(
        "period",
        [
            "1971",
            "1971_1980",
            "1971_2000",
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
            "1981_1990",
            "1982",
            "1983",
            "1984",
            "1985",
            "1986",
            "1987",
            "1988",
            "1989",
            "1990",
            "1991",
            "1991_2000",
            "1992",
            "1993",
            "1994",
            "1995",
            "1996",
            "1997",
            "1998",
            "1999",
            "1_5_c",
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
            "2011_2020",
            "2011_2040",
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
            "2021_2030",
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
            "2031_2040",
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
            "2041_2050",
            "2041_2070",
            "2042",
            "2043",
            "2044",
            "2045",
            "2046",
            "2047",
            "2048",
            "2049",
            "2050",
            "2051",
            "2051_2060",
            "2052",
            "2053",
            "2054",
            "2055",
            "2056",
            "2057",
            "2058",
            "2059",
            "2060",
            "2061",
            "2061_2070",
            "2062",
            "2063",
            "2064",
            "2065",
            "2066",
            "2067",
            "2068",
            "2069",
            "2070",
            "2071",
            "2071_2080",
            "2071_2100",
            "2072",
            "2073",
            "2074",
            "2075",
            "2076",
            "2077",
            "2078",
            "2079",
            "2080",
            "2081",
            "2081_2090",
            "2082",
            "2083",
            "2084",
            "2085",
            "2086",
            "2087",
            "2088",
            "2089",
            "2090",
            "2091",
            "2091_2100",
            "2092",
            "2093",
            "2094",
            "2095",
            "2096",
            "2097",
            "2098",
            "2099",
            "2100",
            "2_0_c",
            "3_0_c",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "aridity_actual",
            "aridity_potential",
            "flood_recurrence_10_years_return_period",
            "flood_recurrence_2_years_return_period",
            "flood_recurrence_50_years_return_period",
            "flood_recurrence_5_years_return_period",
            "maximum_river_discharge",
            "mean_runoff",
            "mean_soil_moisture",
            "minimum_river_discharge",
            "river_discharge",
            "total_nitrogen_concentration_in_catchments",
            "total_nitrogen_concentration_in_local_streams",
            "total_nitrogen_load_in_catchments",
            "total_phosphorus_concentration_in_catchments",
            "total_phosphorus_concentration_in_local_streams",
            "total_phosphorus_load_in_catchments",
            "water_temperature_in_catchments",
            "water_temperature_in_local_streams",
            "wetness_actual",
            "wetness_potential",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "climate_impact_indicators",
            "essential_climate_variables",
        ],
    )
    @normalize(
        "variable_type",
        [
            "absolute_change_from_reference_period",
            "absolute_values",
            "relative_change_from_reference_period",
        ],
    )
    @normalize(
        "time_aggregation",
        [
            "annual_mean",
            "daily",
            "monthly_mean",
        ],
    )
    @normalize(
        "rcm",
        [
            "cclm4_8_17",
            "csc_remo2009",
            "racmo22e",
            "rca4",
        ],
    )
    @normalize(
        "gcm",
        [
            "ec_earth",
            "hadgem2_es",
            "mpi_esm_lr",
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
        ensemble_member,
        experiment,
        hydrological_model,
        period,
        variable,
        product_type,
        variable_type,
        time_aggregation,
        rcm,
        gcm,
        format_,
    ):
        super().__init__(
            ensemble_member=ensemble_member,
            experiment=experiment,
            hydrological_model=hydrological_model,
            period=period,
            variable=variable,
            product_type=product_type,
            variable_type=variable_type,
            time_aggregation=time_aggregation,
            rcm=rcm,
            gcm=gcm,
            format_=format_,
        )
