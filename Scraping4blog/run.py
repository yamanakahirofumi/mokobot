# -*- coding: utf-8 -*-

from Scraping4blog import Scraping4blog

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')
from settings import SettingManager

def main():
    conf = SettingManager()
    instance = Scraping4blog(conf)
    instance.run()

if __name__ == "__main__":
    main()
