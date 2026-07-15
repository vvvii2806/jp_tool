import psycopg2
import connect


def insert_word(meaning, hiragana=None, katakana=None, kanji=None):


    to_words = """INSERT INTO words(hiragana, katakana)
        VALUES (%s, %s) RETURNING wid;"""
    
    to_meanings = """INSERT INTO meanings(wid, meaning)
        VALUES (%s, %s) RETURNING mid;"""

    try:
        cur, conn = connect.create_cursor()

        cur.execute(to_words, (hiragana, katakana, ))

        rows = cur.fetchone()
        if rows:
            word_id = rows[0]

        cur.execute(to_meanings, (word_id, meaning, ))

        rows = cur.fetchone()
        if rows:
            meaning_id = rows[0]

        # commit the changes to the database
        conn.commit()
        connect.close_env(cur, conn)

        return word_id, meaning_id
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    

def update_words(hiragana=None, katakana=None):
    do_update = """UPDATE words
        SET
            hiragana = COALESCE(%s, hiragana),
            katakana = COALESCE(%s, katakana)
        WHERE (%s::text IS NOT NULL AND hiragana = %s)
            OR (%s::text IS NOT NULL AND katakana = %s)
        RETURNING wid;"""
    try:
        cur, conn = connect.create_cursor()

        cur.execute(do_update, (
            hiragana, katakana,
            hiragana, hiragana,
            katakana, katakana
        ))
        
        row = cur.fetchone()
        if row:
            wid=row[0]
        conn.commit()
        connect.close_env(cur, conn)

        return wid

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 




if __name__ == '__main__':

    print(insert_word(hiragana="いぬ", meaning="dog"))
    print(insert_word(katakana="ネコ", meaning="cat"))


    print(update_words(hiragana="いぬ", katakana="イヌ"))
    print(update_words(hiragana="ねこ", katakana="ネコ"))
