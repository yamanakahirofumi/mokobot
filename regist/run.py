# -*- coding: utf-8 -*-

from regist import Regist
from settings import SettingManager

from flask import Flask, jsonify, request, abort
api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False

conf = SettingManager()

instance = Regist(conf)

@api.route("/info/twitter/<userid>", methods=['POST'])
def regist(userid):
    instance.regist(userid)
    return "", 200

@api.route("/info/twitter/", methods=['GET'])
def listup():
    resultList = instance.list()
    jsonlist = [ { "userid" : watch.name } for watch in resultList]
    return jsonify(jsonlist)


def main():
    api.run(host=conf.properties['server']['host'],
     port=conf.properties['server']['port'])

if __name__ == "__main__":
    main()

