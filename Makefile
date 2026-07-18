data:
	sudo -u postgres psql -d jp_vocab

clean:
	python3 cleardb.py

test:
	python3 -m app.backend.queries
	
show:
	sudo -u postgres psql -d jp_vocab -c "SELECT * FROM words w JOIN meanings m ON w.wid = m.wid;"

all:
	python3 -m app.backend.queries
	python3 cleardb.py

run:
	python3 app/app.py 

restart:
	python3 cleardb.py
	python3 -m app.backend.queries
	flask --app app/app run --debug
