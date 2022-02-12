import os
from datetime import datetime, timedelta, timezone, date
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
from pathlib import Path


## VARIÁVEIS E FILTROS


var_nula = 0
tiposArtes = ['ARTE', 'DESTAQUE', 'FOTO', 'TELA', 'PASSEIO', 'DISPLAY', 'MAPA', 'GRAFICO']
siglasArtistas = ['AMB', 'AGB', 'EBV', 'FQB', 'GVB', 'KMB', 'KLB', 'IRB', 'TFB', 'WMB', 'PHB']
artistas = ['AMANDA MARTINS', 'ANDRE GATTO', 'ESTEVAO BRITTO', 'FELIPE DE QUEIROZ', 'GUSTAVO VISCONTI',
            'KATIA DE MEDEIROS', 'KARLA LUZ', 'ISABELLA RIBEIRO', 'THAIS FIUZA', 'WAGNER MAIA']
jornais = ['H1', 'BDDF', 'BDBR', 'DF1', 'GE', 'JH', 'DF2',
           'JN', 'JG', 'GNEWS', 'MH16', 'MH18', 'J10', 'ED16', 'ED18']
meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

DIASmesesAno = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DIASmesesAnoBisexto = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



## CARREGANDO E JUNTANDO OS DADOOS DOS ARQUIVOS CSV

#CARREGANDO DATA ATUAL
saveToday = datetime.today()
saveDate = saveToday - timedelta(1) 
saveDate = saveDate.strftime("%y-%m-%d")
saveMonth = saveDate[0:5]

CSV_filter = r"S:\\A R Q U I V O S\\FERRAMENTAS\\AutoTypeform\\CSV_FINAL\\relatorios_" + str(saveMonth)
files = Path(CSV_filter).rglob('*.csv')
df = pd.concat(map(pd.read_csv, files))

#print(df.columns)

## CRIANDO COLUNAS DOS DIAS DO MÊS PARA GRÁFICOS

getMonth = int(saveDate[3:5])
getYear = int(saveDate[0:2])
if not (getYear%4) == 0:
    ranMES = range(DIASmesesAno[getMonth])
else:
    ranMES = range(DIASmesesAnoBisexto[getMonth])    

DIASdoMES = list(ranMES)
Column_diasMES = [x+1 for x in DIASdoMES]

df_DIASdoMES = pd.DataFrame (Column_diasMES, columns=['Dia'])
df_DIASdoMES['zeros'] = 0


## CONFIGURAÇÕES INICIAIS DO RELATORIO 01

r1 = sns.set(rc={'figure.figsize':(8,10)})


##  TOTAL ARTES x DIAS DO MÊS

df_TM = df['DIA'].value_counts().reset_index()      #soma as ocorrencias de um valor
df_TM.columns = ['Dia', 'Total de artes']
df_TM_final = df_TM.sort_values(by=['Dia'])
df_TM_final.reset_index(drop=True)

## CRIANDO DATAFRAMES DE 30 linhas
df_Finalmes = df_DIASdoMES.merge(df_TM_final, how='left', on='Dia')
df_Finalmes['Total de artes'] = df_Finalmes['Total de artes'].fillna(0).astype(int)
df_Finalmes.drop('zeros', axis=1, inplace=True)
## FIM CRIA 30 LINHAS

plt.subplot(3,1,1)
sns.set_style('darkgrid')
sns.barplot(data=df_Finalmes, x='Dia', y='Total de artes').set_title('Total Artes no Mês')




##  TOTAL ARTES de todos ARTISTAS no MÊS

df_AT = df['ARTISTA'].value_counts().reset_index()
df_AT.columns = ['Artistas', 'Total de artes por mês']
df_AT_final = df_AT.sort_values(by=['Artistas'])

plt.subplot(3,1,2)
sns.set_style('darkgrid')
sns.barplot(data=df_AT_final, x='Artistas', y='Total de artes por mês').set_title('Total Artes no Mês por Artista')



##  TOTAL ARTES de todas PRODUÇÕES no MÊS

df_JM = df['PRODUÇÃO'].value_counts().reset_index()
df_JM.columns = ['Produção', 'Total de artes por mês']
df_JM_final = df_JM.sort_values(by=['Produção'])

plt.subplot(3,1,3)
sns.set_style('darkgrid')
sns.barplot(data=df_JM_final, x='Produção', y='Total de artes por mês').set_title('Total Artes no Mês por Produção')


##  IMPRIMINDO E SALVANDO RELATORIO 01

Report01 = r"S:\\A R Q U I V O S\\FERRAMENTAS\\AutoTypeform\\RELATORIOS_FINAIS\\RELATÓRIO 01_" + str(saveMonth) + ".png"
sns.set_context("poster")
plt.tight_layout()
plt.savefig(Report01)
plt.show()



##  TOTAL ARTES de cada PRODUÇÃO no MÊS


sns.set_style('whitegrid')
sns.set_context("poster")
f, ax = plt.subplots(4, 3, figsize=(8, 10))


def prodCadaMes(prod):
    df_dinPROD = df[df.PRODUÇÃO == prod].reset_index()
    df_din = df_dinPROD['DIA'].value_counts().reset_index()      #soma as ocorrencias de um valor
    df_din.columns = ['Dia', 'Total de artes']
    df_din_final = df_din.sort_values(by=['Dia'])
    df_din_final.reset_index(drop=True)
    df_dinmes = df_DIASdoMES.merge(df_din_final, how='left', on='Dia')
    df_dinmes['Total de artes'] = df_dinmes['Total de artes'].fillna(0).astype(int)
    df_dinmes.drop('zeros', axis=1, inplace=True)
    return df_dinmes

reportJORNAIS = ['H1', 'BDDF', 'BDBR', 'DF1', 'GE', 'JH', 'DF2','JN', 'JG', 'GNEWS']
rangeRepJOR = range(len(reportJORNAIS)-1)
for i in rangeRepJOR:
    prodDin = reportJORNAIS[i]
    df_DIN = prodCadaMes(prodDin)
    plt.subplot(4,3,i)
    sns.set_style('darkgrid')
    sns.barplot(data=df_DIN, x='Dia', y='Total de artes').set_title('Total Artes ' + str(prodDin) + ' no Mês')


Report02 = r"S:\\A R Q U I V O S\\FERRAMENTAS\\AutoTypeform\\RELATORIOS_FINAIS\\RELATÓRIO 02_" + str(saveMonth) + ".png"
plt.tight_layout()
plt.savefig(Report02)
plt.show()




##  TOTAL ARTES de cada ARTISTA no MÊS

df_ART = df[df.ARTISTA == 'GVB'].reset_index()
df_TGBV = df_ART['DIA'].value_counts().reset_index()      #soma as ocorrencias de um valor
df_TGBV.columns = ['Dia', 'Total de artes']
df_TGBV_final = df_TGBV.sort_values(by=['Dia'])
#print(df_TGBV_final)
plt.subplot(5,1,5)
sns.set_style('darkgrid')
sns.barplot(data=df_TGBV_final, x='Dia', y='Total de artes').set_title('Total Artes Gustavo no Mês')



















###Day1_ARTES = rawdf[rawdf.DIA == 1]          #Filtro por Dia (coluna)
#raw_BDBR = rawdf[rawdf.PRODUÇÃO.isin(['BDBR'])]          #Filtro por PRODUCAO TOTAL (coluna)
#raw_Gustavo = rawdf[rawdf.ARTISTA.isin(['GVB'])]          #Filtro por ARTISTA (coluna)

#Day3_total_ARTES = len(Day3_ARTES)          #Filtro Total pedidos do dia (coluna)
#print(rawdf.iloc[0:3])          #Filtra as linhas selecionadas
#ARTES_mes_dia = rawdf[(rawdf.MÊS == 'Jan') & (rawdf.DIA == 1)]          #Filtra as linhas por condicional da coluna
#ARTES_mes_dia.reset_index(inplace = True, drop = True)          #Reseta os índices do DF.

#Day3_BDDF = Day3_ARTES[Day3_ARTES.PRODUÇÃO.isin(['BDDF'])]          #Filtro por PRODUCAO DIA (coluna)
#Day3_hour_BDDF = Day3_BDDF['HORA']
#print(Day3_hour_BDDF)
#print(ARTES_mes_dia)
#print(len(ARTES_mes_dia))

