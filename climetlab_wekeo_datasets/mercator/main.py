#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

import climetlab as cml
import xarray as xr
from climetlab import Dataset

__version__ = "0.1.0"


class Main(Dataset):
    name = None
    home_page = "https://www.wekeo.eu/"
    # The licence is the licence of the data (not the licence of the plugin)
    licence = "https://www.copernicus.eu/en/access-data/copyright-and-licences"
    documentation = "-"
    citation = "-"

    # These are the terms of use of the data (not the licence of the plugin)
    terms_of_use = (
        "By downloading data from this dataset, "
        "you agree to the terms and conditions defined at "
        "https://www.copernicus.eu/en/access-data/copyright-and-licence"
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = None

    default_options = {
        "xarray_open_dataset_kwargs": {"chunks": "auto", "engine": "netcdf4"}
    }

    def __init__(self, *args, **kwargs):
        layer = kwargs["layer"]

        query = {"dataset_id": f"{self.dataset}:{layer}"}

        for key, value in kwargs.items():
            query[key] = value

        if query["variables"] is None:
            # Remove completely the variables argument
            # or the API will return an Unprocessable Entity
            del query["variables"]

        limit = kwargs.get("limit")

        self.source = cml.load_source("wekeo", query, limit)
        self._xarray = None

    def to_xarray(self, **kwargs):
        if self._xarray is not None:
            return self._xarray

        options = dict()
        options.update(self.default_options["xarray_open_dataset_kwargs"])
        options.update(kwargs.get("xarray_open_dataset_kwargs", {}))

        try:
            datasets = [xr.open_dataset(s, **options) for s in self.source.sources]
            array = xr.concat(datasets, dim="time")
            self._xarray = array
            return self._xarray
        except (AttributeError, ValueError):
            # Single file
            self._xarray = super().to_xarray(**options)
            return self._xarray
