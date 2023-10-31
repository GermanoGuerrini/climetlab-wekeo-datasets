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


class efas_reforecast(Main):
    name = "EO:ECMWF:DAT:EFAS_REFORECAST"
    dataset = "EO:ECMWF:DAT:EFAS_REFORECAST"

    choices = [
        "variable",
        "model_levels",
        "format_",
    ]

    string_selects = [
        "hday",
        "hmonth",
        "hyear",
        "leadtime_hour",
        "product_type",
        "soil_level",
    ]

    @normalize(
        "hday",
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
        "hmonth",
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
        "hyear",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "leadtime_hour",
        [
            "0",
            "1002",
            "1008",
            "1014",
            "102",
            "1020",
            "1026",
            "1032",
            "1038",
            "1044",
            "1050",
            "1056",
            "1062",
            "1068",
            "1074",
            "108",
            "1080",
            "1086",
            "1092",
            "1098",
            "1104",
            "114",
            "12",
            "120",
            "126",
            "132",
            "138",
            "144",
            "150",
            "156",
            "162",
            "168",
            "174",
            "18",
            "180",
            "186",
            "192",
            "198",
            "204",
            "210",
            "216",
            "222",
            "228",
            "234",
            "24",
            "240",
            "246",
            "252",
            "258",
            "264",
            "270",
            "276",
            "282",
            "288",
            "294",
            "30",
            "300",
            "306",
            "312",
            "318",
            "324",
            "330",
            "336",
            "342",
            "348",
            "354",
            "36",
            "360",
            "366",
            "372",
            "378",
            "384",
            "390",
            "396",
            "402",
            "408",
            "414",
            "42",
            "420",
            "426",
            "432",
            "438",
            "444",
            "450",
            "456",
            "462",
            "468",
            "474",
            "48",
            "480",
            "486",
            "492",
            "498",
            "504",
            "510",
            "516",
            "522",
            "528",
            "534",
            "54",
            "540",
            "546",
            "552",
            "558",
            "564",
            "570",
            "576",
            "582",
            "588",
            "594",
            "6",
            "60",
            "600",
            "606",
            "612",
            "618",
            "624",
            "630",
            "636",
            "642",
            "648",
            "654",
            "66",
            "660",
            "666",
            "672",
            "678",
            "684",
            "690",
            "696",
            "702",
            "708",
            "714",
            "72",
            "720",
            "726",
            "732",
            "738",
            "744",
            "750",
            "756",
            "762",
            "768",
            "774",
            "78",
            "780",
            "786",
            "792",
            "798",
            "804",
            "810",
            "816",
            "822",
            "828",
            "834",
            "84",
            "840",
            "846",
            "852",
            "858",
            "864",
            "870",
            "876",
            "882",
            "888",
            "894",
            "90",
            "900",
            "906",
            "912",
            "918",
            "924",
            "930",
            "936",
            "942",
            "948",
            "954",
            "96",
            "960",
            "966",
            "972",
            "978",
            "984",
            "990",
            "996",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "control_forecast",
            "ensemble_perturbed_forecasts",
        ],
        multiple=True,
    )
    @normalize(
        "soil_level",
        [
            "1",
            "2",
            "3",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "elevation",
            "field_capacity",
            "river_discharge_in_the_last_6_hours",
            "snow_depth_water_equivalent",
            "soil_depth",
            "upstream_area",
            "volumetric_soil_moisture",
            "wilting_point",
        ],
    )
    @normalize(
        "model_levels",
        [
            "soil_levels",
            "surface_level",
        ],
    )
    @normalize(
        "format_",
        [
            "grib.zip",
            "netcdf4.zip",
        ],
    )
    def __init__(
        self,
        hday,
        hmonth,
        hyear,
        leadtime_hour,
        product_type,
        soil_level,
        variable=None,
        model_levels=None,
        format_=None,
    ):
        super().__init__(
            hday=hday,
            hmonth=hmonth,
            hyear=hyear,
            leadtime_hour=leadtime_hour,
            product_type=product_type,
            soil_level=soil_level,
            variable=variable,
            model_levels=model_levels,
            format_=format_,
        )
