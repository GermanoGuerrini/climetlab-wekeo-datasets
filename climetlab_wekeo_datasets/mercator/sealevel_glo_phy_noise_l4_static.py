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
    "cmems_obs-sl_glo_phy-noise_mynrt_multi-L4-duacs-0.25deg_P1Y_202211",  # noqa: E501 cmems_obs-sl_glo_phy-noise_mynrt_multi-L4-duacs-0.25deg_P1Y
]


class sealevel_glo_phy_noise_l4_static(Main):
    name = "EO:MO:DAT:SEALEVEL_GLO_PHY_NOISE_L4_STATIC_008_033"
    dataset = "EO:MO:DAT:SEALEVEL_GLO_PHY_NOISE_L4_STATIC_008_033"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "crs",
            "lat_bnds",
            "latitude",
            "lon_bnds",
            "longitude",
            "noise",
            "nv",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer="cmems_obs-sl_glo_phy-noise_mynrt_multi-L4-duacs-0.25deg_P1Y_202211",
        max_date="2022-11-28T00:00:00Z",
        min_date="2022-11-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if (
            layer
            == "cmems_obs-sl_glo_phy-noise_mynrt_multi-L4-duacs-0.25deg_P1Y_202211"
        ):
            if min_date is None:
                min_date = "2022-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-28T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )