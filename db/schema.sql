-- Main table for vocabulary
CREATE TABLE IF NOT EXISTS words (
    wid SERIAL PRIMARY KEY,
    hiragana VARCHAR(100) DEFAULT NULL,
    katakana VARCHAR(100) DEFAULT NULL,
    kanji_form VARCHAR(100) DEFAULT NULL,
    note TEXT, -- optional any detail
    successes INTEGER DEFAULT 0,
    failures INTEGER DEFAULT 0
);

-- Table for each meaning a word can have 
CREATE TABLE IF NOT EXISTS meanings (
    mid SERIAL PRIMARY KEY,
    wid INTEGER NOT NULL,
    meaning VARCHAR(100) NOT NULL,
    CONSTRAINT fk_word_meaning FOREIGN KEY (wid) REFERENCES words(wid) ON DELETE CASCADE
);

-- Table for individual kanji
CREATE TABLE IF NOT EXISTS kanji (
    kid SERIAL PRIMARY KEY,
    character VARCHAR(10) UNIQUE NOT NULL,
    meaning VARCHAR(100) NOT NULL,         -- Different from meanings table, meant to be for the specific character
    onyomi VARCHAR(100),                   
    kunyomi VARCHAR(100),                  
    note TEXT                              
);

-- Bridge between words and kanji to show individual parts of words
CREATE TABLE IF NOT EXISTS word_kanji (
    wid INTEGER NOT NULL,
    kid INTEGER NOT NULL,
    PRIMARY KEY (wid, kid),
    CONSTRAINT fk_wk_word FOREIGN KEY (wid) REFERENCES words(wid) ON DELETE CASCADE,
    CONSTRAINT fk_wk_kanji FOREIGN KEY (kid) REFERENCES kanji(kid) ON DELETE CASCADE
);
