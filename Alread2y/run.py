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
    instance.get(cat,art)
    return "", 200

@api.route("/<cat>/<art>", methods=['PUT'])
def put(cat,art):
    if not  request.is_json():
        return abort(404)
    body = request.get_json()
    instance.regist(cat, art, body.baseurl)

@api.route("/<cat>/<art>", methods=['GET'])
def count(cat,art):
    num = {"count" :instance.read(cat, art)}
    return jsonify(num)


def main():
    api.run(host=conf.properties['server']['host'],
     port=conf.properties['server']['port'])
    instance.run()
    instance.get('twitter','jenkinsci')

if __name__ == "__main__":
    main()

