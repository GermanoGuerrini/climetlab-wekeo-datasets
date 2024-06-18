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
    "MetO-NWS-WAV-RAN_202007",  # noqa: E501 MetO-NWS-WAV-RAN
]


class nwshelf_reanalysis_wav(Main):
    name = "EO:MO:DAT:NWSHELF_REANALYSIS_WAV_004_015"
    dataset = "EO:MO:DAT:NWSHELF_REANALYSIS_WAV_004_015"

    @normalize(
        "variables",
        [
            "VHM0",
            "VHM0_SW1",
            "VHM0_SW2",
            "VHM0_WW",
            "VMDR",
            "VMDR_SW1",
            "VMDR_SW2",
            "VMDR_WW",
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
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        variables,
        layer="MetO-NWS-WAV-RAN_202007",
        bbox=None,
        end_datetime="2024-01-31T21:00:00Z",
        start_datetime="1980-01-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            variables=variables,
            layer=layer,
            bbox=bbox,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
