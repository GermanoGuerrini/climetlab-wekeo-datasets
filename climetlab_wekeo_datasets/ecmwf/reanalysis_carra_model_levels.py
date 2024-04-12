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


class reanalysis_carra_model_levels(Main):
    name = "EO:ECMWF:DAT:REANALYSIS_CARRA_MODEL_LEVELS"
    dataset = "EO:ECMWF:DAT:REANALYSIS_CARRA_MODEL_LEVELS"

    @normalize(
        "domain",
        [
            "east_domain",
            "west_domain",
        ],
    )
    @normalize(
        "variable",
        [
            "cloud_cover",
            "graupel",
            "specific_cloud_ice_water_content",
            "specific_cloud_liquid_water_content",
            "specific_cloud_rain_water_content",
            "specific_cloud_snow_water_content",
            "specific_humidity",
            "temperature",
            "turbulent_kinetic_energy",
            "u_component_of_wind",
            "v_component_of_wind",
        ],
        multiple=True,
    )
    @normalize(
        "model_level",
        [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
            "32",
            "33",
            "34",
            "35",
            "36",
            "37",
            "38",
            "39",
            "40",
            "41",
            "42",
            "43",
            "44",
            "45",
            "46",
            "47",
            "48",
            "49",
            "50",
            "51",
            "52",
            "53",
            "54",
            "55",
            "56",
            "57",
            "58",
            "59",
            "60",
            "61",
            "62",
            "63",
            "64",
            "65",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "analysis",
            "forecast",
        ],
    )
    @normalize(
        "time",
        [
            "00:00",
            "03:00",
            "06:00",
            "09:00",
            "12:00",
            "15:00",
            "18:00",
            "21:00",
        ],
        multiple=True,
    )
    @normalize(
        "leadtime_hour",
        [
            "1",
            "2",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
            "2024",
        ],
        multiple=True,
    )
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
        "day",
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
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
        ],
        multiple=True,
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
        ],
    )
    def __init__(
        self,
        domain,
        variable,
        model_level,
        product_type,
        time,
        leadtime_hour,
        year,
        month,
        day,
        format_=None,
        limit=None,
    ):
        super().__init__(
            domain=domain,
            variable=variable,
            model_level=model_level,
            product_type=product_type,
            time=time,
            leadtime_hour=leadtime_hour,
            year=year,
            month=month,
            day=day,
            format_=format_,
            limit=limit,
        )
