import os
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
from pathlib import Path


## VARIÁVEIS E FILTROS

CSV_dir = "S:\\A R Q U I V O S\\FERRAMENTAS\\AutoTypeform\\TESTE"
CSV_filter = r"S:\\A R Q U I V O S\\FERRAMENTAS\\AutoTypeform\\TESTE"
var_nula = 'x'
tiposArtes = ['ARTE', 'DESTAQUE', 'FOTO', 'TELA', 'PASSEIO', 'DISPLAY', 'MAPA', 'GRAFICO']
siglasArtistas = ['AMB', 'AGB', 'EBV', 'FQB', 'GVB', 'KMB', 'KLB', 'IRB', 'TFB', 'WMB', 'PHB']
artistas = ['AMANDA MARTINS', 'ANDRE GATTO', 'ESTEVAO BRITTO', 'FELIPE DE QUEIROZ', 'GUSTAVO VISCONTI',
            'KATIA DE MEDEIROS', 'KARLA LUZ', 'ISABELLA RIBEIRO', 'THAIS FIUZA', 'WAGNER MAIA']
jornais = ['H1', 'BDDF', 'BDBR', 'DF1', 'GE', 'JH', 'DF2',
           'JN', 'JG', 'GNEWS', 'MH16', 'MH18', 'J10', 'ED16', 'ED18']
meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
DIASmesesAno = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DIASmesesAnoBisexto = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



## CARREGANDO E JUNTANDO OS DADOOS

files = Path(CSV_filter).rglob('*.csv')
df = pd.concat(map(pd.read_csv, files))

#print(df.columns)

## CRIANDO COLUNAS DOS DIAS DO MÊS PARA GRÁFICOS

ranMES = range(DIASmesesAno[0])
DIASdoMES = list(ranMES)
Column_diasMES = [x+1 for x in DIASdoMES]

sns.set(rc={'figure.figsize':(8,10)})



##  TOTAL ARTES x DIAS DO MÊS

df_TM = df['DIA'].value_counts().reset_index()      #soma as ocorrencias de um valor
df_TM.columns = ['Dia', 'Total de artes']
df_TM_final = df_TM.sort_values(by=['Dia'])

plt.subplot(5,1,1)
sns.set_style('darkgrid')
sns.barplot(data=df_TM_final, x='Dia', y='Total de artes').set_title('Total Artes no Mês')



##  TOTAL ARTES de todos ARTISTAS no MÊS

df_AT = df['ARTISTA'].value_counts().reset_index()
df_AT.columns = ['Artistas', 'Total de artes por mês']
df_AT_final = df_AT.sort_values(by=['Artistas'])

plt.subplot(5,1,2)
sns.set_style('darkgrid')
sns.barplot(data=df_AT_final, x='Artistas', y='Total de artes por mês').set_title('Total Artes no Mês por Artista')



##  TOTAL ARTES de todas PRODUÇÕES no MÊS

df_JM = df['PRODUÇÃO'].value_counts().reset_index()
df_JM.columns = ['Produção', 'Total de artes por mês']
df_JM_final = df_JM.sort_values(by=['Produção'])

plt.subplot(5,1,3)
sns.set_style('darkgrid')
sns.barplot(data=df_JM_final, x='Produção', y='Total de artes por mês').set_title('Total Artes no Mês por Produção')



##  TOTAL ARTES de cada PRODUÇÃO no MÊS



def prodCadaMes(prod):
    df_dinPROD = df[df.PRODUÇÃO == prod].reset_index()
    df_din = df_dinPROD['DIA'].value_counts().reset_index()      #soma as ocorrencias de um valor
    df_din.columns = ['Dia', 'Total de artes']
    df_din_final = df_din.sort_values(by=['Dia'])
    df_din_final.reset_index()
    return df_din_final

df_BDDF = prodCadaMes('BDDF')

plt.subplot(5,1,4)
sns.set_style('darkgrid')
sns.barplot(data=df_BDDF, x='Dia', y='Total de artes').set_title('Total Artes BDDF no Mês')



##  TOTAL ARTES de cada ARTISTA no MÊS

df_ART = df[df.ARTISTA == 'GVB'].reset_index()
df_TGBV = df_ART['DIA'].value_counts().reset_index()      #soma as ocorrencias de um valor
df_TGBV.columns = ['Dia', 'Total de artes']
df_TGBV_final = df_TGBV.sort_values(by=['Dia'])
print(df_TGBV_final)
plt.subplot(5,1,5)
sns.set_style('darkgrid')
sns.barplot(data=df_TGBV_final, x='Dia', y='Total de artes').set_title('Total Artes Gustavo no Mês')



##  IMPRIMINDO E SALVANDO OS GRÁFICOS

plt.tight_layout()
plt.savefig('RELATÓRIO JANEIRO.png')
plt.show()















#Day1_ARTES = rawdf[rawdf.DIA == 1]          #Filtro por Dia (coluna)
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

