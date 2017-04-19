# -*- coding: utf-8 -*-

from settings import SettingManager

settings = SettingManager()

API_TOKEN = settings.properties['slack']['API_TOKEN']

default_reply = "スイマセン。其ノ言葉ワカリマセン"

PLUGINS = [
    'plugins',
]

del settings

