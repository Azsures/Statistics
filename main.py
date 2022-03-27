import math
import numpy


def c_table(vec, k, c, li, media):
  cont = c
  num = 0
  vecfi = numpy.array([])
  i = 0
  ind = li
  l1 = ind
  l2 = l1+c
  var = 0
  siz = numpy.size(vec)
  med = 0
  fac = 0
  while cont < 1:
    cont = cont*10
  print("Altura \t\t fi \t fr \t fac")
  for a in range(int(k)):
    for _ in range(siz):
      if vec[i] >= ind and vec[i] < ind+c-0.001:
        num += 1
      i += 1
    fr = round((num/siz), 2)
    fac += (num/siz)
    vecfi = numpy.append(vecfi, num)
    med += ((l1 + l2) / 2) * num
    print(f'{l1:.2f}' "|-> " f'{l2:.2f}' + "\t " f'{num}' + "\t" f'{fr}' + "\t"  f'{fac:.2f}')
    ind = round(ind+c, 2)
    num = 0
    i = 0
    l1 = round(l2, 2)
    l2 = round(l2+c, 2)
  med /= siz
  i = 0
  l1 = li
  l2 = l1+c
  for _ in range(int(k)):
    var += ((((l1 + l2)/2) - med)**2) * vecfi[i]
    i += 1
    #print(f'{l1, l2, vecfi[i-1]}' f'{var:.4f}')
    l1 = round(l2, 2)
    l2 = round(l2+c, 2)
  var = var/(siz-1)
  print("\nMedia: " f'{med:.2f}')
  print("Variance: " f'{var:.4f}')
  print("Standart deviation: " f'{math.sqrt(var):.2f}\n')
  return vecfi


def stand_deviantion(vec, media, vecfi, k, li, r):
  var = 0
  i = 0
  j = 0
  lf = li+r
  siz = numpy.size(vec)
  for a in range(int(k)):
    var += ((((li+lf)/2)-media)**2)*vecfi[j]
    j += 1
    li = lf
    lf += r
  var = var/siz-1
  print("Variance: " f'{var:.2f}')
  print("Standart deviation: " f'{math.sqrt(var):.2f} \n')


nov = int(input("Input the size of population: "))
lis = numpy.array([])
vecfi = numpy.array([])
media = 0
for i in range(nov):
  temp = float(input())
  lis = numpy.append(lis, temp)
lis = numpy.sort(lis)
k = float(math.sqrt(nov))
k = round(k, 0)
temp = round(lis[nov-1] - lis[0], 2)
c = temp/(k-1)
c = round(c, 2)
li = lis[0] - (c/2)
cont = c
while cont < 1:
  cont = cont*10
cont = math.ceil(cont)
print()
vecfi = c_table(lis, k, c, li, media)
