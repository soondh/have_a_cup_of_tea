from flask import Flask
from dingtalkchatbot.chatbot import DingtalkChatbot
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/drinktea')
def have_a_cup_of_tea():
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=574369d3260f369159e4643f7c9f4884ebd34b44d2b019d23d9066fc62c73dfc"
    secret = "SEC66b3d9a9e56ff0d0a9a4275681c4a576f2a0be61e9eb2a48633cc17410aa7185"

    caozhi = DingtalkChatbot(webhook,secret=secret)
    caozhi.send_text(msg='hello',is_at_all=False)



if __name__ == '__main__':
    app.run()
