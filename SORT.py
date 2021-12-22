list = [int(i) for i in input('Введите список чисел: ').split()]
def sort(list):
    for i in range(1,len(list)):
        j=list[i]
        k=i-1
        while k>=0 and j<list[k]:
            list[k+1]=list[k]
            k-=1
        list[k+1]=j
    return list
print(sort(list))