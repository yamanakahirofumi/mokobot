# -*- coding: utf-8 -*-

import yaml

class SettingManager:

    def __init__(self,path='application.yml'):
        with open(path, "r+") as f:
            self.properties = yaml.safe_load(f)

