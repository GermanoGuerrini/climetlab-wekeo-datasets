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


class reanalysis_carra_pressure_levels(Main):
    name = "EO:ECMWF:DAT:REANALYSIS_CARRA_PRESSURE_LEVELS"
    dataset = "EO:ECMWF:DAT:REANALYSIS_CARRA_PRESSURE_LEVELS"

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
        "domain",
        [
            "east_domain",
            "west_domain",
        ],
    )
    @normalize(
        "leadtime_hour",
        [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "9",
            "12",
            "15",
            "18",
            "21",
            "24",
            "27",
            "30",
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
        "pressure_level",
        [
            "10",
            "20",
            "30",
            "50",
            "70",
            "100",
            "150",
            "200",
            "250",
            "300",
            "400",
            "500",
            "600",
            "700",
            "750",
            "800",
            "825",
            "850",
            "875",
            "900",
            "925",
            "950",
            "1000",
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
        "variable",
        [
            "cloud_cover",
            "geometric_vertical_velocity",
            "geopotential",
            "graupel",
            "potential_vorticity",
            "pseudo_adiabatic_potential_temperature",
            "relative_humidity",
            "specific_cloud_ice_water_content",
            "specific_cloud_liquid_water_content",
            "specific_cloud_rain_water_content",
            "specific_cloud_snow_water_content",
            "temperature",
            "u_component_of_wind",
            "v_component_of_wind",
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
        "format_",
        [
            "grib",
            "netcdf",
        ],
    )
    def __init__(
        self,
        day,
        domain,
        leadtime_hour,
        month,
        pressure_level,
        product_type,
        time,
        variable,
        year,
        format_=None,
        limit=None,
    ):
        super().__init__(
            day=day,
            domain=domain,
            leadtime_hour=leadtime_hour,
            month=month,
            pressure_level=pressure_level,
            product_type=product_type,
            time=time,
            variable=variable,
            year=year,
            format_=format_,
            limit=limit,
        )
