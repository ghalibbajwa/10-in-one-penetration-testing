#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CMSeeK, check the LICENSE file for more information
# Copyright (c) 2018 - 2020 Tuhinshubhra

# Sitefinity version detection
# Rev 1

from apps.home.libs.CMSeeK.cmseekdb import basic as cmseek
import re

def start(ga_content):
    ga_content = ga_content.lower()
    regex = re.findall(r'sitefinity (.*)', ga_content)
    if regex != []:
        version = regex[0]
        cmseek.success('Sitefinity version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
        return version
    else:
        cmseek.error('Version detection failed!')
        return '0'
