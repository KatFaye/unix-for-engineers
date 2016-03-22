#!/bin/sh

cat demographics.csv | awk '
BEGIN {
FS=","
}

/[MFCOSBNTU]/ {
gender2013[$1]++;
race2013[$2]++;
gender2014[$3]++;
race2014[$4]++;
gender2015[$5]++;
race2015[$6]++;
gender2016[$7]++;
race2016[$8]++;
gender2017[$9]++;
race2017[$10]++;
gender2018[$11]++;
race2018[$12]++;
}
END {
	printf "\n2013\t"
	for ( x in gender2013 )
	if(x=="M" || x=="F")
	printf "%d\t ", gender2013[x]
	
	printf "\n2014\t"
	for ( x in gender2014 )
	if(x=="M" || x=="F")
	printf "%d\t ", gender2014[x]

	printf "\n2015\t"
	for ( x in gender2015 )
	if(x=="M" || x=="F")
	printf "%d\t ",gender2015[x]

	printf "\n2016\t"
	for ( x in gender2016 )
	if(x=="M" || x=="F")
	printf "%d\t ", gender2016[x]

	printf "\n2017\t"
	for ( x in gender2017 )
	if(x=="M" || x=="F")
	printf "%d\t ", gender2017[x]

	printf "\n2018\t"
	for ( x in gender2018 )
	if(x=="M" || x=="F")
	printf "%d\t ", gender2018[x]

	printf "\n# "
	for ( x in race2013 )
	if(x!="")
	printf "%s\t", x

	printf "\n2013\t"
	for ( x in race2013 )
	if(x!="")
	printf "%d\t", race2013[x]

	printf "\n2014\t"
	for ( x in race2014 )
	if(x!="")
	printf "%d\t", race2014[x]

	printf "\n2015\t"
	for ( x in race2015 )
	if(x!="")
	printf "%d\t", race2015[x]

	printf "\n2016\t"
	for ( x in race2016 )
	if(x!="")
	printf "%d\t", race2016[x]

	printf "\n2017\t"
	for ( x in race2017 )
	if(x!="")
	printf "%d\t", race2017[x]

	printf "\n2018\t"
	for ( x in race2018 )
	if(x!="")
	printf "%d\t", race2018[x]
} ' > demographics.dat

csplit demographics.dat 8
mv xx00 gender.dat
mv xx01 race.dat
