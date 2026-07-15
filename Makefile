data:
	sudo -u postgres psql -d jp_vocab

clean:
	python3 cleardb.py

test:
	python3 app/backend/db.py
	
show:
	sudo -u postgres psql -d jp_vocab -c "SELECT * FROM words JOIN meanings ON words.wid = meanings.wid;"