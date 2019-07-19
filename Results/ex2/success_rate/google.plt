set terminal postscript eps enhanced
set output 'google.eps'
set key inside right
set xlabel 'noise level'
set ylabel 'success rate'
plot  "google" using 1:2 title 'speaker K' with lines lw 1 dt 6, \
"google" using 1:3 title 'speaker L' with lines lw 1 dt 3,\
"google" using 1:4 title 'speaker T' with lines lw 1 dt 4,\
"google" using 1:5 title 'speaker W' with lines lw 1 dt 5,\
"google" using 1:($2+$3+$4+$5)/4 title 'average' with lines lw 5