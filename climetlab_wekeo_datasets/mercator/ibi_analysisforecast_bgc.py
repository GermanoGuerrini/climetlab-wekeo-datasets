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
    "cmems_mod_ibi_bgc_anfc_0.027deg-3D_P1D-m_202211",  # noqa: E501 cmems_mod_ibi_bgc_anfc_0.027deg-3D_P1D-m
    "cmems_mod_ibi_bgc_anfc_0.027deg-3D_P1M-m_202211",  # noqa: E501 cmems_mod_ibi_bgc_anfc_0.027deg-3D_P1M-m
    "cmems_mod_ibi_bgc_anfc_0.027deg-3D_static_202012",  # noqa: E501 cmems_mod_ibi_bgc_anfc_0.027deg-3D_static
]


class ibi_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:IBI_ANALYSISFORECAST_BGC_005_004"
    dataset = "EO:MO:DAT:IBI_ANALYSISFORECAST_BGC_005_004"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "chl",
            "depth",
            "deptho",
            "deptho_lev",
            "dissic",
            "fe",
            "latitude",
            "longitude",
            "mask",
            "nh4",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "po4",
            "si",
            "spco2",
            "time",
            "zeu",
            "zooc",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2020-12-28T00:00:00Z",
        min_date="2020-12-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_mod_ibi_bgc_anfc_0.027deg-3D_P1D-m_202211":
            if min_date is None:
                min_date = "2021-12-13T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-06T12:00:00Z"

        if layer == "cmems_mod_ibi_bgc_anfc_0.027deg-3D_P1M-m_202211":
            if min_date is None:
                min_date = "2020-12-16T12:00:00Z"

            if max_date is None:
                max_date = "2024-02-15T12:00:00Z"

        if layer == "cmems_mod_ibi_bgc_anfc_0.027deg-3D_static_202012":
            if min_date is None:
                min_date = "2020-12-01T00:00:00Z"

            if max_date is None:
                max_date = "2020-12-28T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
