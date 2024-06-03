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
    "cmems_mod_bal_phy-cur_anfc_detided_P1D-m_202311",  # noqa: E501 cmems_mod_bal_phy-cur_anfc_detided_P1D-m
    "cmems_mod_bal_phy-ssh_anfc_detided_P1D-m_202311",  # noqa: E501 cmems_mod_bal_phy-ssh_anfc_detided_P1D-m
    "cmems_mod_bal_phy_anfc_P1D-m_202211",  # noqa: E501 cmems_mod_bal_phy_anfc_P1D-m_202211
    "cmems_mod_bal_phy_anfc_P1D-m_202311",  # noqa: E501 cmems_mod_bal_phy_anfc_P1D-m
    "cmems_mod_bal_phy_anfc_P1M-m_202211",  # noqa: E501 cmems_mod_bal_phy_anfc_P1M-m_202211
    "cmems_mod_bal_phy_anfc_P1M-m_202311",  # noqa: E501 cmems_mod_bal_phy_anfc_P1M-m
    "cmems_mod_bal_phy_anfc_PT15m-i_202211",  # noqa: E501 cmems_mod_bal_phy_anfc_PT15m-i_202211
    "cmems_mod_bal_phy_anfc_PT15M-i_202311",  # noqa: E501 cmems_mod_bal_phy_anfc_PT15M-i
    "cmems_mod_bal_phy_anfc_PT1h-i_202211",  # noqa: E501 cmems_mod_bal_phy_anfc_PT1h-i_202211
    "cmems_mod_bal_phy_anfc_PT1H-i_202311",  # noqa: E501 cmems_mod_bal_phy_anfc_PT1H-i
    "cmems_mod_bal_phy_anfc_static_202112",  # noqa: E501 cmems_mod_bal_phy_anfc_static_202112
    "cmems_mod_bal_phy_anfc_static_202311",  # noqa: E501 cmems_mod_bal_phy_anfc_static
]


class balticsea_analysisforecast_phy(Main):
    name = "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_PHY_003_006"
    dataset = "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_PHY_003_006"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "e1t",
            "e2t",
            "e3t",
            "lat",
            "latitude",
            "lon",
            "longitude",
            "mdt",
            "mlotst",
            "siconc",
            "sithick",
            "sla",
            "so",
            "sob",
            "thetao",
            "time",
            "uo",
            "uos_detided",
            "vo",
            "vos_detided",
            "wo",
            "zos_detided",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2021-12-28T00:00:00Z",
        min_date="2021-12-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_bal_phy-cur_anfc_detided_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-23T12:00:00Z"

        if layer == "cmems_mod_bal_phy-ssh_anfc_detided_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-23T12:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_P1D-m_202211":
            if min_date is None:
                min_date = "2021-01-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-04-07T12:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_P1D-m_202311":
            if min_date is None:
                min_date = "2021-11-01T12:00:00Z"

            if max_date is None:
                max_date = "2024-05-24T12:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_P1M-m_202211":
            if min_date is None:
                min_date = "2021-01-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-03-16T18:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_P1M-m_202311":
            if min_date is None:
                min_date = "2021-11-16T06:00:00Z"

            if max_date is None:
                max_date = "2024-04-16T06:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_PT15M-i_202311":
            if min_date is None:
                min_date = "2021-11-01T00:15:00Z"

            if max_date is None:
                max_date = "2024-05-25T12:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_PT15m-i_202211":
            if min_date is None:
                min_date = "2021-01-01T00:15:00Z"

            if max_date is None:
                max_date = "2024-04-08T12:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_PT1H-i_202311":
            if min_date is None:
                min_date = "2021-11-01T01:00:00Z"

            if max_date is None:
                max_date = "2024-05-25T12:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_PT1h-i_202211":
            if min_date is None:
                min_date = "2021-01-01T01:00:00Z"

            if max_date is None:
                max_date = "2024-04-08T12:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_static_202112":
            if min_date is None:
                min_date = "2021-12-01T00:00:00Z"

            if max_date is None:
                max_date = "2021-12-28T00:00:00Z"

        if layer == "cmems_mod_bal_phy_anfc_static_202311":
            if min_date is None:
                min_date = "2023-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2023-11-28T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
