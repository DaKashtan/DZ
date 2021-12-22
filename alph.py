def alph():
  A = input('Задайте алфавит - ').split()
  seq = input('Введите последовательность - ')
  for i in range(len(seq)):
      G = seq.count(A[i])
      print(A[i], G)