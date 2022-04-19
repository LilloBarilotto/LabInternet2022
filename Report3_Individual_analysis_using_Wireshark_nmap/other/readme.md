# COSA HO NOTATO DI STRANO

## R1 RESULT
Allora, la cosa che salta all'occhio prima di tutto, è il SYN fatto da nmap per fare la scansione delle porte.
1- La lunghezza del pacchetto SYN (quindi io che genero attraverso nmap) senza privilegi è 74, con privilegi 58, attraverso wireshark si nota come i byte di differenza siano presenti a causa del campo Opzioni (20 vs 4 byte) nel livello 4 (scansione con TCP)
