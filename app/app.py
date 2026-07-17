from flask import Flask, request, jsonify
from backend import adapter

app = Flask(__name__)

@app.route("/api/getword", methods=['GET'])
def give_word():
    return adapter.get_word()

@app.route("/api/insert", methods=['POST'])
def add_word():
    data = request.get_json()

    meaning = data.get('meaning')
    hiragana = data.get('hiragana') 
    katakana = data.get('katakana')

    return adapter.add_word(meaning, hiragana, katakana)

@app.route("/api/attempt", methods=['PATCH'])
def attempt():
    data = request.get_json()

    wid = data.get('wid')
    succeeded = data.get('success')
    failed = data.get('fail')

    return adapter.register_answer(wid, succeeded, failed)
    

@app.route("/api/update", methods=['PATCH'])
def update():
    data = request.get_json()

    hiragana = data.get('hiragana')
    katakana = data.get('katakana')

    return adapter.add_kana(hiragana, katakana)