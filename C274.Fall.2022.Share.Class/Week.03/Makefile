all:
	python3 count.the.p4.v1.py < words.2
	python3 lec05.p02.count.the.p4.v1.py < words.2

pipe:
	cat words.2 | python3 split.line.p5.v1.py | python3 count.the.p4.v1.py

push:
	git commit -a
	git push

lec04:
	python3 lec04.p01.py
	python3 lec04.p02.py
