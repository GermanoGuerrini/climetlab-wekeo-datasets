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


class satellite_precipitation_microwave(Main):
    name = "EO:ECMWF:DAT:SATELLITE_PRECIPITATION_MICROWAVE"
    dataset = "EO:ECMWF:DAT:SATELLITE_PRECIPITATION_MICROWAVE"

    @normalize(
        "time_aggregation",
        [
            "daily",
            "monthly",
        ],
    )
    @normalize(
        "year",
        [
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
        "variable",
        [
            "all",
        ],
    )
    @normalize(
        "version",
        [
            "v1.0",
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
        time_aggregation,
        year,
        month,
        day,
        variable="all",
        version="v1.0",
        format_=None,
        limit=None,
    ):
        super().__init__(
            time_aggregation=time_aggregation,
            year=year,
            month=month,
            day=day,
            variable=variable,
            version=version,
            format_=format_,
            limit=limit,
        )
