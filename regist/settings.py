# -*- coding: utf-8 -*-

import yaml

class SettingManager:
    properties={}

    def __init__(self):
        f = open("application.yml", "r+")
        self.properties = yaml.safe_load(f)
        f.close()

