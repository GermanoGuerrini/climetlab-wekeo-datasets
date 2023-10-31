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


class satellite_lake_water_level(Main):
    name = "EO:ECMWF:DAT:SATELLITE_LAKE_WATER_LEVEL"
    dataset = "EO:ECMWF:DAT:SATELLITE_LAKE_WATER_LEVEL"

    choices = [
        "variable",
        "version",
        "format_",
    ]

    string_selects = [
        "lake",
        "region",
    ]

    @normalize(
        "lake",
        [
            "achit",
            "alakol",
            "albert",
            "amadjuak",
            "american_falls",
            "aqqikol_hu",
            "argentino",
            "athabasca",
            "ayakkum",
            "aydarkul",
            "aylmer",
            "azhibeksorkoli",
            "bagre",
            "baikal",
            "bairab",
            "baker",
            "balbina",
            "balkhash",
            "bangweulu",
            "bankim",
            "baunt",
            "beas",
            "beysehir",
            "bienville",
            "big_trout",
            "birch",
            "biylikol",
            "bluenose",
            "bodensee",
            "bogoria",
            "bosten",
            "bratskoye",
            "bugunskoye",
            "cahora_bassa",
            "caribou",
            "caspian",
            "cayuga",
            "cedar",
            "cerros_colorados",
            "chagbo_co",
            "chapala",
            "chardarya",
            "chatyrkol",
            "chishi",
            "chlya",
            "chocon",
            "chukochye",
            "cienagachilloa",
            "claire",
            "cochrane",
            "corangamite",
            "cuodarima",
            "dagze_co",
            "dalai",
            "danau_towuti",
            "danausingkarak",
            "dangqiong",
            "des_bois",
            "dogaicoring_q",
            "dorgon",
            "dorsoidong_co",
            "dubawnt",
            "edouard",
            "egridir",
            "erie",
            "faber",
            "fitri",
            "fontana",
            "fort_peck",
            "garkung",
            "george",
            "gods",
            "grande_trois",
            "greatslave",
            "guri",
            "gyaring_co",
            "gyeze_caka",
            "habbaniyah",
            "hala",
            "hamrin",
            "har",
            "hawizeh_marshes",
            "heishi_beihu",
            "hendrik_verwoerd",
            "hinojo",
            "hoh_xil_hu",
            "hongze",
            "hottah",
            "hovsgol",
            "hulun",
            "huron",
            "hyargas",
            "iliamna",
            "illmen",
            "inarinjarvi",
            "issykkul",
            "iznik",
            "jayakwadi",
            "kabele",
            "kabwe",
            "kainji",
            "kairakum",
            "kamilukuak",
            "kamyshlybas",
            "kapchagayskoye",
            "kara_bogaz_gol",
            "karasor",
            "kariba",
            "kasba",
            "khanka",
            "kinkony",
            "kisale",
            "kivu",
            "kokonor",
            "kossou",
            "krasnoyarskoye",
            "kremenchutska",
            "kubenskoye",
            "kulundinskoye",
            "kumskoye",
            "kuybyshevskoye",
            "kyoga",
            "ladoga",
            "lagdo",
            "lagoa_dos_patos",
            "langa_co",
            "langano",
            "lano",
            "leman",
            "lixiodain_co",
            "lumajangdong_co",
            "luotuo",
            "mai_ndombe",
            "malawi",
            "mangbeto",
            "manitoba",
            "memar",
            "michigan",
            "migriggyangzham",
            "mingacevir",
            "mono",
            "mossoul",
            "mullet",
            "mweru",
            "naivasha",
            "namco",
            "namngum",
            "nasser",
            "nezahualcoyoti",
            "ngangze",
            "ngoring_co",
            "nicaragua",
            "nipissing",
            "novosibirskoye",
            "nueltin",
            "oahe",
            "old_wives",
            "onega",
            "ontario",
            "opinac",
            "peipus",
            "prespa",
            "pukaki",
            "pyaozero",
            "ranco",
            "roseires",
            "rukwa",
            "rybinskoye",
            "saint_jean",
            "sakakawea",
            "saksak",
            "san_martin",
            "saratovskoye",
            "sarykamish",
            "sasykkol",
            "saysan",
            "segozerskoye",
            "serbug",
            "sevan",
            "shiroro",
            "sobradino",
            "soungari",
            "srisailam",
            "superior",
            "swan",
            "tana",
            "tanganika",
            "tangra_yumco",
            "tchad",
            "tchany",
            "telashi",
            "teletskoye",
            "telmen",
            "tengiz",
            "tharthar",
            "titicaca",
            "todos_los_santos",
            "toktogul",
            "tonle_sap",
            "tres_marias",
            "tsimlyanskoye",
            "tumba",
            "turkana",
            "ulan_ul",
            "ulungur",
            "umbozero",
            "uvs",
            "valencia",
            "van",
            "vanajanselka",
            "vanerm",
            "vattern",
            "victoria",
            "viedma",
            "volta",
            "walker",
            "williston",
            "winnipeg",
            "winnipegosis",
            "xiangyang",
            "yamzho_yumco",
            "yellowstone",
            "zeyskoye",
            "zhari_namco",
            "zhelin",
            "ziling",
            "zimbambo",
            "ziway",
            "zonag",
        ],
        multiple=True,
    )
    @normalize(
        "region",
        [
            "northern_africa",
            "northern_asia",
            "northern_europe",
            "northern_north_america",
            "oceania",
            "southeastern_asia",
            "southern_africa",
            "southern_america",
            "southern_europe",
            "southern_north_america",
            "southwestern_asia",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "version_2_1",
            "version_3_1",
            "version_4_0",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    @normalize(
        "variable",
        [
            "all",
        ],
    )
    def __init__(
        self,
        lake,
        region,
        version=None,
        format_=None,
        variable="all",
    ):
        super().__init__(
            lake=lake,
            region=region,
            version=version,
            format_=format_,
            variable=variable,
        )
