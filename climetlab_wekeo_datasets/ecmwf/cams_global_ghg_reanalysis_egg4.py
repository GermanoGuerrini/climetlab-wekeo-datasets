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


class cams_global_ghg_reanalysis_egg4(Main):
    name = "EO:ECMWF:DAT:CAMS_GLOBAL_GHG_REANALYSIS_EGG4"
    dataset = "EO:ECMWF:DAT:CAMS_GLOBAL_GHG_REANALYSIS_EGG4"

    @normalize(
        "step",
        [
            "0",
            "3",
            "6",
            "9",
            "12",
            "15",
            "18",
            "21",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "2m_dewpoint_temperature",
            "2m_temperature",
            "accumulated_carbon_dioxide_ecosystem_respiration",
            "accumulated_carbon_dioxide_gross_primary_production",
            "accumulated_carbon_dioxide_net_ecosystem_exchange",
            "anthropogenic_emissions_of_carbon_dioxide",
            "boundary_layer_height",
            "carbon_dioxide",
            "ch4_column_mean_molar_fraction",
            "co2_column_mean_molar_fraction",
            "convective_available_potential_energy",
            "convective_inhibition",
            "convective_precipitation",
            "downward_uv_radiation_at_the_surface",
            "evaporation",
            "flux_of_carbon_dioxide_ecosystem_respiration",
            "flux_of_carbon_dioxide_gross_primary_production",
            "flux_of_carbon_dioxide_net_ecosystem_exchange",
            "forecast_albedo",
            "fraction_of_cloud_cover",
            "geopotential",
            "gpp_coefficient_from_biogenic_flux_adjustment_system",
            "high_cloud_cover",
            "land_sea_mask",
            "large_scale_precipitation",
            "logarithm_of_surface_pressure",
            "low_cloud_cover",
            "mean_sea_level_pressure",
            "medium_cloud_cover",
            "methane",
            "methane_loss_rate_due_to_radical_hydroxyl_oh",
            "methane_surface_fluxes",
            "ocean_flux_of_carbon_dioxide",
            "photosynthetically_active_radiation_at_the_surface",
            "potential_evaporation",
            "potential_vorticity",
            "precipitation_type",
            "rec_coefficient_from_biogenic_flux_adjustment_system",
            "relative_humidity",
            "sea_ice_cover",
            "sea_surface_temperature",
            "skin_reservoir_content",
            "skin_temperature",
            "snow_albedo",
            "snow_depth",
            "specific_cloud_ice_water_content",
            "specific_cloud_liquid_water_content",
            "specific_humidity",
            "specific_rain_water_content",
            "specific_snow_water_content",
            "sunshine_duration",
            "surface_geopotential",
            "surface_latent_heat_flux",
            "surface_net_solar_radiation",
            "surface_net_solar_radiation_clear_sky",
            "surface_net_thermal_radiation",
            "surface_net_thermal_radiation_clear_sky",
            "surface_sensible_heat_flux",
            "surface_solar_radiation_downward_clear_sky",
            "surface_solar_radiation_downwards",
            "surface_thermal_radiation_downward_clear_sky",
            "surface_thermal_radiation_downwards",
            "temperature",
            "toa_incident_solar_radiation",
            "top_net_solar_radiation",
            "top_net_solar_radiation_clear_sky",
            "top_net_thermal_radiation",
            "top_net_thermal_radiation_clear_sky",
            "total_cloud_cover",
            "total_column_cloud_ice_water",
            "total_column_cloud_liquid_water",
            "total_column_water",
            "total_column_water_vapour",
            "total_precipitation",
            "u_component_of_wind",
            "v_component_of_wind",
            "vertical_velocity",
            "visibility",
            "wildfire_flux_of_carbon_dioxide",
            "wildfire_flux_of_methane",
        ],
        multiple=True,
    )
    @normalize("dtend", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("dtstart", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
        ],
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
        ],
        multiple=True,
    )
    @normalize(
        "pressure_level",
        [
            "1",
            "2",
            "3",
            "5",
            "7",
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
            "800",
            "850",
            "900",
            "925",
            "950",
            "1000",
        ],
        multiple=True,
    )
    def __init__(
        self,
        step,
        variable,
        dtend="2020-12-31",
        dtstart="2003-01-01",
        bbox=None,
        format_=None,
        model_level=None,
        pressure_level=None,
        limit=None,
    ):
        super().__init__(
            step=step,
            variable=variable,
            dtend=dtend,
            dtstart=dtstart,
            bbox=bbox,
            format_=format_,
            model_level=model_level,
            pressure_level=pressure_level,
            limit=limit,
        )
