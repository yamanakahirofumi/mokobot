# -*- coding: utf-8 -*-

from Alread2y import Alread2y
from flask import Flask, jsonify, request, abort

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')
from settings import SettingManager

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False

instance = {}

@api.route("/<cat>/<art>", methods=['PUT'])
def checkArticle(cat,art):
    instance.update(cat,art)
    return "", 200

@api.route("/<cat>/<art>", methods=['POST'])0
def regist(cat,art):
    if not request.is_json:
        return abort(404)
    body = request.get_json()
    instance.regist(cat, art, body['baseurl'])
    return "", 200

@api.route("/<cat>/<art>", methods=['GET'])
def listup(cat,art):
    resultlist = instance.get(cat, art)
    body = {"list" : resultlist ,"count" : len(resultlist)}
    return jsonify(body)


def main():
    global instance
    conf = SettingManager()
    instance = Alread2y(conf)
    api.run(host=conf.properties['server']['host'],
     port=conf.properties['server']['port'])

if __name__ == "__main__":
    main()

