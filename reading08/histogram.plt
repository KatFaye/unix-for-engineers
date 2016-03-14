
reset
set term png truecolor
set output "results.png"
set xlabel "Number of Times Rolled"
set ylabel "Roll"
set grid
set yrange [0:200]
set boxwidth 0.95 relative
set style fill transparent solid 0.5 noborder
plot "results.dat" u 1:2 w boxes lc rgb"blue" notitle

