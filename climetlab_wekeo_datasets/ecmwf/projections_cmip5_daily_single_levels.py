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


class projections_cmip5_daily_single_levels(Main):
    name = "EO:ECMWF:DAT:PROJECTIONS_CMIP5_DAILY_SINGLE_LEVELS"
    dataset = "EO:ECMWF:DAT:PROJECTIONS_CMIP5_DAILY_SINGLE_LEVELS"

    choices = [
        "experiment",
        "model",
        "ensemble_member",
        "format_",
    ]

    string_selects = [
        "period",
        "variable",
    ]

    @normalize(
        "period",
        [
            "18500101-18501231",
            "18500101-18541231",
            "18500101-18591231",
            "18500101-18691231",
            "18500101-18741231",
            "18500101-18791231",
            "18500101-18841231",
            "18500101-18991231",
            "18500101-19491231",
            "18500101-20051231",
            "18500101-20121230",
            "18510101-18511231",
            "18520101-18521231",
            "18530101-18531231",
            "18540101-18541231",
            "18550101-18551231",
            "18550101-18591231",
            "18560101-18561231",
            "18570101-18571231",
            "18580101-18581231",
            "18590101-18591231",
            "18591201-18591230",
            "18591201-18641130",
            "18591201-18691130",
            "18591201-18841130",
            "18600101-18601231",
            "18600101-18641231",
            "18600101-18691230",
            "18600101-18691231",
            "18610101-18611231",
            "18610101-18651231",
            "18620101-18621231",
            "18630101-18631231",
            "18640101-18641231",
            "18641201-18691130",
            "18650101-18651231",
            "18650101-18691231",
            "18660101-18661231",
            "18660101-18701231",
            "18670101-18671231",
            "18680101-18681231",
            "18690101-18691231",
            "18691201-18741130",
            "18691201-18791130",
            "18700101-18701231",
            "18700101-18741231",
            "18700101-18791230",
            "18700101-18791231",
            "18700101-18891231",
            "18710101-18711231",
            "18710101-18751231",
            "18720101-18721231",
            "18730101-18731231",
            "18740101-18741231",
            "18741201-18791130",
            "18750101-18751231",
            "18750101-18791231",
            "18750101-18991231",
            "18760101-18761231",
            "18760101-18801231",
            "18770101-18771231",
            "18780101-18781231",
            "18790101-18791231",
            "18791201-18841130",
            "18791201-18891130",
            "18800101-18801231",
            "18800101-18841231",
            "18800101-18891230",
            "18800101-18891231",
            "18800101-19091231",
            "18800101-19091231",
            "18810101-18811231",
            "18810101-18851231",
            "18820101-18821231",
            "18830101-18831231",
            "18840101-18841231",
            "18841201-18891130",
            "18841201-19091130",
            "18850101-18851231",
            "18850101-18891231",
            "18850101-19191231",
            "18860101-18861231",
            "18860101-18901231",
            "18870101-18871231",
            "18880101-18881231",
            "18890101-18891231",
            "18891201-18941130",
            "18891201-18991130",
            "18900101-18901231",
            "18900101-18941231",
            "18900101-18991230",
            "18900101-18991231",
            "18900101-19091231",
            "18910101-18911231",
            "18910101-18951231",
            "18920101-18921231",
            "18930101-18931231",
            "18940101-18941231",
            "18941201-18991130",
            "18950101-18951231",
            "18950101-18991231",
            "18960101-18961231",
            "18960101-19001231",
            "18970101-18971231",
            "18980101-18981231",
            "18990101-18991231",
            "18991201-19041130",
            "18991201-19091130",
            "19000101-19001231",
            "19000101-19041231",
            "19000101-19091230",
            "19000101-19091231",
            "19000101-19241231",
            "19000101-19491231",
            "19010101-19011231",
            "19010101-19051231",
            "19020101-19021231",
            "19030101-19031231",
            "19040101-19041231",
            "19041201-19091130",
            "19050101-19051231",
            "19050101-19091231",
            "19060101-19061231",
            "19060101-19101231",
            "19070101-19071231",
            "19080101-19081231",
            "19090101-19091231",
            "19091201-19141130",
            "19091201-19191130",
            "19091201-19341130",
            "19100101-19101231",
            "19100101-19141231",
            "19100101-19191230",
            "19100101-19191231",
            "19100101-19291231",
            "19100101-19391231",
            "19100101-19391231",
            "19110101-19111231",
            "19110101-19151231",
            "19120101-19121231",
            "19130101-19131231",
            "19140101-19141231",
            "19141201-19191130",
            "19150101-19151231",
            "19150101-19191231",
            "19160101-19161231",
            "19160101-19201231",
            "19170101-19171231",
            "19180101-19181231",
            "19190101-19191231",
            "19191201-19241130",
            "19191201-19291130",
            "19200101-19201231",
            "19200101-19241231",
            "19200101-19291230",
            "19200101-19291231",
            "19200101-19541231",
            "19210101-19211231",
            "19210101-19251231",
            "19220101-19221231",
            "19230101-19231231",
            "19240101-19241231",
            "19241201-19291130",
            "19250101-19251231",
            "19250101-19291231",
            "19250101-19491231",
            "19260101-19261231",
            "19260101-19301231",
            "19270101-19271231",
            "19280101-19281231",
            "19290101-19291231",
            "19291201-19341130",
            "19291201-19391130",
            "19300101-19301231",
            "19300101-19341231",
            "19300101-19391230",
            "19300101-19391231",
            "19300101-19491231",
            "19310101-19311231",
            "19310101-19351231",
            "19320101-19321231",
            "19330101-19331231",
            "19340101-19341231",
            "19341201-19391130",
            "19341201-19591130",
            "19350101-19351231",
            "19350101-19391231",
            "19360101-19361231",
            "19360101-19401231",
            "19370101-19371231",
            "19380101-19381231",
            "19390101-19391231",
            "19391201-19441130",
            "19391201-19491130",
            "19400101-19401231",
            "19400101-19441231",
            "19400101-19491230",
            "19400101-19491231",
            "19400101-19691231",
            "19410101-19411231",
            "19410101-19451231",
            "19420101-19421231",
            "19430101-19431231",
            "19440101-19441231",
            "19441201-19491130",
            "19450101-19451231",
            "19450101-19491231",
            "19460101-19461231",
            "19460101-19501231",
            "19470101-19471231",
            "19480101-19481231",
            "19490101-19491231",
            "19491201-19541130",
            "19491201-19591130",
            "19500101-19501231",
            "19500101-19541231",
            "19500101-19591230",
            "19500101-19591231",
            "19500101-19691231",
            "19500101-19741231",
            "19500101-19791231",
            "19500101-19891231",
            "19500101-19991231",
            "19500101-19991231",
            "19500101-20051231",
            "19500102-19591231",
            "19500102-19891231",
            "19510101-19511231",
            "19510101-19551231",
            "19520101-19521231",
            "19530101-19531231",
            "19540101-19541231",
            "19541201-19591130",
            "19550101-19551231",
            "19550101-19591231",
            "19550101-19891231",
            "19560101-19561231",
            "19560101-19601231",
            "19570101-19571231",
            "19580101-19581231",
            "19590101-19591231",
            "19591201-19641130",
            "19591201-19691130",
            "19591201-19841130",
            "19600101-19601231",
            "19600101-19641231",
            "19600101-19691230",
            "19600101-19691231",
            "19610101-19611231",
            "19610101-19651231",
            "19610101-20051231",
            "19620101-19621231",
            "19630101-19631231",
            "19640101-19641231",
            "19641201-19691130",
            "19650101-19651231",
            "19650101-19691231",
            "19660101-19661231",
            "19660101-19701231",
            "19670101-19671231",
            "19680101-19681231",
            "19690101-19691231",
            "19691201-19741130",
            "19691201-19791130",
            "19700101-19701231",
            "19700101-19741231",
            "19700101-19791230",
            "19700101-19791231",
            "19700101-19891231",
            "19700101-19991231",
            "19700101-20081231",
            "19710101-19711231",
            "19710101-19751231",
            "19720101-19721231",
            "19730101-19731231",
            "19740101-19741231",
            "19741201-19791130",
            "19750101-19751231",
            "19750101-19791231",
            "19750101-19991231",
            "19750101-20051231",
            "19750101-20121231",
            "19760101-19761231",
            "19760101-19801231",
            "19770101-19771231",
            "19780101-19781231",
            "19780101-20021231",
            "19780401-19781231",
            "19780901-19781230",
            "19780901-20081130",
            "19790101-19791231",
            "19790101-19791231",
            "19790101-19831231",
            "19790101-19881230",
            "19790101-19881231",
            "19790101-19931231",
            "19790101-19981231",
            "19790101-20031231",
            "19790101-20051231",
            "19790101-20051231",
            "19790101-20081231",
            "19790101-20091231",
            "19790101-20101231",
            "19791201-19841130",
            "19791201-19891130",
            "19800101-19801231",
            "19800101-19801231",
            "19800101-19841231",
            "19800101-19891230",
            "19800101-19891231",
            "19800101-20051231",
            "19810101-19811231",
            "19810101-19811231",
            "19810101-19851231",
            "19820101-19821231",
            "19820101-19821231",
            "19830101-19831231",
            "19830101-19831231",
            "19840101-19841231",
            "19840101-19841231",
            "19840101-19881231",
            "19841201-19891130",
            "19841201-20051230",
            "19850101-19851231",
            "19850101-19851231",
            "19850101-19891231",
            "19860101-19861231",
            "19860101-19861231",
            "19860101-19901231",
            "19870101-19871231",
            "19870101-19871231",
            "19880101-19881231",
            "19880101-19881231",
            "19890101-19891231",
            "19890101-19891231",
            "19890101-19931231",
            "19890101-19981230",
            "19890101-19981231",
            "19891201-19941130",
            "19891201-19991130",
            "19900101-19901231",
            "19900101-19901231",
            "19900101-19941231",
            "19900101-19991230",
            "19900101-19991231",
            "19900101-20051231",
            "19910101-19911231",
            "19910101-19911231",
            "19910101-19951231",
            "19920101-19921231",
            "19920101-19921231",
            "19930101-19931231",
            "19930101-19931231",
            "19940101-19941231",
            "19940101-19941231",
            "19940101-19981231",
            "19940101-20081231",
            "19941201-19991130",
            "19950101-19951231",
            "19950101-19951231",
            "19950101-19991231",
            "19960101-19961231",
            "19960101-19961231",
            "19960101-20001231",
            "19970101-19971231",
            "19970101-19971231",
            "19980101-19981231",
            "19980101-19981231",
            "19990101-19991231",
            "19990101-19991231",
            "19990101-20031231",
            "19990101-20081230",
            "19990101-20081231",
            "19990101-20091231",
            "19991201-20041130",
            "19991201-20051130",
            "19991201-20051230",
            "20000101-20001231",
            "20000101-20001231",
            "20000101-20041231",
            "20000101-20051230",
            "20000101-20051231",
            "20000101-20091130",
            "20000101-20091231",
            "20000101-20091231",
            "20000101-20101231",
            "20000101-20121230",
            "20000101-20121231",
            "20010101-20011231",
            "20010101-20011231",
            "20010101-20051231",
            "20020101-20021231",
            "20020101-20021231",
            "20030101-20031231",
            "20030101-20031231",
            "20030101-20081231",
            "20040101-20041231",
            "20040101-20041231",
            "20040101-20081231",
            "20041201-20051130",
            "20041201-20051230",
            "20050101-20051231",
            "20050101-20051231",
            "20050101-20091231",
            "20051201-20101130",
            "20051201-20111130",
            "20051201-20151130",
            "20060101-20061231",
            "20060101-20061231",
            "20060101-20061231",
            "20060101-20081231",
            "20060101-20091231",
            "20060101-20101231",
            "20060101-20151231",
            "20060101-20251231",
            "20060101-20301230",
            "20060101-20301231",
            "20060101-20351231",
            "20060101-20401231",
            "20060101-20551231",
            "20060101-20991230",
            "20060101-20991231",
            "20060101-21001231",
            "20060101-22051231",
            "20070101-20071231",
            "20070101-20071231",
            "20070101-20071231",
            "20080101-20081231",
            "20080101-20081231",
            "20080101-20081231",
            "20090101-20091130",
            "20090101-20091231",
            "20090101-20091231",
            "20100101-20101231",
            "20100101-20191231",
            "20101201-20151130",
            "20110101-20111231",
            "20110101-20151231",
            "20111201-20211130",
            "20120101-20121231",
            "20130101-20131231",
            "20140101-20141231",
            "20150101-20151231",
            "20151201-20201130",
            "20151201-20251130",
            "20160101-20161231",
            "20160101-20201231",
            "20160101-20251231",
            "20170101-20171231",
            "20180101-20181231",
            "20190101-20191231",
            "20200101-20201231",
            "20200101-20291231",
            "20201201-20251130",
            "20210101-20211231",
            "20210101-20251231",
            "20211201-20311130",
            "20220101-20221231",
            "20230101-20231231",
            "20240101-20241231",
            "20250101-20251231",
            "20251201-20301130",
            "20251201-20351130",
            "20260101-20261231",
            "20260101-20301231",
            "20260101-20351231",
            "20260101-20451231",
            "20260101-20501231",
            "20270101-20271231",
            "20280101-20281231",
            "20290101-20291231",
            "20300101-20301231",
            "20300101-20391231",
            "20301201-20351130",
            "20310101-20311231",
            "20310101-20351230",
            "20310101-20351231",
            "20310101-20551231",
            "20310101-20601231",
            "20311201-20411130",
            "20320101-20321231",
            "20330101-20331231",
            "20340101-20341231",
            "20350101-20351231",
            "20351201-20401130",
            "20351201-20451130",
            "20360101-20361231",
            "20360101-20401231",
            "20360101-20451231",
            "20370101-20371231",
            "20380101-20381231",
            "20390101-20391231",
            "20400101-20401231",
            "20400101-20491231",
            "20401201-20451130",
            "20410101-20411231",
            "20410101-20451231",
            "20410101-20701231",
            "20410101-20751231",
            "20411201-20511130",
            "20420101-20421231",
            "20430101-20431231",
            "20440101-20441231",
            "20450101-20451231",
            "20451201-20501130",
            "20451201-20551130",
            "20460101-20461231",
            "20460101-20501231",
            "20460101-20551231",
            "20460101-20651231",
            "20470101-20471231",
            "20480101-20481231",
            "20490101-20491231",
            "20500101-20501231",
            "20500101-20591231",
            "20501201-20551130",
            "20510101-20511231",
            "20510101-20551231",
            "20510101-20751231",
            "20511201-20611130",
            "20520101-20520731",
            "20520101-20521231",
            "20530101-20531130",
            "20530101-20531231",
            "20540101-20540630",
            "20540101-20541231",
            "20550101-20550731",
            "20550101-20551231",
            "20551201-20601130",
            "20551201-20651130",
            "20560101-20561231",
            "20560101-20601231",
            "20560101-20651231",
            "20560101-20801231",
            "20560101-21001231",
            "20570101-20571231",
            "20580101-20581231",
            "20590101-20591231",
            "20600101-20601231",
            "20600101-20691231",
            "20601201-20651130",
            "20610101-20611231",
            "20610101-20651231",
            "20610101-20901231",
            "20611201-20711130",
            "20620101-20621231",
            "20630101-20631231",
            "20640101-20641231",
            "20650101-20651231",
            "20651201-20701130",
            "20651201-20751130",
            "20660101-20661231",
            "20660101-20701231",
            "20660101-20751231",
            "20660101-20851231",
            "20670101-20671231",
            "20680101-20681231",
            "20690101-20691231",
            "20700101-20701231",
            "20700101-20791231",
            "20701201-20751130",
            "20710101-20711231",
            "20710101-20751231",
            "20710101-21001231",
            "20711201-20811130",
            "20720101-20721231",
            "20730101-20731231",
            "20740101-20741231",
            "20750101-20751231",
            "20751201-20801130",
            "20751201-20851130",
            "20760101-20761231",
            "20760101-20801231",
            "20760101-20851231",
            "20760101-21001231",
            "20770101-20771231",
            "20780101-20781231",
            "20790101-20791231",
            "20800101-20801231",
            "20800101-20891231",
            "20801201-20851130",
            "20810101-20811231",
            "20810101-20851231",
            "20810101-20991231",
            "20810101-21001230",
            "20810101-21001231",
            "20811201-20911130",
            "20820101-20821231",
            "20830101-20831231",
            "20840101-20841231",
            "20850101-20851231",
            "20851201-20901130",
            "20851201-20951130",
            "20860101-20861231",
            "20860101-20901231",
            "20860101-20951231",
            "20860101-21001231",
            "20870101-20871231",
            "20880101-20881231",
            "20890101-20891231",
            "20900101-20901231",
            "20900101-20991231",
            "20900101-21001231",
            "20901201-20951130",
            "20910101-20911231",
            "20910101-20951231",
            "20910101-21001231",
            "20911201-20991230",
            "20920101-20921231",
            "20930101-20931231",
            "20940101-20941231",
            "20950101-20951231",
            "20951201-20991030",
            "20951201-20991130",
            "20951201-20991230",
            "20951201-21001130",
            "20951201-21001230",
            "20960101-20961231",
            "20960101-21001231",
            "20970101-20971231",
            "20980101-20981231",
            "20990101-20990228",
            "20990101-20991231",
            "20991101-20991230",
            "20991201-20991230",
            "20991201-21091130",
            "21000101-21001230",
            "21000101-21001231",
            "21000101-21991231",
            "21001201-21001230",
            "21010101-21011231",
            "21010101-21091231",
            "21010101-21201231",
            "21010101-21241231",
            "21010101-21501231",
            "21010101-23001231",
            "21020101-21021231",
            "21030101-21031231",
            "21040101-21041231",
            "21050101-21051231",
            "21060101-21061231",
            "21070101-21071231",
            "21080101-21081231",
            "21090101-21091231",
            "21091201-21191130",
            "21100101-21101231",
            "21100101-21191231",
            "21110101-21111231",
            "21120101-21121231",
            "21130101-21131231",
            "21140101-21141231",
            "21150101-21151231",
            "21160101-21161231",
            "21170101-21171231",
            "21180101-21181231",
            "21190101-21191231",
            "21191201-21291130",
            "21200101-21201231",
            "21200101-21291231",
            "21210101-21211231",
            "21210101-21401231",
            "21220101-21221231",
            "21230101-21231231",
            "21240101-21241231",
            "21250101-21251231",
            "21250101-21491231",
            "21260101-21261231",
            "21270101-21271231",
            "21280101-21281231",
            "21290101-21291231",
            "21291201-21391130",
            "21300101-21301231",
            "21300101-21391231",
            "21310101-21311231",
            "21320101-21321231",
            "21330101-21331231",
            "21340101-21341231",
            "21350101-21351231",
            "21360101-21361231",
            "21370101-21371231",
            "21380101-21381231",
            "21390101-21391231",
            "21391201-21491130",
            "21400101-21400105",
            "21400101-21491231",
            "21410101-21601231",
            "21491201-21591130",
            "21500101-21591231",
            "21500101-21741231",
            "21510101-22001231",
            "21591201-21691130",
            "21600101-21691231",
            "21610101-21801231",
            "21691201-21791130",
            "21700101-21801231",
            "21750101-21991231",
            "21791201-21891130",
            "21810101-21811231",
            "21810101-21891231",
            "21810101-22001231",
            "21820101-21821231",
            "21830101-21831231",
            "21840101-21841231",
            "21850101-21851231",
            "21860101-21861231",
            "21870101-21871231",
            "21880101-21881231",
            "21890101-21891231",
            "21891201-21991130",
            "21900101-21901231",
            "21900101-22001231",
            "21910101-21911231",
            "21920101-21921231",
            "21930101-21931231",
            "21940101-21941231",
            "21950101-21951231",
            "21960101-21961231",
            "21970101-21971231",
            "21980101-21981231",
            "21990101-21991231",
            "21991201-22091130",
            "22000101-22001231",
            "22000101-22241231",
            "22000101-23001231",
            "22010101-22011231",
            "22010101-22091231",
            "22010101-22201231",
            "22010101-22501231",
            "22020101-22021231",
            "22030101-22031231",
            "22060101-23001231",
            "22091201-22191130",
            "22100101-22191231",
            "22191201-22291130",
            "22200101-22291231",
            "22210101-22401231",
            "22250101-22491231",
            "22291201-22391130",
            "22300101-22391231",
            "22391201-22491130",
            "22400101-22491231",
            "22410101-22601231",
            "22491201-22591130",
            "22500101-22591231",
            "22500101-22741231",
            "22510101-23001231",
            "22591201-22691130",
            "22600101-22691231",
            "22610101-22801231",
            "22691201-22791130",
            "22700101-22801231",
            "22750101-22991231",
            "22750101-23001231",
            "22791201-22891130",
            "22810101-22891231",
            "22810101-23001231",
            "22891201-22991130",
            "22900101-23001231",
            "22991201-22991230",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "10m_wind_speed",
            "2m_temperature",
            "daily_near_surface_relative_humidity",
            "maximum_2m_temperature_in_the_last_24_hours",
            "mean_precipitation_flux",
            "mean_sea_level_pressure",
            "minimum_2m_temperature_in_the_last_24_hours",
            "near_surface_specific_humidity",
            "snowfall",
            "surface_solar_radiation_downwards",
        ],
        multiple=True,
    )
    @normalize(
        "experiment",
        [
            "amip",
            "historical",
            "rcp_2_6",
            "rcp_4_5",
            "rcp_6_0",
            "rcp_8_5",
        ],
    )
    @normalize(
        "model",
        [
            "access1_0",
            "access1_3",
            "bcc_csm1_1",
            "bcc_csm1_1_m",
            "bnu_esm",
            "canam4",
            "cancm4",
            "canesm2",
            "ccsm4",
            "cesm1_bgc",
            "cesm1_cam5",
            "cmcc_cesm",
            "cmcc_cm",
            "cmcc_cms",
            "cnrm_cm5",
            "csiro_mk3_6_0",
            "ec_earth",
            "fgoals_g2",
            "fgoals_s2",
            "gfdl_cm3",
            "gfdl_esm2g",
            "gfdl_esm2m",
            "gfdl_hiram_c180",
            "gfdl_hiram_c360",
            "giss_e2_h",
            "giss_e2_r",
            "hadcm3",
            "hadgem2_a",
            "hadgem2_cc",
            "hadgem2_es",
            "inmcm4",
            "ipsl_cm5a_lr",
            "ipsl_cm5a_mr",
            "ipsl_cm5b_lr",
            "mpi_esm_lr",
            "mpi_esm_mr",
            "mpi_esm_p",
            "noresm1_m",
        ],
    )
    @normalize(
        "ensemble_member",
        [
            "r10i1p1",
            "r11i1p1",
            "r12i1p1",
            "r13i1p1",
            "r14i1p1",
            "r1i1p1",
            "r1i1p2",
            "r1i2p1",
            "r1i2p2",
            "r2i1p1",
            "r2i3p1",
            "r3i1p1",
            "r3i2p1",
            "r4i1p1",
            "r4i3p1",
            "r5i1p1",
            "r5i3p1",
            "r6i1p1",
            "r6i1p2",
            "r6i1p3",
            "r7i1p1",
            "r8i1p1",
            "r9i1p1",
        ],
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
        period,
        variable,
        experiment,
        model,
        ensemble_member,
        format_,
    ):
        super().__init__(
            period=period,
            variable=variable,
            experiment=experiment,
            model=model,
            ensemble_member=ensemble_member,
            format_=format_,
        )
