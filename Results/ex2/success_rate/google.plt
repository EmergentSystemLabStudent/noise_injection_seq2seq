set terminal postscript eps enhanced
set output 'google.eps'
set key inside right
set xlabel 'noise level'
set ylabel 'success rate'
plot  "google" using 1:2 title 'speaker K' with lines lt 1, \
"google" using 1:3 title 'speaker L' with lines lt 2,\
"google" using 1:4 title 'speaker T' with lines lt 3,\
"google" using 1:5 title 'speaker W' with lines lt 4