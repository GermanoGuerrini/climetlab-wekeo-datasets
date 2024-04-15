#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.ecmwf.main import Main


class insitu_gridded_observations_global_and_regional(Main):
    name = "EO:ECMWF:DAT:INSITU_GRIDDED_OBSERVATIONS_GLOBAL_AND_REGIONAL"
    dataset = "EO:ECMWF:DAT:INSITU_GRIDDED_OBSERVATIONS_GLOBAL_AND_REGIONAL"

    @normalize(
        "origin",
        [
            "berkearth",
            "chirps",
            "cmorph",
            "cpc",
            "cpc_conus",
            "cru",
            "gistemp",
            "gpcc",
            "imerg",
        ],
    )
    @normalize(
        "region",
        [
            "africa",
            "conus",
            "global",
            "quasi_global",
        ],
    )
    @normalize(
        "variable",
        [
            "precipitation",
            "temperature",
            "temperature_anomaly",
        ],
        multiple=True,
    )
    @normalize(
        "statistic",
        [
            "maximum",
            "mean",
            "minimum",
        ],
        multiple=True,
    )
    @normalize(
        "time_aggregation",
        [
            "daily",
            "monthly",
        ],
    )
    @normalize(
        "horizontal_aggregation",
        [
            "0_25_x_0_25",
            "0_2_x_0_2",
            "0_5_x_0_5",
            "1_x_1",
            "2_5_x_2_5",
            "horizontal_average",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1750",
            "1751",
            "1752",
            "1753",
            "1754",
            "1755",
            "1756",
            "1757",
            "1758",
            "1759",
            "1760",
            "1761",
            "1762",
            "1763",
            "1764",
            "1765",
            "1766",
            "1767",
            "1768",
            "1769",
            "1770",
            "1771",
            "1772",
            "1773",
            "1774",
            "1775",
            "1776",
            "1777",
            "1778",
            "1779",
            "1780",
            "1781",
            "1782",
            "1783",
            "1784",
            "1785",
            "1786",
            "1787",
            "1788",
            "1789",
            "1790",
            "1791",
            "1792",
            "1793",
            "1794",
            "1795",
            "1796",
            "1797",
            "1798",
            "1799",
            "1800",
            "1801",
            "1802",
            "1803",
            "1804",
            "1805",
            "1806",
            "1807",
            "1808",
            "1809",
            "1810",
            "1811",
            "1812",
            "1813",
            "1814",
            "1815",
            "1816",
            "1817",
            "1818",
            "1819",
            "1820",
            "1821",
            "1822",
            "1823",
            "1824",
            "1825",
            "1826",
            "1827",
            "1828",
            "1829",
            "1830",
            "1831",
            "1832",
            "1833",
            "1834",
            "1835",
            "1836",
            "1837",
            "1838",
            "1839",
            "1840",
            "1841",
            "1842",
            "1843",
            "1844",
            "1845",
            "1846",
            "1847",
            "1848",
            "1849",
            "1850",
            "1851",
            "1852",
            "1853",
            "1854",
            "1855",
            "1856",
            "1857",
            "1858",
            "1859",
            "1860",
            "1861",
            "1862",
            "1863",
            "1864",
            "1865",
            "1866",
            "1867",
            "1868",
            "1869",
            "1870",
            "1871",
            "1872",
            "1873",
            "1874",
            "1875",
            "1876",
            "1877",
            "1878",
            "1879",
            "1880",
            "1881",
            "1882",
            "1883",
            "1884",
            "1885",
            "1886",
            "1887",
            "1888",
            "1889",
            "1890",
            "1891",
            "1892",
            "1893",
            "1894",
            "1895",
            "1896",
            "1897",
            "1898",
            "1899",
            "1900",
            "1901",
            "1902",
            "1903",
            "1904",
            "1905",
            "1906",
            "1907",
            "1908",
            "1909",
            "1910",
            "1911",
            "1912",
            "1913",
            "1914",
            "1915",
            "1916",
            "1917",
            "1918",
            "1919",
            "1920",
            "1921",
            "1922",
            "1923",
            "1924",
            "1925",
            "1926",
            "1927",
            "1928",
            "1929",
            "1930",
            "1931",
            "1932",
            "1933",
            "1934",
            "1935",
            "1936",
            "1937",
            "1938",
            "1939",
            "1940",
            "1941",
            "1942",
            "1943",
            "1944",
            "1945",
            "1946",
            "1947",
            "1948",
            "1949",
            "1950",
            "1951",
            "1952",
            "1953",
            "1954",
            "1955",
            "1956",
            "1957",
            "1958",
            "1959",
            "1960",
            "1961",
            "1962",
            "1963",
            "1964",
            "1965",
            "1966",
            "1967",
            "1968",
            "1969",
            "1970",
            "1971",
            "1972",
            "1973",
            "1974",
            "1975",
            "1976",
            "1977",
            "1978",
            "1979",
            "1980",
            "1981",
            "1982",
            "1983",
            "1984",
            "1985",
            "1986",
            "1987",
            "1988",
            "1989",
            "1990",
            "1991",
            "1992",
            "1993",
            "1994",
            "1995",
            "1996",
            "1997",
            "1998",
            "1999",
            "2000",
            "2001",
            "2002",
            "2003",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
            "2019",
            "2020",
            "2021",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "v1.0",
            "v2.0",
            "v2020.0",
            "v2020.0-v6.0-fg",
            "v4.0",
            "v4.03",
            "v6.0",
        ],
        multiple=True,
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        origin,
        region,
        variable,
        statistic,
        time_aggregation,
        horizontal_aggregation,
        year,
        version,
        format_=None,
        limit=None,
    ):
        super().__init__(
            origin=origin,
            region=region,
            variable=variable,
            statistic=statistic,
            time_aggregation=time_aggregation,
            horizontal_aggregation=horizontal_aggregation,
            year=year,
            version=version,
            format_=format_,
            limit=limit,
        )
