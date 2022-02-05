#!/usr/bin/env python
# coding: utf-8

# In[64]:


##SCRIPT PARA LEITURA DAS ARTES ENTREGUES
##versão 1.0
##
##CRIAÇÃO DE ARQUIVO CSV COM A SEGUINTE FORMATAÇÃO:
##    -nome arquivo entregue
##        jobs_names
##    -lista com data criação (dia semana, mes, dia, horário, ano)
##        jobs_year
##        jobs_month
##        jobs_day
##        jobs_week
##        jobs_hour
##        jobs_minute
##        jobs_second
##    -nome jornal cliente
##        jobs_Producao
##    -nome retranca matéria
##        jobs_retranca
##    -nome tipo de arte
##        jobs_Tipo
##    -nome artista responsável
##        jobs_Artista
##
##    -salva ARTES DO DIA ANTERIOR
##    -salvar 1 arquivo TypeForm_YY-MM-DD.csv para cada dia do ano
##
##
##FUNÇÕES:

##    -implementar o arquivo executável
##    -implementar um BAT para atualização do CSV a cada 24 horas


import stat
import time
import os
import csv
from datetime import datetime, timedelta, timezone, date
from pathlib import Path
from os import path
from glob import glob



# LISTAS CDESIGN - variáveis para filtro

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


# FUNÇÃO FILTRO

def FN_filtro(listaFinal, listaFiltro):
    for i in jobs_index:
        dinName = jobs_names[i].upper()
        dinFilter = []
        for p in listaFiltro:
            if p in dinName:
                dinFilter.append(p)
            else:
                continue
        if len(dinFilter) == 0:
            listaFinal.append(var_nula)
        else:
            listaFinal.append(dinFilter[0])

            

def get_files_in(folder='L:\\ARTE_para_ILHAS\\INGEST\\Processados', pattern='*.mxf'):
    return glob(path.join(folder, pattern))

mypath = 'L:\\ARTE_para_ILHAS\\INGEST\\Processados'
mypattern = '*.mp4'
mypathLen = len(mypath) + 1
mypatternLen = -4

#full_path_name = get_files_in(mypath, mypattern)
full_path_name = get_files_in()

file_names = [x[mypathLen:] for x in full_path_name]
jobs_names = [y[:mypatternLen] for y in file_names]
jobs_dates = []
jobs_year = []
jobs_month = []
jobs_day = []
jobs_week = []
jobs_hour = []
jobs_minute = []
jobs_second = []
jobs_Producao = []
jobs_Artista = []
jobs_Tipo = []
jobs_retranca = []

jindex = 0
jobs_index = [jindex for jindex in range(len(jobs_names))]



# COLUNA PRODUÇÃO (jobs_Producao)

FN_filtro(jobs_Producao, jornais)



# COLUNA ARTISTA RESPONSAVEL (jobs_Artista)

FN_filtro(jobs_Artista, siglasArtistas)



# COLUNA TIPO DE ARTE (jobs_Tipo)

FN_filtro(jobs_Tipo, tiposArtes)



# RETRANCA DA ARTE (jobs_retranca)

for job in jobs_names:
    fbarra = '_'
    if fbarra in job:
        dinList = job.split('_')
        jobs_retranca.append(dinList[1])
    else:
        dinList = job.split(' ')
        jobs_retranca.append(dinList[1])
        

# CRIA COLUNA DATAS

for entry in full_path_name:
    path = Path(entry)
    statResult = path.stat()
    dateDin = time.ctime(statResult[stat.ST_MTIME])
    jobs_dates.append(dateDin.split())
    dateDinList = dateDin.split()
    jobs_year.append(dateDinList[4])
    jobs_month.append(dateDinList[1])
    jobs_day.append(dateDinList[2])
    jobs_week.append(dateDinList[0])
    timeDinList = dateDinList[3].split(':')
    jobs_hour.append(timeDinList[0])
    jobs_minute.append(timeDinList[1])
    jobs_second.append(timeDinList[2])



## CRIAÇÃO DO ARQUIVO CSV FINAL

finalCSVheader = ['PRODUÇÃO', 'RETRANCA', 'TIPO', 'ARTISTA', 'ANO', 'MÊS', 'DIA', 'SEMANA', 'HORA', 'MINUTOS', 'SEGUNDOS']
finalCSV = []
Filedate = str(date.today())
FileList = Filedate.split('-')
FileYear = str(FileList[0])
FMonth = int(FileList[1])
FileMonth = meses[(FMonth-1)]
Fday = int(FileList[2])
FileDay = str(Fday-1)

for i in jobs_index:
        if jobs_year[i] == FileYear:
            if jobs_month[i] == FileMonth:
                if jobs_day[i] == FileDay:
                    finalCSV.append([
                        jobs_Producao[i],
                        jobs_retranca[i],
                        jobs_Tipo[i],
                        jobs_Artista[i],
                        int(jobs_year[i]),
                        jobs_month[i],
                        int(jobs_day[i]),
                        jobs_week[i],
                        int(jobs_hour[i]),
                        int(jobs_minute[i]),
                        int(jobs_second[i]),
                        ])

findex = 0
CSV_index = [findex for findex in range(len(finalCSV))]

saveToday = datetime.today()
saveDate = saveToday - timedelta(1) 
saveDate = saveDate.strftime("%y-%m-%d")

path = os.chdir(CSV_filter)
#print(path)
path_list = os.listdir(path)
#print(path_list)
savePath = str(CSV_dir) + '\\TypeForm_' + str(saveDate) + '.csv'
#print(savePath)
saveFile = 'TypeForm_' + str(saveDate) + '.csv'
#print(saveFile)

dinCond=[1]

for n in path_list:
    if (n == saveFile):
        print ('A tabela desse dia já existe!')
        dinCond[0]= False
        break
    else:
        dinCond[0]= True
        continue

if dinCond[0] == True:
    print ('Arquivo salvo: ' + str(saveFile))
    with open(savePath, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(finalCSVheader)
        for row in CSV_index:
            w.writerow(finalCSV[row])
    f.close()



## RESULTS

##print(len(jobs_index))
##print(len(jobs_retranca))
##print(finalCSV[0])
##print(finalCSV[-1])

##print(jobs_index)
##print(jobs_names)
##print(jobs_Producao)
##print(jobs_retranca)
##print(jobs_Tipo)
##print(jobs_Artista)
##print(jobs_dates)
##print(jobs_year)
##print(jobs_month)
##print(jobs_day)
##print(jobs_week)
##print(jobs_hour)
##print(jobs_minute)
##print(jobs_second)





