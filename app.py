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
line_bot_api = LineBotApi('YxTSr5T6yB1vNRmZNXGo5tqBMwgelhxFvjHdG9Ymi+fHREqFOtKpVeNEtYrX2I4uEd0z5rCpJuL3ei8hCXF9xCWzrg3Bw7oPzf4D+QzqJKazGEAIs9u7N50v1odKWUlNWtGCa9twFhm0rshrm6bqTAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3c698809cb17ebbe581aebe712c76baf')

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
	print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
	#content = "{}: isom love {}".format(event.source.user_id, event.message.text)
	#line_bot_api.reply_message(
		#event.reply_token,
		#TextSendMessage(text=content))
		
	content = "{}: isom love {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), event.message.text)		
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text=content))

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])