from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, FollowEvent, TextSendMessage
)

import backend


def handler_function(input_message):
    output_message = backend.hoax(input_message)
    return output_message


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = 'ecc29561200057475cbdca1668d6b7da'
channel_access_token = 'F1VRU2c3omjPFzbW5rPqvVWkgGBhJf3ZDux8HNJIpYgdJAdZuzHpSm+gJjLndjpKyAQhPAf97JrSymWug97r2kji/jM2GIeCTC9iEf7LAhg8W6CyRHZMCtDLBD4s92hP7qJVnSO7HQKE7jVC1qrasgdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['x-line-signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent)
def check_message(event):
    if event.source.type == 'user':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=handler_function(event.message.text))
        )


@handler.add(FollowEvent)
def greeting_message(event):
    profile = line_bot_api.get_profile(event.user_id)
    text = 'Hi ' + profile.display_name + ', silakan diisi pake teks yang bagus'
    line_bot_api.push_message(event.user_id, TextSendMessage(text))


if __name__ == "__main__":
    app.run()
