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
    "dataset-carbon-rep-monthly_202311",  # noqa: E501 dataset-carbon-rep-monthly
]


class multiobs_glo_bio_carbon_surface_rep(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_BIO_CARBON_SURFACE_REP_015_008"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_BIO_CARBON_SURFACE_REP_015_008"

    @normalize(
        "variables",
        [
            "fgco2",
            "fgco2_uncertainty",
            "omega_ar",
            "omega_ar_uncertainty",
            "omega_ca",
            "omega_ca_uncertainty",
            "ph",
            "ph_uncertainty",
            "spco2",
            "spco2_uncertainty",
            "talk",
            "talk_uncertainty",
            "tco2",
            "tco2_uncertainty",
        ],
        multiple=True,
    )
    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "end_datetime",
        [
            "1985-01-01T00:00:00Z",
            "1985-02-01T00:00:00Z",
            "1985-03-01T00:00:00Z",
            "1985-04-01T00:00:00Z",
            "1985-05-01T00:00:00Z",
            "1985-06-01T00:00:00Z",
            "1985-07-01T00:00:00Z",
            "1985-08-01T00:00:00Z",
            "1985-09-01T00:00:00Z",
            "1985-10-01T00:00:00Z",
            "1985-11-01T00:00:00Z",
            "1985-12-01T00:00:00Z",
            "1986-01-01T00:00:00Z",
            "1986-02-01T00:00:00Z",
            "1986-03-01T00:00:00Z",
            "1986-04-01T00:00:00Z",
            "1986-05-01T00:00:00Z",
            "1986-06-01T00:00:00Z",
            "1986-07-01T00:00:00Z",
            "1986-08-01T00:00:00Z",
            "1986-09-01T00:00:00Z",
            "1986-10-01T00:00:00Z",
            "1986-11-01T00:00:00Z",
            "1986-12-01T00:00:00Z",
            "1987-01-01T00:00:00Z",
            "1987-02-01T00:00:00Z",
            "1987-03-01T00:00:00Z",
            "1987-04-01T00:00:00Z",
            "1987-05-01T00:00:00Z",
            "1987-06-01T00:00:00Z",
            "1987-07-01T00:00:00Z",
            "1987-08-01T00:00:00Z",
            "1987-09-01T00:00:00Z",
            "1987-10-01T00:00:00Z",
            "1987-11-01T00:00:00Z",
            "1987-12-01T00:00:00Z",
            "1988-01-01T00:00:00Z",
            "1988-02-01T00:00:00Z",
            "1988-03-01T00:00:00Z",
            "1988-04-01T00:00:00Z",
            "1988-05-01T00:00:00Z",
            "1988-06-01T00:00:00Z",
            "1988-07-01T00:00:00Z",
            "1988-08-01T00:00:00Z",
            "1988-09-01T00:00:00Z",
            "1988-10-01T00:00:00Z",
            "1988-11-01T00:00:00Z",
            "1988-12-01T00:00:00Z",
            "1989-01-01T00:00:00Z",
            "1989-02-01T00:00:00Z",
            "1989-03-01T00:00:00Z",
            "1989-04-01T00:00:00Z",
            "1989-05-01T00:00:00Z",
            "1989-06-01T00:00:00Z",
            "1989-07-01T00:00:00Z",
            "1989-08-01T00:00:00Z",
            "1989-09-01T00:00:00Z",
            "1989-10-01T00:00:00Z",
            "1989-11-01T00:00:00Z",
            "1989-12-01T00:00:00Z",
            "1990-01-01T00:00:00Z",
            "1990-02-01T00:00:00Z",
            "1990-03-01T00:00:00Z",
            "1990-04-01T00:00:00Z",
            "1990-05-01T00:00:00Z",
            "1990-06-01T00:00:00Z",
            "1990-07-01T00:00:00Z",
            "1990-08-01T00:00:00Z",
            "1990-09-01T00:00:00Z",
            "1990-10-01T00:00:00Z",
            "1990-11-01T00:00:00Z",
            "1990-12-01T00:00:00Z",
            "1991-01-01T00:00:00Z",
            "1991-02-01T00:00:00Z",
            "1991-03-01T00:00:00Z",
            "1991-04-01T00:00:00Z",
            "1991-05-01T00:00:00Z",
            "1991-06-01T00:00:00Z",
            "1991-07-01T00:00:00Z",
            "1991-08-01T00:00:00Z",
            "1991-09-01T00:00:00Z",
            "1991-10-01T00:00:00Z",
            "1991-11-01T00:00:00Z",
            "1991-12-01T00:00:00Z",
            "1992-01-01T00:00:00Z",
            "1992-02-01T00:00:00Z",
            "1992-03-01T00:00:00Z",
            "1992-04-01T00:00:00Z",
            "1992-05-01T00:00:00Z",
            "1992-06-01T00:00:00Z",
            "1992-07-01T00:00:00Z",
            "1992-08-01T00:00:00Z",
            "1992-09-01T00:00:00Z",
            "1992-10-01T00:00:00Z",
            "1992-11-01T00:00:00Z",
            "1992-12-01T00:00:00Z",
            "1993-01-01T00:00:00Z",
            "1993-02-01T00:00:00Z",
            "1993-03-01T00:00:00Z",
            "1993-04-01T00:00:00Z",
            "1993-05-01T00:00:00Z",
            "1993-06-01T00:00:00Z",
            "1993-07-01T00:00:00Z",
            "1993-08-01T00:00:00Z",
            "1993-09-01T00:00:00Z",
            "1993-10-01T00:00:00Z",
            "1993-11-01T00:00:00Z",
            "1993-12-01T00:00:00Z",
            "1994-01-01T00:00:00Z",
            "1994-02-01T00:00:00Z",
            "1994-03-01T00:00:00Z",
            "1994-04-01T00:00:00Z",
            "1994-05-01T00:00:00Z",
            "1994-06-01T00:00:00Z",
            "1994-07-01T00:00:00Z",
            "1994-08-01T00:00:00Z",
            "1994-09-01T00:00:00Z",
            "1994-10-01T00:00:00Z",
            "1994-11-01T00:00:00Z",
            "1994-12-01T00:00:00Z",
            "1995-01-01T00:00:00Z",
            "1995-02-01T00:00:00Z",
            "1995-03-01T00:00:00Z",
            "1995-04-01T00:00:00Z",
            "1995-05-01T00:00:00Z",
            "1995-06-01T00:00:00Z",
            "1995-07-01T00:00:00Z",
            "1995-08-01T00:00:00Z",
            "1995-09-01T00:00:00Z",
            "1995-10-01T00:00:00Z",
            "1995-11-01T00:00:00Z",
            "1995-12-01T00:00:00Z",
            "1996-01-01T00:00:00Z",
            "1996-02-01T00:00:00Z",
            "1996-03-01T00:00:00Z",
            "1996-04-01T00:00:00Z",
            "1996-05-01T00:00:00Z",
            "1996-06-01T00:00:00Z",
            "1996-07-01T00:00:00Z",
            "1996-08-01T00:00:00Z",
            "1996-09-01T00:00:00Z",
            "1996-10-01T00:00:00Z",
            "1996-11-01T00:00:00Z",
            "1996-12-01T00:00:00Z",
            "1997-01-01T00:00:00Z",
            "1997-02-01T00:00:00Z",
            "1997-03-01T00:00:00Z",
            "1997-04-01T00:00:00Z",
            "1997-05-01T00:00:00Z",
            "1997-06-01T00:00:00Z",
            "1997-07-01T00:00:00Z",
            "1997-08-01T00:00:00Z",
            "1997-09-01T00:00:00Z",
            "1997-10-01T00:00:00Z",
            "1997-11-01T00:00:00Z",
            "1997-12-01T00:00:00Z",
            "1998-01-01T00:00:00Z",
            "1998-02-01T00:00:00Z",
            "1998-03-01T00:00:00Z",
            "1998-04-01T00:00:00Z",
            "1998-05-01T00:00:00Z",
            "1998-06-01T00:00:00Z",
            "1998-07-01T00:00:00Z",
            "1998-08-01T00:00:00Z",
            "1998-09-01T00:00:00Z",
            "1998-10-01T00:00:00Z",
            "1998-11-01T00:00:00Z",
            "1998-12-01T00:00:00Z",
            "1999-01-01T00:00:00Z",
            "1999-02-01T00:00:00Z",
            "1999-03-01T00:00:00Z",
            "1999-04-01T00:00:00Z",
            "1999-05-01T00:00:00Z",
            "1999-06-01T00:00:00Z",
            "1999-07-01T00:00:00Z",
            "1999-08-01T00:00:00Z",
            "1999-09-01T00:00:00Z",
            "1999-10-01T00:00:00Z",
            "1999-11-01T00:00:00Z",
            "1999-12-01T00:00:00Z",
            "2000-01-01T00:00:00Z",
            "2000-02-01T00:00:00Z",
            "2000-03-01T00:00:00Z",
            "2000-04-01T00:00:00Z",
            "2000-05-01T00:00:00Z",
            "2000-06-01T00:00:00Z",
            "2000-07-01T00:00:00Z",
            "2000-08-01T00:00:00Z",
            "2000-09-01T00:00:00Z",
            "2000-10-01T00:00:00Z",
            "2000-11-01T00:00:00Z",
            "2000-12-01T00:00:00Z",
            "2001-01-01T00:00:00Z",
            "2001-02-01T00:00:00Z",
            "2001-03-01T00:00:00Z",
            "2001-04-01T00:00:00Z",
            "2001-05-01T00:00:00Z",
            "2001-06-01T00:00:00Z",
            "2001-07-01T00:00:00Z",
            "2001-08-01T00:00:00Z",
            "2001-09-01T00:00:00Z",
            "2001-10-01T00:00:00Z",
            "2001-11-01T00:00:00Z",
            "2001-12-01T00:00:00Z",
            "2002-01-01T00:00:00Z",
            "2002-02-01T00:00:00Z",
            "2002-03-01T00:00:00Z",
            "2002-04-01T00:00:00Z",
            "2002-05-01T00:00:00Z",
            "2002-06-01T00:00:00Z",
            "2002-07-01T00:00:00Z",
            "2002-08-01T00:00:00Z",
            "2002-09-01T00:00:00Z",
            "2002-10-01T00:00:00Z",
            "2002-11-01T00:00:00Z",
            "2002-12-01T00:00:00Z",
            "2003-01-01T00:00:00Z",
            "2003-02-01T00:00:00Z",
            "2003-03-01T00:00:00Z",
            "2003-04-01T00:00:00Z",
            "2003-05-01T00:00:00Z",
            "2003-06-01T00:00:00Z",
            "2003-07-01T00:00:00Z",
            "2003-08-01T00:00:00Z",
            "2003-09-01T00:00:00Z",
            "2003-10-01T00:00:00Z",
            "2003-11-01T00:00:00Z",
            "2003-12-01T00:00:00Z",
            "2004-01-01T00:00:00Z",
            "2004-02-01T00:00:00Z",
            "2004-03-01T00:00:00Z",
            "2004-04-01T00:00:00Z",
            "2004-05-01T00:00:00Z",
            "2004-06-01T00:00:00Z",
            "2004-07-01T00:00:00Z",
            "2004-08-01T00:00:00Z",
            "2004-09-01T00:00:00Z",
            "2004-10-01T00:00:00Z",
            "2004-11-01T00:00:00Z",
            "2004-12-01T00:00:00Z",
            "2005-01-01T00:00:00Z",
            "2005-02-01T00:00:00Z",
            "2005-03-01T00:00:00Z",
            "2005-04-01T00:00:00Z",
            "2005-05-01T00:00:00Z",
            "2005-06-01T00:00:00Z",
            "2005-07-01T00:00:00Z",
            "2005-08-01T00:00:00Z",
            "2005-09-01T00:00:00Z",
            "2005-10-01T00:00:00Z",
            "2005-11-01T00:00:00Z",
            "2005-12-01T00:00:00Z",
            "2006-01-01T00:00:00Z",
            "2006-02-01T00:00:00Z",
            "2006-03-01T00:00:00Z",
            "2006-04-01T00:00:00Z",
            "2006-05-01T00:00:00Z",
            "2006-06-01T00:00:00Z",
            "2006-07-01T00:00:00Z",
            "2006-08-01T00:00:00Z",
            "2006-09-01T00:00:00Z",
            "2006-10-01T00:00:00Z",
            "2006-11-01T00:00:00Z",
            "2006-12-01T00:00:00Z",
            "2007-01-01T00:00:00Z",
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
        ],
    )
    @normalize(
        "start_datetime",
        [
            "1985-01-01T00:00:00Z",
            "1985-02-01T00:00:00Z",
            "1985-03-01T00:00:00Z",
            "1985-04-01T00:00:00Z",
            "1985-05-01T00:00:00Z",
            "1985-06-01T00:00:00Z",
            "1985-07-01T00:00:00Z",
            "1985-08-01T00:00:00Z",
            "1985-09-01T00:00:00Z",
            "1985-10-01T00:00:00Z",
            "1985-11-01T00:00:00Z",
            "1985-12-01T00:00:00Z",
            "1986-01-01T00:00:00Z",
            "1986-02-01T00:00:00Z",
            "1986-03-01T00:00:00Z",
            "1986-04-01T00:00:00Z",
            "1986-05-01T00:00:00Z",
            "1986-06-01T00:00:00Z",
            "1986-07-01T00:00:00Z",
            "1986-08-01T00:00:00Z",
            "1986-09-01T00:00:00Z",
            "1986-10-01T00:00:00Z",
            "1986-11-01T00:00:00Z",
            "1986-12-01T00:00:00Z",
            "1987-01-01T00:00:00Z",
            "1987-02-01T00:00:00Z",
            "1987-03-01T00:00:00Z",
            "1987-04-01T00:00:00Z",
            "1987-05-01T00:00:00Z",
            "1987-06-01T00:00:00Z",
            "1987-07-01T00:00:00Z",
            "1987-08-01T00:00:00Z",
            "1987-09-01T00:00:00Z",
            "1987-10-01T00:00:00Z",
            "1987-11-01T00:00:00Z",
            "1987-12-01T00:00:00Z",
            "1988-01-01T00:00:00Z",
            "1988-02-01T00:00:00Z",
            "1988-03-01T00:00:00Z",
            "1988-04-01T00:00:00Z",
            "1988-05-01T00:00:00Z",
            "1988-06-01T00:00:00Z",
            "1988-07-01T00:00:00Z",
            "1988-08-01T00:00:00Z",
            "1988-09-01T00:00:00Z",
            "1988-10-01T00:00:00Z",
            "1988-11-01T00:00:00Z",
            "1988-12-01T00:00:00Z",
            "1989-01-01T00:00:00Z",
            "1989-02-01T00:00:00Z",
            "1989-03-01T00:00:00Z",
            "1989-04-01T00:00:00Z",
            "1989-05-01T00:00:00Z",
            "1989-06-01T00:00:00Z",
            "1989-07-01T00:00:00Z",
            "1989-08-01T00:00:00Z",
            "1989-09-01T00:00:00Z",
            "1989-10-01T00:00:00Z",
            "1989-11-01T00:00:00Z",
            "1989-12-01T00:00:00Z",
            "1990-01-01T00:00:00Z",
            "1990-02-01T00:00:00Z",
            "1990-03-01T00:00:00Z",
            "1990-04-01T00:00:00Z",
            "1990-05-01T00:00:00Z",
            "1990-06-01T00:00:00Z",
            "1990-07-01T00:00:00Z",
            "1990-08-01T00:00:00Z",
            "1990-09-01T00:00:00Z",
            "1990-10-01T00:00:00Z",
            "1990-11-01T00:00:00Z",
            "1990-12-01T00:00:00Z",
            "1991-01-01T00:00:00Z",
            "1991-02-01T00:00:00Z",
            "1991-03-01T00:00:00Z",
            "1991-04-01T00:00:00Z",
            "1991-05-01T00:00:00Z",
            "1991-06-01T00:00:00Z",
            "1991-07-01T00:00:00Z",
            "1991-08-01T00:00:00Z",
            "1991-09-01T00:00:00Z",
            "1991-10-01T00:00:00Z",
            "1991-11-01T00:00:00Z",
            "1991-12-01T00:00:00Z",
            "1992-01-01T00:00:00Z",
            "1992-02-01T00:00:00Z",
            "1992-03-01T00:00:00Z",
            "1992-04-01T00:00:00Z",
            "1992-05-01T00:00:00Z",
            "1992-06-01T00:00:00Z",
            "1992-07-01T00:00:00Z",
            "1992-08-01T00:00:00Z",
            "1992-09-01T00:00:00Z",
            "1992-10-01T00:00:00Z",
            "1992-11-01T00:00:00Z",
            "1992-12-01T00:00:00Z",
            "1993-01-01T00:00:00Z",
            "1993-02-01T00:00:00Z",
            "1993-03-01T00:00:00Z",
            "1993-04-01T00:00:00Z",
            "1993-05-01T00:00:00Z",
            "1993-06-01T00:00:00Z",
            "1993-07-01T00:00:00Z",
            "1993-08-01T00:00:00Z",
            "1993-09-01T00:00:00Z",
            "1993-10-01T00:00:00Z",
            "1993-11-01T00:00:00Z",
            "1993-12-01T00:00:00Z",
            "1994-01-01T00:00:00Z",
            "1994-02-01T00:00:00Z",
            "1994-03-01T00:00:00Z",
            "1994-04-01T00:00:00Z",
            "1994-05-01T00:00:00Z",
            "1994-06-01T00:00:00Z",
            "1994-07-01T00:00:00Z",
            "1994-08-01T00:00:00Z",
            "1994-09-01T00:00:00Z",
            "1994-10-01T00:00:00Z",
            "1994-11-01T00:00:00Z",
            "1994-12-01T00:00:00Z",
            "1995-01-01T00:00:00Z",
            "1995-02-01T00:00:00Z",
            "1995-03-01T00:00:00Z",
            "1995-04-01T00:00:00Z",
            "1995-05-01T00:00:00Z",
            "1995-06-01T00:00:00Z",
            "1995-07-01T00:00:00Z",
            "1995-08-01T00:00:00Z",
            "1995-09-01T00:00:00Z",
            "1995-10-01T00:00:00Z",
            "1995-11-01T00:00:00Z",
            "1995-12-01T00:00:00Z",
            "1996-01-01T00:00:00Z",
            "1996-02-01T00:00:00Z",
            "1996-03-01T00:00:00Z",
            "1996-04-01T00:00:00Z",
            "1996-05-01T00:00:00Z",
            "1996-06-01T00:00:00Z",
            "1996-07-01T00:00:00Z",
            "1996-08-01T00:00:00Z",
            "1996-09-01T00:00:00Z",
            "1996-10-01T00:00:00Z",
            "1996-11-01T00:00:00Z",
            "1996-12-01T00:00:00Z",
            "1997-01-01T00:00:00Z",
            "1997-02-01T00:00:00Z",
            "1997-03-01T00:00:00Z",
            "1997-04-01T00:00:00Z",
            "1997-05-01T00:00:00Z",
            "1997-06-01T00:00:00Z",
            "1997-07-01T00:00:00Z",
            "1997-08-01T00:00:00Z",
            "1997-09-01T00:00:00Z",
            "1997-10-01T00:00:00Z",
            "1997-11-01T00:00:00Z",
            "1997-12-01T00:00:00Z",
            "1998-01-01T00:00:00Z",
            "1998-02-01T00:00:00Z",
            "1998-03-01T00:00:00Z",
            "1998-04-01T00:00:00Z",
            "1998-05-01T00:00:00Z",
            "1998-06-01T00:00:00Z",
            "1998-07-01T00:00:00Z",
            "1998-08-01T00:00:00Z",
            "1998-09-01T00:00:00Z",
            "1998-10-01T00:00:00Z",
            "1998-11-01T00:00:00Z",
            "1998-12-01T00:00:00Z",
            "1999-01-01T00:00:00Z",
            "1999-02-01T00:00:00Z",
            "1999-03-01T00:00:00Z",
            "1999-04-01T00:00:00Z",
            "1999-05-01T00:00:00Z",
            "1999-06-01T00:00:00Z",
            "1999-07-01T00:00:00Z",
            "1999-08-01T00:00:00Z",
            "1999-09-01T00:00:00Z",
            "1999-10-01T00:00:00Z",
            "1999-11-01T00:00:00Z",
            "1999-12-01T00:00:00Z",
            "2000-01-01T00:00:00Z",
            "2000-02-01T00:00:00Z",
            "2000-03-01T00:00:00Z",
            "2000-04-01T00:00:00Z",
            "2000-05-01T00:00:00Z",
            "2000-06-01T00:00:00Z",
            "2000-07-01T00:00:00Z",
            "2000-08-01T00:00:00Z",
            "2000-09-01T00:00:00Z",
            "2000-10-01T00:00:00Z",
            "2000-11-01T00:00:00Z",
            "2000-12-01T00:00:00Z",
            "2001-01-01T00:00:00Z",
            "2001-02-01T00:00:00Z",
            "2001-03-01T00:00:00Z",
            "2001-04-01T00:00:00Z",
            "2001-05-01T00:00:00Z",
            "2001-06-01T00:00:00Z",
            "2001-07-01T00:00:00Z",
            "2001-08-01T00:00:00Z",
            "2001-09-01T00:00:00Z",
            "2001-10-01T00:00:00Z",
            "2001-11-01T00:00:00Z",
            "2001-12-01T00:00:00Z",
            "2002-01-01T00:00:00Z",
            "2002-02-01T00:00:00Z",
            "2002-03-01T00:00:00Z",
            "2002-04-01T00:00:00Z",
            "2002-05-01T00:00:00Z",
            "2002-06-01T00:00:00Z",
            "2002-07-01T00:00:00Z",
            "2002-08-01T00:00:00Z",
            "2002-09-01T00:00:00Z",
            "2002-10-01T00:00:00Z",
            "2002-11-01T00:00:00Z",
            "2002-12-01T00:00:00Z",
            "2003-01-01T00:00:00Z",
            "2003-02-01T00:00:00Z",
            "2003-03-01T00:00:00Z",
            "2003-04-01T00:00:00Z",
            "2003-05-01T00:00:00Z",
            "2003-06-01T00:00:00Z",
            "2003-07-01T00:00:00Z",
            "2003-08-01T00:00:00Z",
            "2003-09-01T00:00:00Z",
            "2003-10-01T00:00:00Z",
            "2003-11-01T00:00:00Z",
            "2003-12-01T00:00:00Z",
            "2004-01-01T00:00:00Z",
            "2004-02-01T00:00:00Z",
            "2004-03-01T00:00:00Z",
            "2004-04-01T00:00:00Z",
            "2004-05-01T00:00:00Z",
            "2004-06-01T00:00:00Z",
            "2004-07-01T00:00:00Z",
            "2004-08-01T00:00:00Z",
            "2004-09-01T00:00:00Z",
            "2004-10-01T00:00:00Z",
            "2004-11-01T00:00:00Z",
            "2004-12-01T00:00:00Z",
            "2005-01-01T00:00:00Z",
            "2005-02-01T00:00:00Z",
            "2005-03-01T00:00:00Z",
            "2005-04-01T00:00:00Z",
            "2005-05-01T00:00:00Z",
            "2005-06-01T00:00:00Z",
            "2005-07-01T00:00:00Z",
            "2005-08-01T00:00:00Z",
            "2005-09-01T00:00:00Z",
            "2005-10-01T00:00:00Z",
            "2005-11-01T00:00:00Z",
            "2005-12-01T00:00:00Z",
            "2006-01-01T00:00:00Z",
            "2006-02-01T00:00:00Z",
            "2006-03-01T00:00:00Z",
            "2006-04-01T00:00:00Z",
            "2006-05-01T00:00:00Z",
            "2006-06-01T00:00:00Z",
            "2006-07-01T00:00:00Z",
            "2006-08-01T00:00:00Z",
            "2006-09-01T00:00:00Z",
            "2006-10-01T00:00:00Z",
            "2006-11-01T00:00:00Z",
            "2006-12-01T00:00:00Z",
            "2007-01-01T00:00:00Z",
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
        ],
    )
    def __init__(
        self,
        variables,
        layer="dataset-carbon-rep-monthly_202311",
        bbox=None,
        end_datetime=None,
        start_datetime=None,
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
