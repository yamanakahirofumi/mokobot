
from settings import SettingManager
from slackbot.bot import respond_to
import subprocess

import tweepy

# 各種キーをセット
settings = SettingManager()

CONSUMER_KEY = settings.properties['twitter']['CONSUMER_KEY']
CONSUMER_SECRET = settings.properties['twitter']['CONSUMER_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = settings.properties['twitter']['ACCESS_TOKEN']
ACCESS_SECRET = settings.properties['twitter']['ACCESS_SECRET']
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)


@respond_to('歌手一覧')
def cheer(message):
    stdout = subprocess.Popen("ls /mnt/m-st/music/", stdout=subprocess.PIPE,shell=True).communicate()[0]
    message.reply(stdout)


@respond_to('jenkins now')
def getjenkins(message):
    message.reply(api.user_timeline(id='jenkinsci',count=1)[0].text)
