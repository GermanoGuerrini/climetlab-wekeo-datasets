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
    "cmems_obs-wave_glo_phy-swh_my_multi-l4-2deg_P1D_202112",  # noqa: E501 cmems_obs-wave_glo_phy-swh_my_multi-l4-2deg_P1D
]


class wave_glo_phy_swh_l4_my(Main):
    name = "EO:MO:DAT:WAVE_GLO_PHY_SWH_L4_MY_014_007"
    dataset = "EO:MO:DAT:WAVE_GLO_PHY_SWH_L4_MY_014_007"

    @normalize(
        "variables",
        [
            "VAVH_DAILY_MAX",
            "VAVH_DAILY_MEAN",
            "VAVH_DAILY_NBR",
            "VAVH_DAILY_STD",
            "VAVH_INST",
            "VAVH_INST_NBR",
            "VAVH_INST_SCORE",
        ],
        multiple=True,
    )
    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    def __init__(
        self,
        variables,
        layer="cmems_obs-wave_glo_phy-swh_my_multi-l4-2deg_P1D_202112",
        bbox=None,
        limit=None,
    ):
        super().__init__(variables=variables, layer=layer, bbox=bbox, limit=limit)
