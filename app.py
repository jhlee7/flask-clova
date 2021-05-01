from flask import Flask
from flask_clova import Clova, statement, question, say

app = Flask(__name__)
# must set CLOVA_VERIFY_REQUESTS False
# while testing wihtout application_id
# app.config['CLOVA_VERIFY_REQUESTS'] = False

clova = Clova(app, '/user_defined')

@clova.intent('HelloIntent.Reprompt')
def hello_reprompt():
    speech = "혹시 더 이야기하고 싶으신 게 없으신가요? 저에게 말 걸어주세요."
    return question(say.Korean(speech)).reprompt(say.Korean("혹시 더 대화를 나누고 싶지 않으신가요? 저는 어떤 대화든 더 하고 싶어요."))

@clova.intent('HelloIntent.Hello')
def hello():
    speech = "안녕하세요"
    return statement(say.Korean(speech))

if __name__ == "__main__":
    app.config['CLOVA_VERIFY_REQUESTS'] = False
    app.run(port='5000', debug=True, host = '0.0.0.0')