# -*- coding: utf-8 -*-

from Scraping4twitter import Scraping4twitter

from flask import Flask, jsonify
api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False
instance = Scraping4twitter()

@api.route("/tweets/<twitter_id>")
def get_tweets(twitter_id):
    return jsonify(instance.get_tweets(twitter_id))

@api.route("/tweets/<twitter_id>", methods=['POST'])
def save_tweets(twitter_id):
    instance.run(twitter_id)
    return '',200


def main():
    api.run(host='0.0.0.0', port=3000)

if __name__ == "__main__":
    main()

