load 'projects/sppifo/plots/spectral.pal'
midnight = "#D53E4F"; aqua = "#F46D43"; ocean = "#FDAE61"; wave = "#66C2A5"; stone = "#ABDDA4"; foam = "#3288BD"
set terminal pdfcairo
set term pdfcairo enhanced font "Helvetica,16" size 4in,2.5in

########################################################################################################################
# Mean flow completion time: pFabric-based scheduling schemes
########################################################################################################################
set output 'projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_less_100KB_99th_fct_ms.pdf'

set xlabel 'Load'
set xrange [0:6]
set xtics ("0.2" 0, "0.3" 1, "0.4" 2, "0.5" 3, "0.6" 4, "0.7" 5, "0.8" 6)

set ylabel 'Flow Completion Time (ms)'
set yrange [0:50]
set key opaque
plot "projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_less_100KB_99th_fct_ms.dat" using 4 title "PIFO" w lp  ls 21 lw 4, \
            '' using 5 title "SP-PIFO"  w lp ls 23 lw 4, \
            '' using 3 title "DCTCP" w lp ls 27 lw 4, \
            '' using 2 title "TCP"  w lp ls 28 lw 4, \
            '' using 6 title "XIFO" w lp ls 29 lw 4

########################################################################################################################
# Mean flow completion time <100KB: pFabric-based scheduling schemes
########################################################################################################################
set output 'projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_less_100KB_mean_fct_ms.pdf'

set xlabel 'Load'
set ylabel 'Flow Completion Time (ms)'
set yrange [0:10]
set ytics 2
set key opaque
plot "projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_less_100KB_mean_fct_ms.dat" using 4 title "PIFO" w lp  ls 21 lw 4, \
            '' using 5 title "SP-PIFO"  w lp ls 23 lw 4, \
            '' using 3 title "DCTCP" w lp ls 27 lw 4, \
            '' using 2 title "TCP"  w lp ls 28 lw 4, \
            '' using 6 title "XIFO" w lp ls 29 lw 4

########################################################################################################################
# Mean flow completion time >10MB: pFabric-based scheduling schemes
########################################################################################################################
set output 'projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_geq_1MB_mean_fct_ms.pdf'

set xlabel 'Load'
set ylabel 'Flow Completion Time (ms)'
set yrange [0:500]
set ytics auto
set key opaque
plot "projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_geq_1MB_mean_fct_ms.dat" using 4 title "PIFO" w lp  ls 21 lw 4, \
            '' using 5 title "SP-PIFO"  w lp ls 23 lw 4, \
            '' using 3 title "DCTCP" w lp ls 27 lw 4, \
            '' using 2 title "TCP"  w lp ls 28 lw 4, \
            '' using 6 title "XIFO" w lp ls 29 lw 4


############################################################################################################################
# Mean Flow completion time per service: pFabric-based scheduling schemes
############################################################################################################################
set output 'projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_perSevice_mean_fct_ms.pdf'

set xlabel 'Service'
set ylabel 'Flow Completion Time (ms)'
set yrange [0:75000]
set boxwidth 0.7
set style data histogram
set style fill solid 0.6
set bars front
set key top center horizontal samplen 1.5 spacing 0.8
midnight = "#191970"

# Update xtics to match the 12 services in your data
set xtics ("CS" 0, "DF" 1, "EW" 2, "GH" 3, "MI" 4, "QW" 5, "RF" 6, "RT" 7, "SN" 8, "TV" 9, "YT" 10, "YU" 11)

# Update xrange to include all 12 data points
set xrange [-0.5:11.5]

plot "projects/sppifo/plots/sppifo_evaluation/pFabric/data_mining_workload/pFabric_service_based_fct_ms.dat" using 2:xtic(1) title "TCP" linecolor rgb midnight lw 4, \
     '' using 3 title "DCTCP" linecolor rgb "#F46D43" lw 4, \
     '' using 4 title "PIFO" linecolor rgb "#FDAE61" lw 4, \
     '' using 5 title "SP-PIFO" linecolor rgb "#66C2A5" lw 4, \
     '' using 6 title "XIFO" linecolor rgb "#3288BD" lw 4