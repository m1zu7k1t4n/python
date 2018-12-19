# coding: utf-8

from slackbot.bot import respond_to, listen_to, default_reply

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？
#
# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない

def_word = 'デフォルトの返事です'


@default_reply()
def default_func(message):
    message.reply(def_word)  # def_wordの文字列を返す


@respond_to(r'^set\s+\S.*')
def set_default_func(message):
    print(message.body)
    text = message.body['text']  # メッセージを取り出す
    temp, word = text.split(None, 1)  # 設定する言葉を取り出す。tempには'set'が入る
    global def_word  # 外で定義した変数の値を変えられるようにする
    def_word = word  # デフォルトの返事を上書きする
    msg = 'デフォルトの返事を以下のように変更しました。\n```' + word + '```'
    message.reply(msg)


@respond_to('メンション')
def mention_func(message):
    message.reply('私にメンションと言ってどうするのだ')  # メンション


@listen_to('リッスン')
def listen_func(message):
    message.send('誰かがリッスンと投稿したようだ')  # ただの投稿
    message.reply('君だね？')  # メンション


@respond_to('かっこいい')
def cool_func(message):
    message.reply('ありがとう。スタンプ押しとくね')  # メンション
    message.react('+1')  # リアクション
