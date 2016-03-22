
reset
set title "Racial Demographics"
set term png truecolor
set output "race.png"
set xlabel "Year Demographics"
set ylabel "Number of Students"
set grid
set yrange [0:100]
set boxwidth 0.95 relative
set style fill transparent solid 0.5 noborder
set style data histogram 
set style histogram cluster
set key left top Left

plot "race.dat" using 2:xtic(1) lc rgb"red" title "Black", "race.dat" using 3 lc rgb"blue" title "Caucasian", "race.dat" using 4 lc rgb"green" title "Native American", "race.dat" using 5 lc rgb"orange" title "Asian", "race.dat" using 6 lc rgb"black" title "Hispanic", "race.dat" using 7 lc rgb"purple" title "Multiple Selection", "race.dat" using 8 lc rgb"brown" title "Undeclared"
