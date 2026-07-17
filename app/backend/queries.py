import psycopg2
from . import connect


# To get a random word from the database
def get_random():
    get_word = """SELECT w.wid, m.meaning, w.hiragana, w.katakana, w.kanji_form, w.note, w.successes, w.failures
        FROM words w
        JOIN meanings m ON w.wid = m.wid
        ORDER BY RANDOM() LIMIT 1;"""
    
    cur, conn = connect.create_cursor()

    cur.execute(get_word)

    row = cur.fetchall()
    connect.print_rows(cur, row)
    return (row, cur), (True, None)


# Lacks inserting into kanji table, will be done when I learn kanji
def add_word(meaning, hiragana=None, katakana=None, kanji=None, note=None):


    to_words = """INSERT INTO words(hiragana, katakana, kanji_form, note)
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

        connect.close_connection(cur, conn)    

        return True, None
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        return False, error


# To keep track of successes/failures and then turn it into weighted chance (maybe)
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
        cur.execute(register, (isSuccess, isFailure, word_id, ))

        conn.commit()
        connect.close_connection(cur, conn)

        return True, None

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        return False, error


# To add extra information for a certain word
def update_word(hiragana=None, katakana=None, kanji_form=None, note=None):

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

        connect.close_connection(cur, conn)  

        return True, None

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
        conn.rollback()
        return False, error


# TODO: function to add kanji, will be done later i think
def update_kanji(kanji=None):



    return


def check_duplicate(hiragana=None, katakana=None, kanji_form=None):
    search = """SELECT wid FROM words 
        WHERE (
            (%s::text IS NOT NULL AND hiragana = %s)
            OR (%s::text IS NOT NULL AND katakana = %s)
        )
        AND (%s::text IS NULL OR COALESCE(kanji_form, '') = %s);
    """
    pass

    cur, conn = connect.create_cursor()

    try:
        cur.execute(search, (hiragana, hiragana,
                katakana, katakana,
                kanji_form, kanji_form, ))
        exists = cur.fetchone() is not None

        connect.close_connection(cur, conn)

        return exists

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        return

# Testing the functions to see if they work like intended
if __name__ == '__main__':

    print(add_word(hiragana="いぬ", meaning="dog", note="guauguau"))
    print(add_word(katakana="ネコ", meaning="cat")) 
    print(add_word(katakana="エイガ", meaning="movie"))

 
    print(update_word(hiragana="いぬ", katakana="イヌ"))
    print(update_word(hiragana="ねこ", katakana="ネコ"))

    register_attempt(2, isFailure=True)
    register_attempt(3, isSuccess=True)

    
    get_random()
    get_random()