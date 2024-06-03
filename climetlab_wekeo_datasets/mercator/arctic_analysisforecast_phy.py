#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.mercator.main import Main

LAYERS = [
    "cmems_mod_arc_phy_anfc_6km_detided_P1D-m_202311",  # noqa: E501 cmems_mod_arc_phy_anfc_6km_detided_P1D-m
    "cmems_mod_arc_phy_anfc_6km_detided_P1M-m_202311",  # noqa: E501 cmems_mod_arc_phy_anfc_6km_detided_P1M-m
    "cmems_mod_arc_phy_anfc_6km_detided_PT1H-i_202311",  # noqa: E501 cmems_mod_arc_phy_anfc_6km_detided_PT1H-i_202311
    "cmems_mod_arc_phy_anfc_6km_detided_PT6H-m_202311",  # noqa: E501 cmems_mod_arc_phy_anfc_6km_detided_PT6H-m_202311
]


class arctic_analysisforecast_phy(Main):
    name = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_002_001"
    dataset = "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_PHY_002_001"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "latitude",
            "longitude",
            "mlotst",
            "model_depth",
            "siage",
            "sialb",
            "siconc",
            "siconc_fy",
            "sisnthick",
            "sithick",
            "so",
            "stereographic",
            "stfbaro",
            "thetao",
            "time",
            "vxo",
            "vxsi",
            "vyo",
            "vysi",
            "wo",
            "x",
            "y",
            "zos",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-04-16T00:00:00Z",
        min_date="2021-11-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_arc_phy_anfc_6km_detided_P1D-m_202311":
            if min_date is None:
                min_date = "2021-07-05T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-28T12:00:00Z"

        if layer == "cmems_mod_arc_phy_anfc_6km_detided_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T00:00:00Z"

        if layer == "cmems_mod_arc_phy_anfc_6km_detided_PT1H-i_202311":
            if min_date is None:
                min_date = "2021-07-05T00:30:00Z"

            if max_date is None:
                max_date = "2024-05-28T23:30:00Z"

        if layer == "cmems_mod_arc_phy_anfc_6km_detided_PT6H-m_202311":
            if min_date is None:
                min_date = "2023-09-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-21T21:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
