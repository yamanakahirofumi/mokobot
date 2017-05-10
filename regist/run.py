# -*- coding: utf-8 -*-

from regist import Regist
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')
from settings import SettingManager

from flask import Flask, jsonify
api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False

instance = {}

@api.route("/info/twitter/<category>/<userid>", methods=['POST'])
def regist(category, userid):
    instance.regist(category, userid)
    return "", 200

@api.route("/info/twitter/<category>", methods=['GET'])
def listup(category):
    jsonlist = instance.listup(category)
    return jsonify(jsonlist)


def main():
    global instance
    conf = SettingManager()
    instance = Regist(conf)
    api.run(host=conf.properties['server']['host'],
     port=conf.properties['server']['port'])

if __name__ == "__main__":
    main()

