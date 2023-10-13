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
    "cmems_obs_oc_arc_bgc_geophy_nrt_l4-hr_P1D-m_202105",  # noqa: E501 cmems_obs_oc_arc_bgc_geophy_nrt_l4-hr_P1D-m_202105
    "cmems_obs_oc_arc_bgc_geophy_nrt_l4-hr_P1M-m_202105",  # noqa: E501 cmems_obs_oc_arc_bgc_geophy_nrt_l4-hr_P1M-m_202105
    "cmems_obs_oc_arc_bgc_optics_nrt_l4-hr_P1D-m_202105",  # noqa: E501 cmems_obs_oc_arc_bgc_optics_nrt_l4-hr_P1D-m_202105
    "cmems_obs_oc_arc_bgc_optics_nrt_l4-hr_P1M-m_202105",  # noqa: E501 cmems_obs_oc_arc_bgc_optics_nrt_l4-hr_P1M-m_202105
    "cmems_obs_oc_arc_bgc_transp_nrt_l4-hr_P1D-m_202105",  # noqa: E501 cmems_obs_oc_arc_bgc_transp_nrt_l4-hr_P1D-m_202105
    "cmems_obs_oc_arc_bgc_transp_nrt_l4-hr_P1M-m_202105",  # noqa: E501 cmems_obs_oc_arc_bgc_transp_nrt_l4-hr_P1M-m_202105
]


class oceancolour_arc_bgc_hr_l4_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_ARC_BGC_HR_L4_NRT_009_207"
    dataset = "EO:MO:DAT:OCEANCOLOUR_ARC_BGC_HR_L4_NRT_009_207"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "BBP443",
            "BBP443_count",
            "BBP443_error",
            "CHL",
            "CHL_count",
            "CHL_error",
            "SPM",
            "SPM_count",
            "SPM_error",
            "TUR",
            "TUR_count",
            "TUR_error",
            "crs",
            "lat",
            "lon",
            "time",
            "x",
            "y",
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
        if layer == "cmems_obs_oc_arc_bgc_transp_nrt_l4-hr_P1D-m_202105":
            if start is None:
                start = "2020-02-01T00:00:00Z"

            if end is None:
                end = "2023-04-30T23:59:59Z"

        if layer == "cmems_obs_oc_arc_bgc_optics_nrt_l4-hr_P1D-m_202105":
            if start is None:
                start = "2020-02-01T00:00:00Z"

            if end is None:
                end = "2023-04-30T23:59:59Z"

        if layer == "cmems_obs_oc_arc_bgc_geophy_nrt_l4-hr_P1D-m_202105":
            if start is None:
                start = "2020-02-01T00:00:00Z"

            if end is None:
                end = "2023-04-30T23:59:59Z"

        if layer == "cmems_obs_oc_arc_bgc_geophy_nrt_l4-hr_P1M-m_202105":
            if start is None:
                start = "2020-01-01T00:00:00Z"

            if end is None:
                end = "2023-08-31T23:59:59Z"

        if layer == "cmems_obs_oc_arc_bgc_transp_nrt_l4-hr_P1M-m_202105":
            if start is None:
                start = "2020-01-01T00:00:00Z"

            if end is None:
                end = "2023-08-31T23:59:59Z"

        if layer == "cmems_obs_oc_arc_bgc_optics_nrt_l4-hr_P1M-m_202105":
            if start is None:
                start = "2020-01-01T00:00:00Z"

            if end is None:
                end = "2023-08-31T23:59:59Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
