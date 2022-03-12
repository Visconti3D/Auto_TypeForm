import stat
import time
import os
import csv
from datetime import datetime, timedelta, timezone, date
from pathlib import Path
from os import path
from glob import glob

saveToday = datetime.today()
print(saveToday)
saveDate = saveToday - timedelta(11)        ### AQUI EU ESCOLHO O DIA A SER IMPRESSO, BASTA ESCOLHER QUANTOS DIAS PARA TRÁS DO ATUAL ###
print(saveDate)
saveDate = saveDate.strftime("%y-%m-%d")
print(saveDate)
saveYear = '20' + str(saveDate[:2])
print(saveYear)
saveMonth = saveDate[3:5]
print(saveMonth)
saveDay = saveDate[-2:]
print(saveDay)
