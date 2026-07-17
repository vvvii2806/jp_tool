from . import queries

def _to_dicts(cursor, rows):
    cols = [i[0] for i in cursor.description]
    return [dict(zip(cols, row)) for row in rows]


def get_word():
    word, res = queries.get_random()
    row = word[0]
    cursor = word[1]
    if not row:
        return []
    return _to_dicts(cursor, row)

def add_word(meaning, hiragana=None, katakana=None, kanji=None, note=None):
    # Error if request lacks necessary values to add word
    if not meaning or meaning == "" or (not hiragana and not katakana):
        return {"Error": "Empty meaning/request"}, 400
    
    res = queries.add_word(meaning, hiragana=hiragana, katakana=katakana, kanji=kanji, note=note)

    if not res[0]:
        return {'Error': f'{res[1]}'}, 500
    return {'Done': 'No errors'}, 201

    
def register_answer(word_id, succeed=False, fail=False):
    #Somehow gets no word ID
    if not word_id:
        return {'Error': 'Lacking wordID'}, 500
    elif not succeed and not fail:
        return {'Error': 'succeed and fail false at the same time'}, 400
    
    res = queries.register_attempt(word_id, succeed, fail)

    if not res[0]:
        return {'Error': f'{res[1]}'}, 500
    return {'Done': 'No errors'}, 201

def update_word(hiragana=None, katakana=None, kanji_form=None, note=None):
    if not hiragana and not katakana and not kanji_form and not note:
        return {'Error': 'No changes were given'}, 400

    res = queries.update_word(hiragana, katakana, kanji_form, note)
    if not res[0]:
        return {'Error': f'{res[1]}'}, 500
    return {'Done': 'No errors'}, 201

