#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CMSeeK, check the LICENSE file for more information
# Copyright (c) 2018 - 2020 Tuhinshubhra

def start(id, url, ua, ga, source, ga_content,test_id, detection_method='', headers=''):
    if id == "wp":
        # for now this is the only cms... but not for long!
        from apps.home.libs.CMSeeK.deepscans.wp import init as wpscan
  
        wpscan.start(id, url, ua, ga, source, detection_method,test_id)
    if id == 'joom':
        # told ya... not for long
        from apps.home.libs.CMSeeK.deepscans.joom import init as joomscan
    
        joomscan.start(id, url, ua, ga, source)
    if id == 'umbraco':
        # umm... whatever
        from apps.home.libs.CMSeeK.deepscans.umbraco import init as umbracoscan
        umbracoscan.start(id, url, ua, ga, source, detection_method, headers,test_id)
