import seq
ref=input('Задайте референсную последовательность: ')
k=int(input('Задайте количество проверяемых последовательностей - '))
M=[]
for i in range (k):
    M.append(input('Введите последовательность: '))
def sortchange(M):
    c=[]
    for i in range(0,k):
        l = 0
        for j in range(0,len(M[i])):
            if M[i][j]!=ref[j]:
                l+=1
        c.append(l)
    for i in range(1,len(c)):
        j=c[i]
        g=M[i]
        n=i-1
        while n>=0 and j<c[n]:
            c[n+1]=c[n]
            M[n + 1] = M[n]
            n-=1
        M[n + 1] = g
        c[n+1]=j
    print(M)
sortchange(M)    
