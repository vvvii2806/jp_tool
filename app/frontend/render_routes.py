from flask import request, render_template, request, url_for
from backend import adapter
from random import randint

def render(app):

    @app.route("/api/getword", methods=['GET'])
    def give_word():
        return adapter.get_word()

    @app.route("/api/insert", methods=['POST'])
    def add_word():
        data = request.get_json()

        meaning = data.get('meaning')
        hiragana = data.get('hiragana') 
        katakana = data.get('katakana')
        kanji = data.get('kanji')
        note = data.get('note')

        return adapter.add_word(meaning, hiragana, katakana, kanji, note)

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
        kanji_form = data.get('kanji_form')
        note = data.get('note')

        return adapter.update_word(hiragana, katakana, kanji_form, note)
    
    @app.route("/")
    def test():
        data = adapter.get_word()
        
        hiragana = data[0]['hiragana']
        katakana = data[0]['katakana']
        kanji_form = data[0]['kanji_form']
        word_id = data[0]['wid']
        meaning = data[0]['meaning']
        note = data[0]['note']

        return render_template('index.html', hiragana=hiragana, katakana=katakana, kanji = kanji_form)
