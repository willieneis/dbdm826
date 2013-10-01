#MOVIEDB = /afs/andrew.cmu.edu/usr22/seunghak/15826/movies.db
#We will use our full data above for our grading (it is not publicly available)
#Change this test db file to your movie db file
#MOVIEDB = movies-mini.db 
MOVIEDB = movies-short.db

#Change this source to your movie data source
#SRC = movies-mini.csv
SRC = movies-short.csv

all: hw1.q1.3 hw1.q1.4 hw1.q1.5 hw1.q1.6 hw1.q1.7 hw1.q1.8 hw1.q1.9

linenum: $(SRC)
	wc -l $(SRC)

hw1.q1.3:
	sqlite3 $(MOVIEDB) < hw1.q1.3.txt

hw1.q1.4: 
	sqlite3 $(MOVIEDB) < hw1.q1.4.txt

hw1.q1.5: 
	sqlite3 $(MOVIEDB) < hw1.q1.5.txt

hw1.q1.6: 
	sqlite3 $(MOVIEDB) < hw1.q1.6.txt

hw1.q1.7: 
	sqlite3 $(MOVIEDB) < hw1.q1.7.txt
	time sqlite3 $(MOVIEDB) < hw1.q1.7.txt

hw1.q1.8:
	sqlite3 $(MOVIEDB) < hw1.q1.8.txt
	time sqlite3 $(MOVIEDB) < hw1.q1.7.txt

hw1.q1.9:
	sqlite3 $(MOVIEDB) < hw1.q1.9.txt

clean:
	\rm -f *.o
