
reset
set title "Male and Female Demographics"
set term png truecolor
set output "gender.png"
set xlabel "Year Demographics"
set ylabel "Number of Students"
set grid
set yrange [0:100]
set boxwidth 0.95 relative
set style fill transparent solid 0.5 noborder
set style data histogram 
set style histogram cluster

plot "gender.dat" using 3:xtic(1) lc rgb"red" title "Males", "gender.dat" using 2 lc rgb"blue" title "Females"
