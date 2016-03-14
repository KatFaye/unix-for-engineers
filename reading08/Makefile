all: reading08.pdf

reading08.pdf: results.png
	pdflatex reading08
	pdflatex reading08

results.png: results.dat
	gnuplot histogram.plt

clean:
	rm -f reading08.[!tex]* results.png
