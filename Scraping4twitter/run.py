# -*- coding: utf-8 -*-

from Scraping4twitter import Scraping4twitter

from flask import Flask, jsonify

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')

from settings import SettingManager

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False


@api.route('/tweets/<twitter_id>')
def get_tweets(twitter_id):
    return jsonify(instance.get_tweets(twitter_id))

@api.route('/tweet/<twitter_id>/<tweet_id>')
def get_tweet_one(twitter_id, tweet_id):
    result = instance.get_tweet_one(twitter_id, tweet_id)
    return jsonify(result)


@api.route('/tweets/<twitter_id>', methods=['POST'])
def save_tweets(twitter_id):
    instance.run(twitter_id)
    return '',200


def main():
    global instance
    conf = SettingManager()
    instance = Scraping4twitter(conf)
    api.run(host=conf.properties['server']['host'],
     port=conf.properties['server']['port'])

if __name__ == '__main__':
    main()

