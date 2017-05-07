# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')
from settings import SettingManager

settings = SettingManager()

API_TOKEN = settings.properties['slack']['API_TOKEN']

default_reply = "スイマセン。其ノ言葉ワカリマセン"

PLUGINS = [
    'plugins',
]

del settings

