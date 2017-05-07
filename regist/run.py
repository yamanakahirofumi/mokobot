# -*- coding: utf-8 -*-

from regist import Regist
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')
from settings import SettingManager

from flask import Flask, jsonify
api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False

instance = {}

@api.route("/info/twitter/<userid>", methods=['POST'])
def regist(userid):
    instance.regist(userid)
    return "", 200

@api.route("/info/twitter/", methods=['GET'])
def listup():
    resultList = instance.listup()
    jsonlist = [ { "userid" : watch.name } for watch in resultList]
    return jsonify(jsonlist)


def main():
    global instance
    conf = SettingManager()
    instance = Regist(conf)
    api.run(host=conf.properties['server']['host'],
     port=conf.properties['server']['port'])

if __name__ == "__main__":
    main()

