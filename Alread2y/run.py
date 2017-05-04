# -*- coding: utf-8 -*-

from Alread2y import Alread2y
from settings import SettingManager

from flask import Flask, jsonify, request, abort
api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False

conf = SettingManager()

instance = Alread2y(conf)

@api.route("/<cat>/<art>", methods=['POST'])
def checkArticle(cat,art):
    instance.update(cat,art)
    return "", 200

@api.route("/<cat>/<art>", methods=['PUT'])
def put(cat,art):
    if not request.is_json:
        return abort(404)
    body = request.get_json()
    instance.regist(cat, art, body['baseurl'])
    return "", 200

@api.route("/<cat>/<art>", methods=['GET'])
def list(cat,art):
    list = instance.get(cat, art)
    body = {"list" : list ,"count" : len(list)}
    return jsonify(body)


def main():
    api.run(host=conf.properties['server']['host'],
     port=conf.properties['server']['port'])
    instance.run()

if __name__ == "__main__":
    main()

