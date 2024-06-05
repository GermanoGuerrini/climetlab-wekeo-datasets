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
    "cmems_mod_med_wav_anfc_4.2km_PT1H-i_202311",  # noqa: E501 cmems_mod_med_wav_anfc_4.2km_PT1H-i
]


class medsea_analysisforecast_wav(Main):
    name = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_WAV_006_017"
    dataset = "EO:MO:DAT:MEDSEA_ANALYSISFORECAST_WAV_006_017"

    @normalize(
        "variables",
        [
            "VCMX",
            "VHM0",
            "VHM0_SW1",
            "VHM0_SW2",
            "VHM0_WW",
            "VMDR",
            "VMDR_SW1",
            "VMDR_SW2",
            "VMDR_WW",
            "VMXL",
            "VPED",
            "VSDX",
            "VSDY",
            "VTM01_SW1",
            "VTM01_SW2",
            "VTM01_WW",
            "VTM02",
            "VTM10",
            "VTPK",
        ],
        multiple=True,
    )
    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    def __init__(
        self,
        variables,
        layer="cmems_mod_med_wav_anfc_4.2km_PT1H-i_202311",
        bbox=None,
        limit=None,
    ):
        super().__init__(variables=variables, layer=layer, bbox=bbox, limit=limit)
