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
    "CERSAT-GLO-SEAICE_30DAYS_DRIFT_ASCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_30DAYS_DRIFT_ASCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_30DAYS_DRIFT_QUICKSCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_30DAYS_DRIFT_QUICKSCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_3DAYS_DRIFT_ASCAT_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_3DAYS_DRIFT_ASCAT_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_3DAYS_DRIFT_ASCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_3DAYS_DRIFT_ASCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_3DAYS_DRIFT_QUICKSCAT_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_3DAYS_DRIFT_QUICKSCAT_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_3DAYS_DRIFT_QUICKSCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_3DAYS_DRIFT_QUICKSCAT_SSMI_MERGED_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_6DAYS_DRIFT_ASCAT_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_6DAYS_DRIFT_ASCAT_RAN-OBS_FULL_TIME_SERIE
    "CERSAT-GLO-SEAICE_6DAYS_DRIFT_QUICKSCAT_RAN-OBS_FULL_TIME_SERIE_202311",  # noqa: E501 CERSAT-GLO-SEAICE_6DAYS_DRIFT_QUICKSCAT_RAN-OBS_FULL_TIME_SERIE
    "cmems_obs-si_arc_phy-drift_my_l3-ssmi_P30D_202311",  # noqa: E501 cmems_obs-si_arc_phy-drift_my_l3-ssmi_P30D
    "cmems_obs-si_arc_phy-drift_my_l3-ssmi_P3D_202311",  # noqa: E501 cmems_obs-si_arc_phy-drift_my_l3-ssmi_P3D
]


class seaice_arc_seaice_l3_rep_observations(Main):
    name = "EO:MO:DAT:SEAICE_ARC_SEAICE_L3_REP_OBSERVATIONS_011_010"
    dataset = "EO:MO:DAT:SEAICE_ARC_SEAICE_L3_REP_OBSERVATIONS_011_010"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "eastward_sea_ice_velocity",
            "northward_sea_ice_velocity",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "end_datetime",
        [
            "2007-02-01T00:00:00Z",
            "2007-03-01T00:00:00Z",
            "2007-04-01T00:00:00Z",
            "2007-05-01T00:00:00Z",
            "2007-06-01T00:00:00Z",
            "2007-07-01T00:00:00Z",
            "2007-08-01T00:00:00Z",
            "2007-09-01T00:00:00Z",
            "2007-10-01T00:00:00Z",
            "2007-11-01T00:00:00Z",
            "2007-12-01T00:00:00Z",
            "2008-01-01T00:00:00Z",
            "2008-02-01T00:00:00Z",
            "2008-03-01T00:00:00Z",
            "2008-04-01T00:00:00Z",
            "2008-05-01T00:00:00Z",
            "2008-06-01T00:00:00Z",
            "2008-07-01T00:00:00Z",
            "2008-08-01T00:00:00Z",
            "2008-09-01T00:00:00Z",
            "2008-10-01T00:00:00Z",
            "2008-11-01T00:00:00Z",
            "2008-12-01T00:00:00Z",
            "2009-01-01T00:00:00Z",
            "2009-02-01T00:00:00Z",
            "2009-03-01T00:00:00Z",
            "2009-04-01T00:00:00Z",
            "2009-05-01T00:00:00Z",
            "2009-06-01T00:00:00Z",
            "2009-07-01T00:00:00Z",
            "2009-08-01T00:00:00Z",
            "2009-09-01T00:00:00Z",
            "2009-10-01T00:00:00Z",
            "2009-11-01T00:00:00Z",
            "2009-12-01T00:00:00Z",
            "2010-01-01T00:00:00Z",
            "2010-02-01T00:00:00Z",
            "2010-03-01T00:00:00Z",
            "2010-04-01T00:00:00Z",
            "2010-05-01T00:00:00Z",
            "2010-06-01T00:00:00Z",
            "2010-07-01T00:00:00Z",
            "2010-08-01T00:00:00Z",
            "2010-09-01T00:00:00Z",
            "2010-10-01T00:00:00Z",
            "2010-11-01T00:00:00Z",
            "2010-12-01T00:00:00Z",
            "2011-01-01T00:00:00Z",
            "2011-02-01T00:00:00Z",
            "2011-03-01T00:00:00Z",
            "2011-04-01T00:00:00Z",
            "2011-05-01T00:00:00Z",
            "2011-06-01T00:00:00Z",
            "2011-07-01T00:00:00Z",
            "2011-08-01T00:00:00Z",
            "2011-09-01T00:00:00Z",
            "2011-10-01T00:00:00Z",
            "2011-11-01T00:00:00Z",
            "2011-12-01T00:00:00Z",
            "2012-01-01T00:00:00Z",
            "2012-02-01T00:00:00Z",
            "2012-03-01T00:00:00Z",
            "2012-04-01T00:00:00Z",
            "2012-05-01T00:00:00Z",
            "2012-06-01T00:00:00Z",
            "2012-07-01T00:00:00Z",
            "2012-08-01T00:00:00Z",
            "2012-09-01T00:00:00Z",
            "2012-10-01T00:00:00Z",
            "2012-11-01T00:00:00Z",
            "2012-12-01T00:00:00Z",
            "2013-01-01T00:00:00Z",
            "2013-02-01T00:00:00Z",
            "2013-03-01T00:00:00Z",
            "2013-04-01T00:00:00Z",
            "2013-05-01T00:00:00Z",
            "2013-06-01T00:00:00Z",
            "2013-07-01T00:00:00Z",
            "2013-08-01T00:00:00Z",
            "2013-09-01T00:00:00Z",
            "2013-10-01T00:00:00Z",
            "2013-11-01T00:00:00Z",
            "2013-12-01T00:00:00Z",
            "2014-01-01T00:00:00Z",
            "2014-02-01T00:00:00Z",
            "2014-03-01T00:00:00Z",
            "2014-04-01T00:00:00Z",
            "2014-05-01T00:00:00Z",
            "2014-06-01T00:00:00Z",
            "2014-07-01T00:00:00Z",
            "2014-08-01T00:00:00Z",
            "2014-09-01T00:00:00Z",
            "2014-10-01T00:00:00Z",
            "2014-11-01T00:00:00Z",
            "2014-12-01T00:00:00Z",
            "2015-01-01T00:00:00Z",
            "2015-02-01T00:00:00Z",
            "2015-03-01T00:00:00Z",
            "2015-04-01T00:00:00Z",
            "2015-05-01T00:00:00Z",
            "2015-06-01T00:00:00Z",
            "2015-07-01T00:00:00Z",
            "2015-08-01T00:00:00Z",
            "2015-09-01T00:00:00Z",
            "2015-10-01T00:00:00Z",
            "2015-11-01T00:00:00Z",
            "2015-12-01T00:00:00Z",
            "2016-01-01T00:00:00Z",
            "2016-02-01T00:00:00Z",
            "2016-03-01T00:00:00Z",
            "2016-04-01T00:00:00Z",
            "2016-05-01T00:00:00Z",
            "2016-06-01T00:00:00Z",
            "2016-07-01T00:00:00Z",
            "2016-08-01T00:00:00Z",
            "2016-09-01T00:00:00Z",
            "2016-10-01T00:00:00Z",
            "2016-11-01T00:00:00Z",
            "2016-12-01T00:00:00Z",
            "2017-01-01T00:00:00Z",
            "2017-02-01T00:00:00Z",
            "2017-03-01T00:00:00Z",
            "2017-04-01T00:00:00Z",
            "2017-05-01T00:00:00Z",
            "2017-06-01T00:00:00Z",
            "2017-07-01T00:00:00Z",
            "2017-08-01T00:00:00Z",
            "2017-09-01T00:00:00Z",
            "2017-10-01T00:00:00Z",
            "2017-11-01T00:00:00Z",
            "2017-12-01T00:00:00Z",
            "2018-01-01T00:00:00Z",
            "2018-02-01T00:00:00Z",
            "2018-03-01T00:00:00Z",
            "2018-04-01T00:00:00Z",
            "2018-05-01T00:00:00Z",
            "2018-06-01T00:00:00Z",
            "2018-07-01T00:00:00Z",
            "2018-08-01T00:00:00Z",
            "2018-09-01T00:00:00Z",
            "2018-10-01T00:00:00Z",
            "2018-11-01T00:00:00Z",
            "2018-12-01T00:00:00Z",
            "2019-01-01T00:00:00Z",
            "2019-02-01T00:00:00Z",
            "2019-03-01T00:00:00Z",
            "2019-04-01T00:00:00Z",
            "2019-05-01T00:00:00Z",
            "2019-06-01T00:00:00Z",
            "2019-07-01T00:00:00Z",
            "2019-08-01T00:00:00Z",
            "2019-09-01T00:00:00Z",
            "2019-10-01T00:00:00Z",
            "2019-11-01T00:00:00Z",
            "2019-12-01T00:00:00Z",
            "2020-01-01T00:00:00Z",
            "2020-02-01T00:00:00Z",
            "2020-03-01T00:00:00Z",
            "2020-04-01T00:00:00Z",
            "2020-05-01T00:00:00Z",
            "2020-06-01T00:00:00Z",
            "2020-07-01T00:00:00Z",
            "2020-08-01T00:00:00Z",
            "2020-09-01T00:00:00Z",
            "2020-10-01T00:00:00Z",
            "2020-11-01T00:00:00Z",
            "2020-12-01T00:00:00Z",
            "2021-01-01T00:00:00Z",
            "2021-02-01T00:00:00Z",
            "2021-03-01T00:00:00Z",
            "2021-04-01T00:00:00Z",
            "2021-05-01T00:00:00Z",
            "2021-06-01T00:00:00Z",
            "2021-07-01T00:00:00Z",
            "2021-08-01T00:00:00Z",
            "2021-09-01T00:00:00Z",
            "2021-10-01T00:00:00Z",
            "2021-11-01T00:00:00Z",
            "2021-12-01T00:00:00Z",
            "2022-01-01T00:00:00Z",
            "2022-02-01T00:00:00Z",
            "2022-03-01T00:00:00Z",
            "2022-04-01T00:00:00Z",
            "2022-05-01T00:00:00Z",
            "2022-06-01T00:00:00Z",
            "2022-07-01T00:00:00Z",
            "2022-08-01T00:00:00Z",
            "2022-09-01T00:00:00Z",
            "2022-10-01T00:00:00Z",
            "2022-11-01T00:00:00Z",
            "2022-12-01T00:00:00Z",
            "2023-01-01T00:00:00Z",
            "2023-02-01T00:00:00Z",
            "2023-03-01T00:00:00Z",
            "2023-04-01T00:00:00Z",
            "2023-05-01T00:00:00Z",
            "2023-06-01T00:00:00Z",
            "2023-07-01T00:00:00Z",
            "2023-08-01T00:00:00Z",
            "2023-09-01T00:00:00Z",
            "2023-10-01T00:00:00Z",
            "2023-11-01T00:00:00Z",
        ],
    )
    @normalize(
        "start_datetime",
        [
            "2007-02-01T00:00:00Z",
            "2007-03-01T00:00:00Z",
            "2007-04-01T00:00:00Z",
            "2007-05-01T00:00:00Z",
            "2007-06-01T00:00:00Z",
            "2007-07-01T00:00:00Z",
            "2007-08-01T00:00:00Z",
            "2007-09-01T00:00:00Z",
            "2007-10-01T00:00:00Z",
            "2007-11-01T00:00:00Z",
            "2007-12-01T00:00:00Z",
            "2008-01-01T00:00:00Z",
            "2008-02-01T00:00:00Z",
            "2008-03-01T00:00:00Z",
            "2008-04-01T00:00:00Z",
            "2008-05-01T00:00:00Z",
            "2008-06-01T00:00:00Z",
            "2008-07-01T00:00:00Z",
            "2008-08-01T00:00:00Z",
            "2008-09-01T00:00:00Z",
            "2008-10-01T00:00:00Z",
            "2008-11-01T00:00:00Z",
            "2008-12-01T00:00:00Z",
            "2009-01-01T00:00:00Z",
            "2009-02-01T00:00:00Z",
            "2009-03-01T00:00:00Z",
            "2009-04-01T00:00:00Z",
            "2009-05-01T00:00:00Z",
            "2009-06-01T00:00:00Z",
            "2009-07-01T00:00:00Z",
            "2009-08-01T00:00:00Z",
            "2009-09-01T00:00:00Z",
            "2009-10-01T00:00:00Z",
            "2009-11-01T00:00:00Z",
            "2009-12-01T00:00:00Z",
            "2010-01-01T00:00:00Z",
            "2010-02-01T00:00:00Z",
            "2010-03-01T00:00:00Z",
            "2010-04-01T00:00:00Z",
            "2010-05-01T00:00:00Z",
            "2010-06-01T00:00:00Z",
            "2010-07-01T00:00:00Z",
            "2010-08-01T00:00:00Z",
            "2010-09-01T00:00:00Z",
            "2010-10-01T00:00:00Z",
            "2010-11-01T00:00:00Z",
            "2010-12-01T00:00:00Z",
            "2011-01-01T00:00:00Z",
            "2011-02-01T00:00:00Z",
            "2011-03-01T00:00:00Z",
            "2011-04-01T00:00:00Z",
            "2011-05-01T00:00:00Z",
            "2011-06-01T00:00:00Z",
            "2011-07-01T00:00:00Z",
            "2011-08-01T00:00:00Z",
            "2011-09-01T00:00:00Z",
            "2011-10-01T00:00:00Z",
            "2011-11-01T00:00:00Z",
            "2011-12-01T00:00:00Z",
            "2012-01-01T00:00:00Z",
            "2012-02-01T00:00:00Z",
            "2012-03-01T00:00:00Z",
            "2012-04-01T00:00:00Z",
            "2012-05-01T00:00:00Z",
            "2012-06-01T00:00:00Z",
            "2012-07-01T00:00:00Z",
            "2012-08-01T00:00:00Z",
            "2012-09-01T00:00:00Z",
            "2012-10-01T00:00:00Z",
            "2012-11-01T00:00:00Z",
            "2012-12-01T00:00:00Z",
            "2013-01-01T00:00:00Z",
            "2013-02-01T00:00:00Z",
            "2013-03-01T00:00:00Z",
            "2013-04-01T00:00:00Z",
            "2013-05-01T00:00:00Z",
            "2013-06-01T00:00:00Z",
            "2013-07-01T00:00:00Z",
            "2013-08-01T00:00:00Z",
            "2013-09-01T00:00:00Z",
            "2013-10-01T00:00:00Z",
            "2013-11-01T00:00:00Z",
            "2013-12-01T00:00:00Z",
            "2014-01-01T00:00:00Z",
            "2014-02-01T00:00:00Z",
            "2014-03-01T00:00:00Z",
            "2014-04-01T00:00:00Z",
            "2014-05-01T00:00:00Z",
            "2014-06-01T00:00:00Z",
            "2014-07-01T00:00:00Z",
            "2014-08-01T00:00:00Z",
            "2014-09-01T00:00:00Z",
            "2014-10-01T00:00:00Z",
            "2014-11-01T00:00:00Z",
            "2014-12-01T00:00:00Z",
            "2015-01-01T00:00:00Z",
            "2015-02-01T00:00:00Z",
            "2015-03-01T00:00:00Z",
            "2015-04-01T00:00:00Z",
            "2015-05-01T00:00:00Z",
            "2015-06-01T00:00:00Z",
            "2015-07-01T00:00:00Z",
            "2015-08-01T00:00:00Z",
            "2015-09-01T00:00:00Z",
            "2015-10-01T00:00:00Z",
            "2015-11-01T00:00:00Z",
            "2015-12-01T00:00:00Z",
            "2016-01-01T00:00:00Z",
            "2016-02-01T00:00:00Z",
            "2016-03-01T00:00:00Z",
            "2016-04-01T00:00:00Z",
            "2016-05-01T00:00:00Z",
            "2016-06-01T00:00:00Z",
            "2016-07-01T00:00:00Z",
            "2016-08-01T00:00:00Z",
            "2016-09-01T00:00:00Z",
            "2016-10-01T00:00:00Z",
            "2016-11-01T00:00:00Z",
            "2016-12-01T00:00:00Z",
            "2017-01-01T00:00:00Z",
            "2017-02-01T00:00:00Z",
            "2017-03-01T00:00:00Z",
            "2017-04-01T00:00:00Z",
            "2017-05-01T00:00:00Z",
            "2017-06-01T00:00:00Z",
            "2017-07-01T00:00:00Z",
            "2017-08-01T00:00:00Z",
            "2017-09-01T00:00:00Z",
            "2017-10-01T00:00:00Z",
            "2017-11-01T00:00:00Z",
            "2017-12-01T00:00:00Z",
            "2018-01-01T00:00:00Z",
            "2018-02-01T00:00:00Z",
            "2018-03-01T00:00:00Z",
            "2018-04-01T00:00:00Z",
            "2018-05-01T00:00:00Z",
            "2018-06-01T00:00:00Z",
            "2018-07-01T00:00:00Z",
            "2018-08-01T00:00:00Z",
            "2018-09-01T00:00:00Z",
            "2018-10-01T00:00:00Z",
            "2018-11-01T00:00:00Z",
            "2018-12-01T00:00:00Z",
            "2019-01-01T00:00:00Z",
            "2019-02-01T00:00:00Z",
            "2019-03-01T00:00:00Z",
            "2019-04-01T00:00:00Z",
            "2019-05-01T00:00:00Z",
            "2019-06-01T00:00:00Z",
            "2019-07-01T00:00:00Z",
            "2019-08-01T00:00:00Z",
            "2019-09-01T00:00:00Z",
            "2019-10-01T00:00:00Z",
            "2019-11-01T00:00:00Z",
            "2019-12-01T00:00:00Z",
            "2020-01-01T00:00:00Z",
            "2020-02-01T00:00:00Z",
            "2020-03-01T00:00:00Z",
            "2020-04-01T00:00:00Z",
            "2020-05-01T00:00:00Z",
            "2020-06-01T00:00:00Z",
            "2020-07-01T00:00:00Z",
            "2020-08-01T00:00:00Z",
            "2020-09-01T00:00:00Z",
            "2020-10-01T00:00:00Z",
            "2020-11-01T00:00:00Z",
            "2020-12-01T00:00:00Z",
            "2021-01-01T00:00:00Z",
            "2021-02-01T00:00:00Z",
            "2021-03-01T00:00:00Z",
            "2021-04-01T00:00:00Z",
            "2021-05-01T00:00:00Z",
            "2021-06-01T00:00:00Z",
            "2021-07-01T00:00:00Z",
            "2021-08-01T00:00:00Z",
            "2021-09-01T00:00:00Z",
            "2021-10-01T00:00:00Z",
            "2021-11-01T00:00:00Z",
            "2021-12-01T00:00:00Z",
            "2022-01-01T00:00:00Z",
            "2022-02-01T00:00:00Z",
            "2022-03-01T00:00:00Z",
            "2022-04-01T00:00:00Z",
            "2022-05-01T00:00:00Z",
            "2022-06-01T00:00:00Z",
            "2022-07-01T00:00:00Z",
            "2022-08-01T00:00:00Z",
            "2022-09-01T00:00:00Z",
            "2022-10-01T00:00:00Z",
            "2022-11-01T00:00:00Z",
            "2022-12-01T00:00:00Z",
            "2023-01-01T00:00:00Z",
            "2023-02-01T00:00:00Z",
            "2023-03-01T00:00:00Z",
            "2023-04-01T00:00:00Z",
            "2023-05-01T00:00:00Z",
            "2023-06-01T00:00:00Z",
            "2023-07-01T00:00:00Z",
            "2023-08-01T00:00:00Z",
            "2023-09-01T00:00:00Z",
            "2023-10-01T00:00:00Z",
            "2023-11-01T00:00:00Z",
        ],
    )
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        end_datetime=None,
        start_datetime=None,
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
