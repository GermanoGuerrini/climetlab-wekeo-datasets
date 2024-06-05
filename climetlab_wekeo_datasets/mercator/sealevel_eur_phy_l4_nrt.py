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
    "cmems_obs-sl_eur_phy-ssh_nrt_allsat-l4-duacs-0.125deg_P1D_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_allsat-l4-duacs-0.125deg_P1D
]


class sealevel_eur_phy_l4_nrt(Main):
    name = "EO:MO:DAT:SEALEVEL_EUR_PHY_L4_NRT_008_060"
    dataset = "EO:MO:DAT:SEALEVEL_EUR_PHY_L4_NRT_008_060"

    @normalize(
        "variables",
        [
            "adt",
            "err_sla",
            "err_ugosa",
            "err_vgosa",
            "flag_ice",
            "sla",
            "ugos",
            "ugosa",
            "vgos",
            "vgosa",
        ],
        multiple=True,
    )
    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    def __init__(
        self,
        variables,
        layer="cmems_obs-sl_eur_phy-ssh_nrt_allsat-l4-duacs-0.125deg_P1D_202311",
        bbox=None,
        limit=None,
    ):
        super().__init__(variables=variables, layer=layer, bbox=bbox, limit=limit)
