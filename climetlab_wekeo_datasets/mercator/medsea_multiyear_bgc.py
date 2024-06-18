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
    "cmems_mod_med_bgc-bio_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_bgc-bio_my_4.2km_P1Y-m
    "cmems_mod_med_bgc-bio_myint_4.2km_P1M-m_202112",  # noqa: E501 cmems_mod_med_bgc-bio_myint_4.2km_P1M-m
    "cmems_mod_med_bgc-car_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_bgc-car_my_4.2km_P1Y-m
    "cmems_mod_med_bgc-car_myint_4.2km_P1M-m_202112",  # noqa: E501 cmems_mod_med_bgc-car_myint_4.2km_P1M-m
    "cmems_mod_med_bgc-co2_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_bgc-co2_my_4.2km_P1Y-m
    "cmems_mod_med_bgc-co2_myint_4.2km_P1M-m_202112",  # noqa: E501 cmems_mod_med_bgc-co2_myint_4.2km_P1M-m
    "cmems_mod_med_bgc-nut_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_bgc-nut_my_4.2km_P1Y-m
    "cmems_mod_med_bgc-nut_myint_4.2km_P1M-m_202112",  # noqa: E501 cmems_mod_med_bgc-nut_myint_4.2km_P1M-m
    "cmems_mod_med_bgc-pft_myint_4.2km_P1M-m_202112",  # noqa: E501 cmems_mod_med_bgc-pft_myint_4.2km_P1M-m
    "cmems_mod_med_bgc-plankton_my_4.2km_P1Y-m_202211",  # noqa: E501 cmems_mod_med_bgc-plankton_my_4.2km_P1Y-m
    "med-ogs-bio-rean-d_202105",  # noqa: E501 med-ogs-bio-rean-d
    "med-ogs-bio-rean-m_202105",  # noqa: E501 med-ogs-bio-rean-m
    "med-ogs-car-rean-d_202105",  # noqa: E501 med-ogs-car-rean-d
    "med-ogs-car-rean-m_202105",  # noqa: E501 med-ogs-car-rean-m
    "med-ogs-co2-rean-d_202105",  # noqa: E501 med-ogs-co2-rean-d
    "med-ogs-co2-rean-m_202105",  # noqa: E501 med-ogs-co2-rean-m
    "med-ogs-nut-rean-d_202105",  # noqa: E501 med-ogs-nut-rean-d
    "med-ogs-nut-rean-m_202105",  # noqa: E501 med-ogs-nut-rean-m
    "med-ogs-pft-rean-d_202105",  # noqa: E501 med-ogs-pft-rean-d
    "med-ogs-pft-rean-m_202105",  # noqa: E501 med-ogs-pft-rean-m
]


class medsea_multiyear_bgc(Main):
    name = "EO:MO:DAT:MEDSEA_MULTIYEAR_BGC_006_008"
    dataset = "EO:MO:DAT:MEDSEA_MULTIYEAR_BGC_006_008"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "chl",
            "dissic",
            "fpco2",
            "nh4",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "po4",
            "spco2",
            "talk",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-1.0182366371154785",
            "-10.536603927612305",
            "-1005.135498046875",
            "-104.94397735595703",
            "-1040.0762939453125",
            "-1075.914306640625",
            "-1112.6636962890625",
            "-112.25020599365234",
            "-1150.33837890625",
            "-1188.9521484375",
            "-119.85543060302734",
            "-1228.518798828125",
            "-1269.0517578125",
            "-127.76783752441406",
            "-13.318384170532227",
            "-1310.564208984375",
            "-135.9958038330078",
            "-1353.0693359375",
            "-1396.5799560546875",
            "-144.5478973388672",
            "-1441.108642578125",
            "-1486.6678466796875",
            "-153.43284606933594",
            "-1533.2694091796875",
            "-1580.9251708984375",
            "-16.270586013793945",
            "-162.6596221923828",
            "-1629.6466064453125",
            "-1679.44482421875",
            "-172.2373504638672",
            "-1730.330322265625",
            "-1782.3135986328125",
            "-182.17535400390625",
            "-1835.404541015625",
            "-1889.6126708984375",
            "-19.398210525512695",
            "-192.48313903808594",
            "-1944.9471435546875",
            "-2001.4166259765625",
            "-203.17044067382812",
            "-2059.029052734375",
            "-2117.79248046875",
            "-214.24716186523438",
            "-2177.714111328125",
            "-22.706392288208008",
            "-2238.80029296875",
            "-225.72340393066406",
            "-2301.0576171875",
            "-2364.49169921875",
            "-237.60946655273438",
            "-2429.107666015625",
            "-249.9158477783203",
            "-2494.91015625",
            "-2561.903076171875",
            "-26.20039939880371",
            "-262.6532287597656",
            "-2630.08984375",
            "-2699.4736328125",
            "-275.83251953125",
            "-2770.056640625",
            "-2841.8408203125",
            "-289.46478271484375",
            "-29.885643005371094",
            "-2914.826904296875",
            "-2989.015869140625",
            "-3.1657474040985107",
            "-303.5613098144531",
            "-3064.407470703125",
            "-3141.00146484375",
            "-318.133544921875",
            "-3218.796142578125",
            "-3297.790283203125",
            "-33.76767349243164",
            "-333.1931457519531",
            "-3377.9814453125",
            "-3459.3662109375",
            "-348.751953125",
            "-3541.94189453125",
            "-3625.703857421875",
            "-364.82196044921875",
            "-37.85219192504883",
            "-3710.6474609375",
            "-3796.76806640625",
            "-381.4154357910156",
            "-3884.0595703125",
            "-3972.51611328125",
            "-398.5447082519531",
            "-4062.13037109375",
            "-4152.89599609375",
            "-416.2223205566406",
            "-42.14503860473633",
            "-434.4610595703125",
            "-453.2737731933594",
            "-46.6522102355957",
            "-472.6734924316406",
            "-492.6734619140625",
            "-5.464963436126709",
            "-51.379859924316406",
            "-513.2869873046875",
            "-534.527587890625",
            "-556.4088745117188",
            "-56.334285736083984",
            "-578.944580078125",
            "-602.1486206054688",
            "-61.52195739746094",
            "-626.034912109375",
            "-650.6175537109375",
            "-66.94949340820312",
            "-675.9107055664062",
            "-7.920377254486084",
            "-701.9286499023438",
            "-72.62368774414062",
            "-728.6856079101562",
            "-756.196044921875",
            "-78.55149841308594",
            "-784.4743041992188",
            "-813.5348510742188",
            "-84.74004364013672",
            "-843.3921508789062",
            "-874.0606689453125",
            "-905.5548095703125",
            "-91.1966323852539",
            "-937.8890991210938",
            "-97.92872619628906",
            "-971.077880859375",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-1.0182366371154785",
            "-10.536603927612305",
            "-1005.135498046875",
            "-104.94397735595703",
            "-1040.0762939453125",
            "-1075.914306640625",
            "-1112.6636962890625",
            "-112.25020599365234",
            "-1150.33837890625",
            "-1188.9521484375",
            "-119.85543060302734",
            "-1228.518798828125",
            "-1269.0517578125",
            "-127.76783752441406",
            "-13.318384170532227",
            "-1310.564208984375",
            "-135.9958038330078",
            "-1353.0693359375",
            "-1396.5799560546875",
            "-144.5478973388672",
            "-1441.108642578125",
            "-1486.6678466796875",
            "-153.43284606933594",
            "-1533.2694091796875",
            "-1580.9251708984375",
            "-16.270586013793945",
            "-162.6596221923828",
            "-1629.6466064453125",
            "-1679.44482421875",
            "-172.2373504638672",
            "-1730.330322265625",
            "-1782.3135986328125",
            "-182.17535400390625",
            "-1835.404541015625",
            "-1889.6126708984375",
            "-19.398210525512695",
            "-192.48313903808594",
            "-1944.9471435546875",
            "-2001.4166259765625",
            "-203.17044067382812",
            "-2059.029052734375",
            "-2117.79248046875",
            "-214.24716186523438",
            "-2177.714111328125",
            "-22.706392288208008",
            "-2238.80029296875",
            "-225.72340393066406",
            "-2301.0576171875",
            "-2364.49169921875",
            "-237.60946655273438",
            "-2429.107666015625",
            "-249.9158477783203",
            "-2494.91015625",
            "-2561.903076171875",
            "-26.20039939880371",
            "-262.6532287597656",
            "-2630.08984375",
            "-2699.4736328125",
            "-275.83251953125",
            "-2770.056640625",
            "-2841.8408203125",
            "-289.46478271484375",
            "-29.885643005371094",
            "-2914.826904296875",
            "-2989.015869140625",
            "-3.1657474040985107",
            "-303.5613098144531",
            "-3064.407470703125",
            "-3141.00146484375",
            "-318.133544921875",
            "-3218.796142578125",
            "-3297.790283203125",
            "-33.76767349243164",
            "-333.1931457519531",
            "-3377.9814453125",
            "-3459.3662109375",
            "-348.751953125",
            "-3541.94189453125",
            "-3625.703857421875",
            "-364.82196044921875",
            "-37.85219192504883",
            "-3710.6474609375",
            "-3796.76806640625",
            "-381.4154357910156",
            "-3884.0595703125",
            "-3972.51611328125",
            "-398.5447082519531",
            "-4062.13037109375",
            "-4152.89599609375",
            "-416.2223205566406",
            "-42.14503860473633",
            "-434.4610595703125",
            "-453.2737731933594",
            "-46.6522102355957",
            "-472.6734924316406",
            "-492.6734619140625",
            "-5.464963436126709",
            "-51.379859924316406",
            "-513.2869873046875",
            "-534.527587890625",
            "-556.4088745117188",
            "-56.334285736083984",
            "-578.944580078125",
            "-602.1486206054688",
            "-61.52195739746094",
            "-626.034912109375",
            "-650.6175537109375",
            "-66.94949340820312",
            "-675.9107055664062",
            "-7.920377254486084",
            "-701.9286499023438",
            "-72.62368774414062",
            "-728.6856079101562",
            "-756.196044921875",
            "-78.55149841308594",
            "-784.4743041992188",
            "-813.5348510742188",
            "-84.74004364013672",
            "-843.3921508789062",
            "-874.0606689453125",
            "-905.5548095703125",
            "-91.1966323852539",
            "-937.8890991210938",
            "-97.92872619628906",
            "-971.077880859375",
        ],
    )
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        maximum_depth=None,
        minimum_depth=None,
        end_datetime="2022-01-01T00:00:00Z",
        start_datetime="1999-01-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            maximum_depth=maximum_depth,
            minimum_depth=minimum_depth,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
