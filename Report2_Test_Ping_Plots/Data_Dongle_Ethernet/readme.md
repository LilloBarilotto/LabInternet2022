# Cosa posso capire da alcuni di questi risultati
## TEST SU 10M_Dongle_1.txt
Ping con -c 10, -i 0.2

Mmmh possiamo ipotizzare alcune cose da questi strani risultati, in sequenza potremmmo dire che:
-il dongle ethernet non faccia Store&Forward, si vede chiaramente che RttMin reale sta sopra RttTheory di poco.
-riguardando il caso di prima, potrebbe essere che la formula ricavata per lo switch vada bene solo per lo switch, il che potrebbe aver senso.


 D'altronde stiamo confrontando una formula su un dispositivo che potrebbe fare Store&Forward ma la funzione associata potrebbe essere diversa, questo perchè diversamente da prima abbiamo dal un lato un collegamento con un cavo di capacità C e dall'altro un collegamento attraverso una USB3.0 (sostituendo allo switch nel nostro disegno/rappresentazione il nostro dongle ethernet). Rimane comunque strano perchè, ponendo il caso peggiore, la porta USB-C del mio dispositivo potrebbe essere una 2.0, la quale arriva comunque a velocità massime di 420Mbit/s, quindi non dovrebbe in ogni caso intaccare la capacità della rete.
 
Che i ritardi di elaborazione e propagazione in questi casi non siano trascurabili?
La cosa più strana è l'effetto onda triangolare se confrontato con i risultati di un test 10Mbit_Diretto ma senza dongle. Questo effetto particolare invece potrebbe essere dovuto a un disturbo nel dongle oppure nel mio cavo Ethernet personale.

I casi fatti con il dongle sono stati fatti attraverso il laptop con Pop!_OS 21.10 sprovvisto di porta Ethernet "nativa", con IP 172.16.1.1 da cui veniva effettuato il ping verso 172.16.1.2, host su un portatile con la distro avviata da chiavetta fornita nel corso con porta Ethernet nativa

## TEST SU 100M_Dongle.txt
Oltre a ciò che è stato già detto sul caso del 10M_Dir_Dongle, qui si può vedere in modo più accentuato un disturbo che definisce una errorbar di circa 0.3ms sull'asse y nei risultati.