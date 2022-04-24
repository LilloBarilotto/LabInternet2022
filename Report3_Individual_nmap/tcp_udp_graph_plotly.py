#IMPORT DELLE LIBRERIE
import pandas as pd
import plotly.express as px
import plotly.io as pio
import sys, os

#IMPORT DEI DATI
pio.kaleido.scope.mathjax = None #trick to solve problems with .pdf

if not os.path.exists("images"):
    os.mkdir("images")
    
if len(sys.argv) < 4:
     sys.exit("Wrong Usage, use : python plot_try.py [path_src] [ip_dest] [tcp_or_udp]")

path = sys.argv[1]
titleF= sys.argv[2] +'_'+ sys.argv[3]

df= pd.read_csv(path,delimiter=' ')

fig = px.scatter(df, x="Time", y="Port",width=600, height=600,
                  labels={"Time": "Time [s]", "Port": "Port [Number]"},
                )
fig.update_layout(title={"text": titleF+"_yport_xtime", "x":0.5, "xanchor": "center","yanchor": "top"})
    
fig.show()
fig.write_image("images/"+titleF+"_yport_xtime"+".pdf")

df_group= df.groupby('Port',  as_index=False).count()
fig2 = px.scatter(df_group, x="Port", y="Time", width=1200, height=600,
                  labels={"Port": "Port [Number]", "Time": "CounterTRY [count_number]"}
                )
fig2.update_layout(title={"text": titleF+"_ynumbertime_xport", "x":0.5, "xanchor": "center","yanchor": "top"})

fig2.show()
fig2.write_image("images/"+titleF+"_ynumbertime_xport"+".pdf")