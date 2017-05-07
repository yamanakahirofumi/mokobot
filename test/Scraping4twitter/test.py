# -*- coding:utf-8

import unittest

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../Scraping4twitter')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../util')

from settings import SettingManager

from Scraping4twitter import Scraping4twitter

class TestScraping4twitter(unittest.TestCase):

    def test_init(self):
        app_yml = os.path.dirname(os.path.abspath(__file__)) + '/init_application.yml'
        conf = SettingManager(app_yml)
        instance = Scraping4twitter(conf)

        self.assertEqual(instance.api.auth.consumer_key,'_CONSUMER_KEY'.encode('ascii'))
        self.assertEqual(instance.api.auth.consumer_secret,'_CONSUMER_SECRET'.encode('ascii'))
        self.assertEqual(instance.api.auth.access_token,'_ACCESS_TOKEN')
        self.assertEqual(instance.api.auth.access_token_secret,'_ACCESS_SECRET')


if __name__ == '__main__':
    unittest.main()

