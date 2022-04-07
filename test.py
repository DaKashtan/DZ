from Bio.SeqIO import parse
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import re

vector = open(input("Задайте адрес к файлу с векторной последовательностью: "),'r') #последовательность вектора
records = parse(vector, "fasta")
for record in records:
    vector_sequence = record.seq

vstavki = []
vst = open(input("Задайте адрес к файлу с вставками: "), 'r') #открываем файл со вставками
vstavki = map(str.strip, vst.readlines())
#дальше сшиваем вставки в одну
new_insert_sequence = ''.join(vstavki)

#открываем файл с сайтами рестрикции
sites1 = open(input("Задайте адрес к файлу с сайтами рестрикции: "), 'r') ## правка
sites = [i for i in sites1.read().splitlines() if i] #получаем список с сайтами
good_sites = []
for i in sites:
    if i in vector_sequence:
        good_sites.append(i) #добавляем в список гуд_сайтс сайты, которые есть в векторе
sum_inclusions=[]
for i in good_sites:
    inclusions=re.findall(i,vector_sequence)
    sum_inclusions.append(len(inclusions)) #Подсчет количества включений "хороших" сайтов
    inclusions=[]
ind=sum_inclusions.index(min(sum_inclusions))
site_restr=good_sites[ind] #Находим сайт рестрикции

a, b = vector_sequence.split(site_restr)
result = a+site_restr+new_insert_sequence+site_restr + b #теперь берем сайт рестриции и добавляем вставку
print(result)

# вывод манипуляций
print('1. Проведение ПЦР... сайт рестрикции', site_restr)
print('2. Обработка рестриктазой...')
print('3. Лигирование...')
print('4. Конечный результат...', result)


#import pandas as pd
#enz_data = pd.read_html("http://rebase.neb.com/rebase/azlist.re2.cy.html", skiprows=1)
#print(enz_data)




