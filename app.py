# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import time

app = Flask(__name__)

# 填入你的 message api 資訊
line_bot_api = LineBotApi('gi2NdIngaDaOHkfhfBWR8zLH2OAgaTWE2+2lE/cO9qe99Bu0ssQdn7cwb6fkyv/+oHMWYgLueyuymUi6O6uDVzF0RUt4Hzyem3b6BrqaPoPC1KPue96tK5cuOFa/egyOIB69ZWrdJ2cDxwQFon2h1wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d3a982e72a276216a43939540e247f34')
#line_bot_api = LineBotApi('YxTSr5T6yB1vNRmZNXGo5tqBMwgelhxFvjHdG9Ymi+fHREqFOtKpVeNEtYrX2I4uEd0z5rCpJuL3ei8hCXF9xCWzrg3Bw7oPzf4D+QzqJKazGEAIs9u7N50v1odKWUlNWtGCa9twFhm0rshrm6bqTAdB04t89/1O/w1cDnyilFU=')
#handler = WebhookHandler('3c698809cb17ebbe581aebe712c76baf')

# 設定你接收訊息的網址，如 https://YOURAPP.herokuapp.com/callback
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

	msg = event.message.text
	print(msg)
	#msg = msg.encode('utf-8')
	if msg=="dog":
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="汪汪叫"))
	if msg=="isom":
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="艾陞科技"))
	if msg=="cat":
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="喵喵叫"))
	if msg=="1":
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="求救警報"))		
	if msg=="2":
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="火災警報"))
	if msg=="3":
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="瓦斯警報"))
	if msg=="4":
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="紅外警報"))
	if msg=="5":
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="磁簧警報"))
	else:
		content = "{}: isom love {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), event.message.text)
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))

	
import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])