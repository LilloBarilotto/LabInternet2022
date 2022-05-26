
REPORT di GRUPPO #3 - misure di goodput

Nella relazione di gruppo riportare:

    Collegare tra host H1, H2, H3 tramite switch come sempre ad una rete locale
    Disabilitare offloading, ed impostare le velocità di trasmissione a 10Mb/s, full/half duplex a seconda dello scenario
    Descrivere del testbed utilizzato, dettagliando la configurazione HW (PC, interfacce usate, velocità) e SW (sistema operativo, tool usati). 
    Discutere e giustificare la scelta dei parametri di generazione dei dati da parte della applicazione nttcp (parametri -l e -n)
    Per ogni scenario
        descrivere il goodput atteso per ogni flusso dati, giustificando e motivando lo stesso discutenso di i) eventuali problemi a livello fisico, ii) probabilità di collisioni e congestione a livello collegamento, iii) perdite a livello applicazione, iv) impatto delle intestazioni ed efficienza attesa
        effettuare l'esperimento, ripetendo lo stesso eventualmente più volte in presenza di fenomeni aleatori
        confrontare quanto predetto con quanto osservato sperimentalmente e giustiticare eventuali risultati non concordi

Nel report, riportare e commentare gli scenari, considerando flussi TCP, UDP, e, qualora ci siano più flussi contemporanei, un flusso UDP e uno TCP:

    ​A) singolo TX che trasmette a singolo RX, canali in FULL duplex
    B) singolo TX che trasmette a singolo RX, con almeno un canale (a scelta) in HALF duplex
    E) Due TX che trasmettono a singolo RX, con tutti canali in FULL duplex
    F) Due TX che trasmettono a singolo RX, con almento un canale (a scelta) in HALF duplex
    [opzionale] Singolo TX che trasmette a due RX, tutti canali in FULL duplex
    [opzionale] Singolo TX che trasmette a due RX, almeno un canale (a scelta) in HALF duplex

La scadenza per la consegna del report e' il domenica 15/5 - 23:59 CET. Il report può essere al più 4 pagine + una di intestazioni. I punti opzionali possono essere commentati usando una pagina aggiuntiva. Eventuli grafici di support o script possono essere messi in appendice.