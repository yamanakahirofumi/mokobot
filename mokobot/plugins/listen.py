from slackbot.bot import respond_to
import subprocess


class Respond:
    @respond_to('歌手一覧')
    def cheer(message):
        stdout = subprocess.Popen("ls /mnt/m-st/music/", stdout=subprocess.PIPE,shell=True).communicate()[0]
        message.reply(stdout)

