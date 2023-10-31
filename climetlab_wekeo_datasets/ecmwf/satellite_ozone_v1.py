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


class satellite_ozone_v1(Main):
    name = "EO:ECMWF:DAT:SATELLITE_OZONE_V1"
    dataset = "EO:ECMWF:DAT:SATELLITE_OZONE_V1"

    choices = [
        "processing_level",
        "variable",
        "vertical_aggregation",
        "algorithm",
        "format_",
    ]

    string_selects = [
        "month",
        "sensor",
        "version",
        "year",
    ]

    @normalize(
        "month",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        ],
        multiple=True,
    )
    @normalize(
        "sensor",
        [
            "ace",
            "allg",
            "amzm",
            "cllg",
            "cmzm",
            "gome",
            "gome2_a",
            "gome2_b",
            "gome2_c",
            "gomos",
            "haloe",
            "iasi_a_day_time",
            "iasi_a_night_time",
            "iasi_b_day_time",
            "iasi_b_night_time",
            "iasi_c_day_time",
            "iasi_c_night_time",
            "merged_uv",
            "mipas",
            "mls",
            "msr",
            "omi",
            "omps",
            "osiris",
            "saber",
            "sage_2",
            "sage_3",
            "sciamachy",
            "smr",
            "tropomi",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "v0001",
            "v0002",
            "v0003",
            "v0004",
            "v0005",
            "v0006",
            "v0007",
            "v0008",
            "v0020",
            "v0021",
            "v0022",
            "v0023",
            "v0024",
            "v0025",
            "v0100",
            "v0101",
            "v0200",
            "v0300",
            "v0400",
            "v0500",
            "v0600",
            "v0700",
            "v0800",
            "v0900",
            "v1000",
            "v1100",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
            "2022",
            "2023",
        ],
        multiple=True,
    )
    @normalize(
        "processing_level",
        [
            "level_3",
            "level_4",
        ],
    )
    @normalize(
        "variable",
        [
            "anomaly_of_mole_concentration_of_ozone_in_air",
            "atmosphere_mole_content_of_ozone",
            "mole_concentration_of_ozone_in_air",
            "mole_content_of_ozone_in_atmosphere_layer",
            "mole_fraction_of_ozone_in_air",
        ],
    )
    @normalize(
        "vertical_aggregation",
        [
            "total_column",
            "tropospheric_column_0_6_km",
            "vertical_profiles_from_limb_sensors",
            "vertical_profiles_from_nadir_sensors",
        ],
    )
    @normalize(
        "algorithm",
        [
            "ubr",
            "usask",
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
        month,
        sensor,
        version,
        year,
        processing_level=None,
        variable=None,
        vertical_aggregation=None,
        algorithm=None,
        format_=None,
    ):
        super().__init__(
            month=month,
            sensor=sensor,
            version=version,
            year=year,
            processing_level=processing_level,
            variable=variable,
            vertical_aggregation=vertical_aggregation,
            algorithm=algorithm,
            format_=format_,
        )
