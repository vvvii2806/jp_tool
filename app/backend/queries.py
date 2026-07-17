import psycopg2
from . import connect
# Lacks inserting into kanji table, will be done when I learn kanji
def insert_word(meaning, hiragana=None, katakana=None, kanji=None, note=None):


    to_words = """INSERT INTO words(hiragana, katakana, kanji, note)
        VALUES (%s, %s, %s, %s) RETURNING wid;"""
    
    to_meanings = """INSERT INTO meanings(wid, meaning)
        VALUES (%s, %s) RETURNING mid;"""

    cur, conn = connect.create_cursor()
    try:

        cur.execute(to_words, (hiragana, katakana, kanji, note))

        rows = cur.fetchone()
        if rows:
            word_id = rows[0]

        cur.execute(to_meanings, (word_id, meaning, ))

        rows = cur.fetchone()
        if rows:
            meaning_id = rows[0]

        # commit the changes to the database
        conn.commit()

        return {'done': 'Ok', 'text': 'Word inserted'}, 201
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        return {'error': f'{error}'}, 500
    finally:
        connect.close_connection(cur, conn)    


# TODO: function to add kanji to existing words
def update_kanji(kanji=None):



    return
    
# To add the hiragana or katakana form of a word depending on which one is empty
# and which one is registered
def update_words(hiragana=None, katakana=None, kanji_form=None, note=None):
    add_kana = """UPDATE words
        SET
            hiragana = COALESCE(%s, hiragana),
            katakana = COALESCE(%s, katakana),
            kanji_form = COALESCE(%s, kanji_form),
            note = COALESCE(%s, note)
        WHERE (%s::text IS NOT NULL AND hiragana = %s)
            OR (%s::text IS NOT NULL AND katakana = %s)
            OR (%s::text IS NOT NULL AND kanji_form = %s)
        RETURNING wid;"""
    cur, conn = connect.create_cursor()
    try:

        cur.execute(add_kana, (
            hiragana, katakana, kanji_form, note,
            hiragana, hiragana,
            katakana, katakana,
            kanji_form, kanji_form
        ))
        
        row = cur.fetchone()
        if row:
            wid=row[0]
        conn.commit()

        return {'type': 'Ok', 'text': f'Modified word with id {wid}'}, 201

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
        conn.rollback()
        return {'type': 'Error', 'text': 'Something failed while registering the attempt'}, 500
    finally:
        connect.close_connection(cur, conn)  

def get_random():
    get_word = """SELECT M.meaning, W.hiragana, W.katakana, W.successes, W.failures
        FROM words W
        JOIN meanings M ON W.wid = M.wid
        ORDER BY RANDOM() LIMIT 1;"""
    
    cur, conn = connect.create_cursor()

    cur.execute(get_word)

    row = cur.fetchall()
    connect.print_rows(cur, row)
    return row, cur

# To keep track of successes/failures and then turn it into weighted chance maybe
def register_attempt(word_id, isSuccess=False, isFailure=False):
    register = """UPDATE words
        SET
            successes = 
            CASE
                WHEN (%s) = True THEN successes + 1
                ELSE successes
            END,
            failures = 
            CASE
                WHEN (%s) = True THEN failures + 1
                ELSE failures
            END
        WHERE words.wid = (%s);"""
    cur, conn = connect.create_cursor()

    try:
        cur.execute(register, (isSuccess, isFailure, word_id))

        conn.commit()

        return {'type': 'Ok', 'text': 'Attempt inserted'}, 200

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback
        return {'type': 'Error', 'text': 'Something failed while registering the attempt'}, 500

    finally:
        connect.close_connection(cur, conn)



# Testing the functions to see if they work like intended
if __name__ == '__main__':

    print(insert_word(hiragana="いぬ", meaning="dog", note="guauguau"))
    print(insert_word(katakana="ネコ", meaning="cat")) 
    print(insert_word(hiragana="だいがく", meaning="university"))
    print(insert_word(katakana="エイガ", meaning="movie"))

 
    print(update_words(hiragana="いぬ", katakana="イヌ"))
    print(update_words(hiragana="ねこ", katakana="ネコ"))

    register_attempt(2, isFailure=True)
    register_attempt(3, isSuccess=True)

    
    get_random()
    get_random()