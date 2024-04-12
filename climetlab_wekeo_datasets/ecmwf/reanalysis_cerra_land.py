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


class reanalysis_cerra_land(Main):
    name = "EO:ECMWF:DAT:REANALYSIS_CERRA_LAND"
    dataset = "EO:ECMWF:DAT:REANALYSIS_CERRA_LAND"

    @normalize(
        "variable",
        [
            "albedo",
            "evaporation",
            "fraction_of_snow_cover",
            "lake_bottom_temperature",
            "lake_depth",
            "lake_ice_depth",
            "lake_ice_temperature",
            "lake_mix_layer_depth",
            "lake_mix_layer_temperature",
            "lake_shape_factor",
            "lake_total_layer_temperature",
            "land_sea_mask",
            "liquid_volumetric_soil_moisture",
            "orography",
            "percolation",
            "skin_temperature",
            "snow_albedo",
            "snow_density",
            "snow_depth",
            "snow_depth_water_equivalent",
            "snow_melt",
            "soil_heat_flux",
            "soil_temperature",
            "surface_latent_heat_flux",
            "surface_net_solar_radiation",
            "surface_net_thermal_radiation",
            "surface_roughness",
            "surface_runoff",
            "surface_sensible_heat_flux",
            "surface_solar_radiation_downwards",
            "surface_thermal_radiation_downwards",
            "temperature_of_snow_layer",
            "total_precipitation",
            "volumetric_soil_moisture",
            "volumetric_transpiration_stress_onset",
            "volumetric_wilting_point",
        ],
        multiple=True,
    )
    @normalize(
        "level_type",
        [
            "soil",
            "surface",
        ],
        multiple=True,
    )
    @normalize(
        "soil_layer",
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
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "analysis",
            "forecast",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
            "3",
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
        variable,
        level_type,
        soil_layer,
        product_type,
        year,
        month,
        day,
        time,
        leadtime_hour,
        format_=None,
        limit=None,
    ):
        super().__init__(
            variable=variable,
            level_type=level_type,
            soil_layer=soil_layer,
            product_type=product_type,
            year=year,
            month=month,
            day=day,
            time=time,
            leadtime_hour=leadtime_hour,
            format_=format_,
            limit=limit,
        )
