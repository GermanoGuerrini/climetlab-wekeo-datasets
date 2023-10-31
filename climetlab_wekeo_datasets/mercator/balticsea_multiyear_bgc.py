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
    "cmems_mod_bal_bgc_my_P1D-m_202303",  # noqa: E501 Cmems ergom daily integrated model fields
    "cmems_mod_bal_bgc_my_P1M-m_202303",  # noqa: E501 Cmems ergom monthly integrated model fields
    "cmems_mod_bal_bgc_my_P1Y-m_202303",  # noqa: E501 Cmems ergom annual integrated model fields
]


class balticsea_multiyear_bgc(Main):
    name = "EO:MO:DAT:BALTICSEA_MULTIYEAR_BGC_003_012"
    dataset = "EO:MO:DAT:BALTICSEA_MULTIYEAR_BGC_003_012"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "chl",
            "depth",
            "lat",
            "lon",
            "nh4",
            "no3",
            "nppv",
            "o2",
            "o2b",
            "ph",
            "po4",
            "spco2",
            "time",
            "zsd",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer,
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_mod_bal_bgc_my_P1D-m_202303":
            if start is None:
                start = "1993-01-01T12:00:00Z"

            if end is None:
                end = "2021-12-31T12:00:00Z"

        if layer == "cmems_mod_bal_bgc_my_P1M-m_202303":
            if start is None:
                start = "1993-01-01T12:00:00Z"

            if end is None:
                end = "2021-12-01T12:00:00Z"

        if layer == "cmems_mod_bal_bgc_my_P1Y-m_202303":
            if start is None:
                start = "1993-01-01T12:00:00Z"

            if end is None:
                end = "2021-01-01T12:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
