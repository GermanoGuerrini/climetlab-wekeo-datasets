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


class sis_biodiversity_era5_regional(Main):
    name = "EO:ECMWF:DAT:SIS_BIODIVERSITY_ERA5_REGIONAL"
    dataset = "EO:ECMWF:DAT:SIS_BIODIVERSITY_ERA5_REGIONAL"

    @normalize(
        "region",
        [
            "central_africa",
            "europe",
            "northern_brazil",
        ],
        multiple=True,
    )
    @normalize(
        "origin",
        [
            "era5",
            "era5_land",
        ],
    )
    @normalize(
        "variable",
        [
            "2m_temperature",
            "annual_mean_temperature",
            "annual_precipitation",
            "aridity",
            "cloud_cover",
            "dry_days",
            "dry_spells",
            "evaporative_fraction",
            "frost_days",
            "growing_degree_days",
            "growing_degree_days_during_growing_season_length",
            "growing_season",
            "isothermality",
            "koeppen_geiger_class",
            "maximum_temperature_of_warmest_month",
            "mean_diurnal_range",
            "mean_temperature_of_coldest_quarter",
            "mean_temperature_of_driest_quarter",
            "mean_temperature_of_warmest_quarter",
            "mean_temperature_of_wettest_quarter",
            "meridional_wind_speed",
            "minimum_temperature_of_coldest_month",
            "potential_evaporation",
            "precipitation",
            "precipitation_of_coldest_quarter",
            "precipitation_of_driest_month",
            "precipitation_of_driest_quarter",
            "precipitation_of_warmest_quarter",
            "precipitation_of_wettest_month",
            "precipitation_of_wettest_quarter",
            "precipitation_seasonality",
            "summer_days",
            "surface_latent_heat_flux",
            "surface_sensible_heat_flux",
            "temperature_annual_range",
            "temperature_seasonality",
            "volumetric_soil_water",
            "water_vapor_pressure",
            "wind_speed",
            "zonal_wind_speed",
        ],
        multiple=True,
    )
    @normalize(
        "derived_variable",
        [
            "annual_maximum",
            "annual_maximum_of_daily_mean",
            "annual_mean",
            "annual_mean_of_daily_maximum",
            "annual_mean_of_daily_minimum",
            "annual_minimum",
            "annual_sum",
            "coldest_quarter",
            "driest_quarter",
            "end_of_season",
            "length_of_season",
            "maximum_length",
            "mean_intensity",
            "mean_length_with_minimum_5_days",
            "monthly_mean",
            "monthly_mean_of_daily_maximum",
            "monthly_mean_of_daily_minimum",
            "monthly_sum",
            "number_of_occurrences",
            "start_of_season",
            "warmest_quarter",
            "wettest_quarter",
        ],
        multiple=True,
    )
    @normalize(
        "statistic",
        [
            "25th_quartile",
            "75th_quartile",
            "mean",
            "median",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "1.0",
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
        region,
        origin,
        variable,
        derived_variable,
        statistic,
        version="1.0",
        format_=None,
        limit=None,
    ):
        super().__init__(
            region=region,
            origin=origin,
            variable=variable,
            derived_variable=derived_variable,
            statistic=statistic,
            version=version,
            format_=format_,
            limit=limit,
        )
