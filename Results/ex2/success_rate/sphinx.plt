set terminal postscript eps enhanced
set output 'sphinx.eps'
set key inside right
set xlabel 'noise level'
set ylabel 'success rate'
plot  "sphinx" using 1:2 title 'speaker K' with lines lt 1, \
"sphinx" using 1:3 title 'speaker L' with lines lt 2,\
"sphinx" using 1:4 title 'speaker T' with lines lt 3,\
"sphinx" using 1:5 title 'speaker W' with lines lt 4