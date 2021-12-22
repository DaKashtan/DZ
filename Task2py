import math
from math import log
k=int(input('Сообщите количество списков - '))
M=[]
for i in range (1,k+1):
    M.append(input('Введите список: ').split())
def length(M):
    l = len(M[1])
    for i in range(0, k):
        l2 = len(M[i])
        l = max(l, l2)
    for i in range (0, k):
        li=len(M[i])
        while li<l:
            M[i].append(0)
            li=len(M[i])
    for i in range (0,k):
        for j in range (0,l):
            M[i][j]=int(M[i][j])

def sum(M):
    DEGREE=[]
    for i in range (0,k-1):
        a=[]
        for j in range (0,len(M[i])):
            a.append(M[i][j]+ M[i+1][j])
        DEGREE.append(a)
    print("Сумма ", DEGREE)
def dif(M):
    DEGREE=[]
    for i in range (0,k-1):
        a=[]
        for j in range (0,len(M[i])):
            a.append(M[i][j]- M[i+1][j])
        DEGREE.append(a)
    print("Разность ", DEGREE)
def mult(M):
    DEGREE=[]
    for i in range (0,k-1):
        a=[]
        for j in range (0,len(M[i])):
            a.append(M[i][j]* M[i+1][j])
        DEGREE.append(a)
    print("Произведение ", DEGREE)
def div(M):
    DEGREE=[]
    for i in range (0,k-1):
        a=[]
        for j in range (0,len(M[i])):
            if M[i + 1][j] != 0:
                a.append(M[i][j]/ M[i+1][j])
            else:
                a.append('NA')
        DEGREE.append(a)
    print("Деление ", DEGREE)
def degree(M):
    DEGREE=[]
    for i in range (0,k-1):
        a=[]
        for j in range (0,len(M[i])):
            a.append(M[i][j]** M[i+1][j])
        DEGREE.append(a)
    print("Возведение в степень ", DEGREE)
def root(M):
    ROOT=[]
    for i in range (0,k-1):
        a=[]
        for j in range (0,len(M[i])):
            if M[i][j] != 0 and M[i+1][j]!=0:
                a.append(round(M[i][j]** (1/M[i+1][j]),2))
            else:
                a.append('NA')
        ROOT.append(a)
    print("Извлечение корня ",ROOT)
def log(M):
    LOG=[]
    for i in range (0,k-1):
        a=[]
        for j in range (0,len(M[i])):
            if M[i][j]==0 or M[i+1][j]==0 or M[i+1][j]==1:
                a.append('NA')
            else:
                a.append(math.log(M[i][j],M[i+1][j]))
        LOG.append(a)
    print("Логарифмирование ",LOG)
length(M)
D = input('Выберете действие над списками : Сложение, Вычитание, Умножение, Деление, Возведение в степень, Извлечение корня, Логарифмирование - ')
if D == 'Сложение' or D == 'сложение' or D == '+':
    sum(M)
elif D == 'Вычитание' or D == 'вычитание' or D == '-':
    dif(M)
elif D == 'Умножение' or D == 'умножение' or D == '*':
    mult(M)
elif D == 'Деление' or D == 'деление' or D == '/':
    div()
elif D == 'Возведение в степень' or D == 'возведение в степень' or D == '^':
    degree(M)
elif D == 'Извлечение корня' or D == 'извлечение корня':
    root(M)
elif D == 'Логарифмирование' or D == 'логарифмирование'or D == 'log':
    log(M)
else:
    print('Некорректно задана операция')



