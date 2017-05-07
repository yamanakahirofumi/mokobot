
# -*- coding: utf-8 -*-
from slackbot.bot import respond_to

import tweepy

# 各種キーをセット
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')
from settings import SettingManager

CONSUMER_KEY = settings.properties['twitter']['CONSUMER_KEY']
CONSUMER_SECRET = settings.properties['twitter']['CONSUMER_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = settings.properties['twitter']['ACCESS_TOKEN']
ACCESS_SECRET = settings.properties['twitter']['ACCESS_SECRET']
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)



@respond_to('未読')
def notRead(message):
    body = requests.get('http://localhost:3001/twitter/jenkinsci')
    result = json.loads(body.text)
    global unreadable_list
    unreadable_list = result['list']
    message.reply("未読件数は{}件".format(result['count']))

unreadable_list=[]

@respond_to('次')
def nextone(message):
    text='ないよ'
    if unreadable_list:
        res = requests.get('http://localhost:3000/tweet/jenkinsci/{}'.format(unreadable_list[-1]))
        text = json.loads(res.text, 'utf-8')['body']
        unreadable_list.pop()
    message.reply(text)


@respond_to('jenkins now')
def getjenkins(message):
    message.reply(api.user_timeline(id='jenkinsci',count=1)[0].text)
