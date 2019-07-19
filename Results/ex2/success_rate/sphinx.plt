set terminal postscript eps enhanced
set output 'sphinx.eps'
set key inside right
set xlabel 'noise level'
set ylabel 'success rate'
plot  "sphinx" using 1:2 title 'speaker K' with lines lw 1 dt 6, \
"sphinx" using 1:3 title 'speaker L' with lines lw 1 dt 3,\
"sphinx" using 1:4 title 'speaker T' with lines lw 1 dt 4,\
"sphinx" using 1:5 title 'speaker W' with lines lw 1 dt 5,\
"sphinx" using 1:($2+$3+$4+$5)/4 title 'average' with lines lw 5