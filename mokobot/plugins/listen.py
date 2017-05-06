from slackbot.bot import respond_to

class Respond:
    @respond_to('歌手一覧')
    def cheer(message):
        stdout = 'todo'
        message.reply(stdout)

