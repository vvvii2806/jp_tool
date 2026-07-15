CREATE TABLE IF NOT EXISTS words (
    wid SERIAL PRIMARY KEY,
    hiragana varchar(100) DEFAULT NULL,
    katakana varchar(100) DEFAULT NULL,
    successes INTEGER DEFAULT 0,
    failures INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS meanings (
    mid SERIAL PRIMARY KEY,
    wid INTEGER NOT NULL,
    meaning varchar(100) NOT NULL,
    
    CONSTRAINT fk_word_meaning FOREIGN KEY (wid) REFERENCES words(wid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS kanji (
    kid SERIAL PRIMARY KEY,
    wid INTEGER NOT NULL,
    kanji varchar(100) NOT NULL,
    note TEXT,
    CONSTRAINT fk_kanji_word FOREIGN KEY (wid) REFERENCES words(wid) ON DELETE CASCADE

);

