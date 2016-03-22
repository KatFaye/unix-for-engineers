all: homework06.pdf

homework06.pdf: gender.png race.png
	pdflatex homework06
	pdflatex homework06

gender.png: gender.plt demographics.dat
	gnuplot gender.plt

race.png: race.plt demographics.dat
	gnuplot race.plt

demographics.dat:
	./csedata.sh

clean:
	rm -f homework06.[!tex]* *.png *.dat
