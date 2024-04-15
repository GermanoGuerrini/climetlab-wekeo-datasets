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


class reanalysis_carra_single_levels(Main):
    name = "EO:ECMWF:DAT:REANALYSIS_CARRA_SINGLE_LEVELS"
    dataset = "EO:ECMWF:DAT:REANALYSIS_CARRA_SINGLE_LEVELS"

    @normalize(
        "domain",
        [
            "east_domain",
            "west_domain",
        ],
    )
    @normalize(
        "level_type",
        [
            "soil_level",
            "surface_or_atmosphere",
        ],
    )
    @normalize(
        "variable",
        [
            "10m_eastward_wind_gust_since_previous_post_processing",
            "10m_northward_wind_gust_since_previous_post_processing",
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "10m_wind_direction",
            "10m_wind_gust_since_previous_post_processing",
            "10m_wind_speed",
            "2m_relative_humidity",
            "2m_specific_humidity",
            "2m_temperature",
            "albedo",
            "cloud_base",
            "cloud_top",
            "direct_solar_radiation",
            "evaporation",
            "fog",
            "fraction_of_snow_cover",
            "high_cloud_cover",
            "land_sea_mask",
            "low_cloud_cover",
            "maximum_2m_temperature_since_previous_post_processing",
            "mean_sea_level_pressure",
            "medium_cloud_cover",
            "minimum_2m_temperature_since_previous_post_processing",
            "orography",
            "percolation",
            "precipitation_type",
            "sea_ice_area_fraction",
            "sea_ice_surface_temperature",
            "sea_ice_thickness",
            "sea_surface_temperature",
            "skin_temperature",
            "snow_albedo",
            "snow_density",
            "snow_depth_water_equivalent",
            "snow_on_ice_total_depth",
            "surface_latent_heat_flux",
            "surface_net_solar_radiation",
            "surface_net_solar_radiation,_clear_sky",
            "surface_net_thermal_radiation",
            "surface_net_thermal_radiation,_clear_sky",
            "surface_pressure",
            "surface_roughness",
            "surface_roughness_length_for_heat",
            "surface_runoff",
            "surface_sensible_heat_flux",
            "surface_solar_radiation_downwards",
            "thermal_surface_radiation_downwards",
            "time_integral_of_rain_flux",
            "time_integral_of_snow_evaporation_flux",
            "time_integral_of_surface_eastward_momentum_flux",
            "time_integral_of_surface_latent_heat_evaporation_flux",
            "time_integral_of_surface_latent_heat_sublimation_flux",
            "time_integral_of_surface_northward_momentum_flux",
            "time_integral_of_total_solid_precipitation_flux",
            "time_integrated_surface_direct_short_wave_radiation_flux",
            "top_net_solar_radiation",
            "top_net_thermal_radiation",
            "total_cloud_cover",
            "total_column_cloud_ice_water",
            "total_column_cloud_liquid_water",
            "total_column_graupel",
            "total_column_integrated_water_vapour",
            "total_precipitation",
            "visibility",
            "volumetric_soil_ice",
            "volumetric_soil_moisture",
        ],
        multiple=True,
    )
    @normalize(
        "soil_level",
        [
            "root_depth",
            "soil_surface",
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
        level_type,
        variable,
        soil_level,
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
            level_type=level_type,
            variable=variable,
            soil_level=soil_level,
            product_type=product_type,
            time=time,
            leadtime_hour=leadtime_hour,
            year=year,
            month=month,
            day=day,
            format_=format_,
            limit=limit,
        )
