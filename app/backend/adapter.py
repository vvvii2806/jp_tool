from . import queries

def _to_dicts(cursor, rows):
    cols = [i[0] for i in cursor.description]
    return [dict(zip(cols, row)) for row in rows]


def get_word():
    row, cursor = queries.get_random()
    if not row:
        return []
    return _to_dicts(cursor, row)

def add_word(meaning, hiragana=None, katakana=None, kanji=None):
    if not meaning:
        return {'type': 'Error', "text": "No meaning specified or emtpy request"}, 400
    
    res = queries.insert_word(meaning, hiragana=hiragana, katakana=katakana, kanji=kanji)

    if res is None:
        return {'type': 'Error', 'text': 'Unkown error while adding word'}, 500
    return res
    
def register_answer(word_id, succeed=False, fail=False):
    if not word_id:
        return {'type': 'Error', 'text': 'No word associated'}, 500
    elif not succeed and not fail:
        return {'type': 'Error', 'text': 'succeed and fail cannot be false at the same time'}, 400
    
    res = queries.register_attempt(word_id, succeed, fail)

    return res

def add_kana(hiragana, katakana):
    if not hiragana and not katakana:
        return {'type': 'Error', 'text': 'Empty kana'}, 400

    res = queries.update_words(hiragana, katakana)
    return res 

