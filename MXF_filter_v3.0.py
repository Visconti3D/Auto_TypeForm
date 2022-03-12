#!/usr/bin/env python
# coding: utf-8

# In[64]:


##SCRIPT PARA LEITURA DAS ARTES ENTREGUES
##versão 2.2
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
##    -implementar o arquivo executável
##    -implementar um BAT para atualização do CSV a cada 24 horas
##
##
##FUNÇÕES:
##    -salvar 5 arquivos TypeForm_YY-MM-DD.csv para os últimos 5 dias



import stat
import time
import os
import csv
from datetime import datetime, timedelta, timezone, date
from pathlib import Path
from os import path
from glob import glob



# LISTAS CDESIGN - variáveis para filtros

CSV_dir = "S:\\A R Q U I V O S\\FERRAMENTAS\\GitRepository\\Auto_Typeform\\CSV_FINAL"
var_nula = 'x'
tiposArtes = ['ARTE', 'DESTAQUE', 'FOTO', 'TELA', 'PASSEIO', 'DISPLAY', 'MAPA', 'GRAFICO']
siglasArtistas = ['AMB', 'AGB', 'EBV', 'FQB', 'GVB', 'KMB', 'KLB', 'IRB', 'TFB', 'WMB', 'PHB']
artistas = ['AMANDA MARTINS', 'ANDRE GATTO', 'ESTEVAO BRITTO', 'FELIPE DE QUEIROZ', 'GUSTAVO VISCONTI',
            'KATIA DE MEDEIROS', 'KARLA LUZ', 'ISABELLA RIBEIRO', 'THAIS FIUZA', 'WAGNER MAIA']
jornais = ['H1', 'BDDF', 'BDBR', 'DF1', 'GE', 'JH', 'DF2',
           'JN', 'JG', 'GNEWS', 'MH16', 'MH18', 'J10', 'ED16', 'ED18']
monthsList = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
dayList = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
versoes = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15'] 
retrancas = []

# FUNÇÃO FILTRO por NOMES - insere o VALOR REQUISITADO quando existente ou VALOR NULO à uma posição vazia da tabela

def FN_filtro(listaFinal, listaFiltro):
    for i in jobs_index:
        dinName = jobs_names[i].upper()
        dinFilter = []
        for p in listaFiltro:
            if p in dinName:
                dinFilter.insert(0, p)
            else:
                continue
        if len(dinFilter) == 0:
            listaFinal.append(var_nula)
        else:
            listaFinal.append(dinFilter[0])


# FUNÇÃO FILTRO por CAMPOS"_" - insere o VALOR REQUISITADO quando existente ou VALOR NULO à uma posição vazia da tabela

def FN_filtro_campos(new_column, listaFiltro, campo):
    for i in jobs_index:
        dinName = jobs_names[i].upper()
        splitName = dinName.split('_')
        dinFilter = []
        campoValue = splitName[campo]
        if campoValue in listaFiltro:
            dinFilter.insert(0, campoValue)
        else:
            for p in listaFiltro:
               if p in dinName:
                   dinFilter.insert(0, p)
               else:
                   continue
        if len(dinFilter) == 0:
            new_column.append(var_nula)
        else:
            new_column.append(dinFilter[0])


# FUNÇÃO PARA DEFINIÇÃO DA PASTA e EXTENSÃO DOS ARQUIVOS CAPTURADOS            

def Fn_get_files_in(folder='L:\\ARTE_para_ILHAS\\INGEST\\Processados', pattern='*.mxf'):
    return glob(path.join(folder, pattern))

#variáveis para definições específicas 
mypath = 'L:\\ARTE_para_ILHAS\\INGEST\\Processados'
mypattern = '*.mxf'
mypathLen = len(mypath) + 1
mypatternLen = -4

#full_path_name = Fn_get_files_in(mypath, mypattern)
full_path_name = Fn_get_files_in()


# INICIALIZAÇÃO DAS LISTAS DOS JOBS
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
jobs_Retranca = []
jobs_Versao = []

jindex = 0
jobs_index = [jindex for jindex in range(len(jobs_names))]



# COLUNA PRODUÇÃO (jobs_Producao)
FN_filtro_campos(jobs_Producao, jornais, 0)
#FN_filtro(jobs_Producao, jornais)


# RETRANCA DA ARTE (jobs_Retranca)

def FN_filtro_Retranca(new_column, campo):
    for i in jobs_index:
        dinName = jobs_names[i].upper()
        splitName = dinName.split('_')
        dinFilter = []
        campoValue = splitName[campo]
        dinFilter.insert(0, campoValue)
        if len(dinFilter) == 0:
            new_column.append(var_nula)
        else:
            new_column.append(dinFilter[0])
            
FN_filtro_Retranca(jobs_Retranca, 1)


# COLUNA TIPO DE ARTE (jobs_Tipo)
FN_filtro_campos(jobs_Tipo, tiposArtes, 2)
#FN_filtro(jobs_Tipo, tiposArtes)


# COLUNA ARTISTA RESPONSAVEL (jobs_Artista)
FN_filtro_campos(jobs_Artista, siglasArtistas, -2)
#FN_filtro(jobs_Artista, siglasArtistas)


# COLUNA VERSAO DA ARTE (jobs_Versao)
FN_filtro_campos(jobs_Versao, versoes, -1)

#print(jobs_Retranca)        
#print(len(jobs_index))
#print(len(jobs_Retranca))

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



## CRIAÇÃO DOS ARQUIVOS CSV FINAIS

def Fn_Create_Day_DB(NumDaysBefore):
    finalCSVheader = ['PRODUÇÃO', 'RETRANCA', 'TIPO', 'ARTISTA', 'VERSÃO', 'ANO', 'MÊS', 'DIA', 'SEMANA', 'HORA', 'MINUTOS', 'SEGUNDOS']
    finalCSV = []
    
    saveToday = datetime.today()
    saveDate = saveToday - timedelta(NumDaysBefore)          ### AQUI EU ESCOLHO O DIA A SER IMPRESSO, BASTA ESCOLHER QUANTOS DIAS PARA TRÁS DO ATUAL ###
    saveDate = saveDate.strftime("%y-%m-%d")
    saveYear = '20' + str(saveDate[:2])
    saveMonth = saveDate[3:5]
    month = monthsList.index(saveMonth)             ## Converting Month 'numeral'('02') to 'String'('Feb')
    FileMonth = meses[month]
    saveDay = saveDate[-2:]
    if saveDay in dayList:
        saveDay = saveDay[-1]             ## Cleaning '0's from 'numeral'('02')
    fileDate = saveDate[0:5]


    for i in jobs_index:
        if jobs_year[i] == saveYear:
            if jobs_month[i] == FileMonth:
                if jobs_day[i] == saveDay:
                    finalCSV.append([
                        jobs_Producao[i],
                        jobs_Retranca[i],
                        jobs_Tipo[i],
                        jobs_Artista[i],
                        jobs_Versao[i],
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

    fileDatePath = str(CSV_dir) + '\\relatorios_' + str(fileDate)
    if not os.path.isdir(fileDatePath) == True:
        os.makedirs(fileDatePath)  

    CSV_filter = r"S:\\A R Q U I V O S\\FERRAMENTAS\\GitRepository\\Auto_Typeform\\CSV_FINAL\\relatorios_" + str(fileDate)
    path = os.chdir(r"S:\\A R Q U I V O S\\FERRAMENTAS\\GitRepository\\Auto_Typeform\\CSV_FINAL\\relatorios_" + str(fileDate))
    path_list = os.listdir(path)
    #print(path_list)
    savePath = str(CSV_dir) + '\\TypeForm_' + str(saveDate) + '.csv'
    #print(savePath)



    savePath = str(CSV_dir) + '\\relatorios_' + str(fileDate) + '\\TypeForm_' + str(saveDate) + '.csv'
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

## Creating the CSVs
        
Fn_Create_Day_DB(1)
Fn_Create_Day_DB(2)
Fn_Create_Day_DB(3)
Fn_Create_Day_DB(4)
Fn_Create_Day_DB(5)


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





