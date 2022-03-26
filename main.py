import math
import numpy


def c_table(vec, k, c, li):
  cont = c
  num = 0
  i = 0
  ind = li
  l1 = ind
  l2 = l1+c
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
    med += ((l1 + l2) / 2) * num
    print(f'{l1:.2f}' "|-> " f'{l2:.2f}' + "\t " f'{num}' + "\t" f'{fr}' + "\t"  f'{fac:.2f}')
    ind = round(ind+c, 2)
    num = 0
    i = 0
    l1 = round(l2, 2)
    l2 = round(l2+c, 2)
  med /= siz
  print("\nMedia: " + f'{med:.2f}')
  return med


def stand_deviantion(vec, media):
  var = 0
  i = 0
  siz = numpy.size(vec)
  for _ in range(siz):
    var += ((vec[i]-media)**2)
  var /= siz
  print("Variance: " f'{var:.2f}')
  print("Standart deviation: " f'{math.sqrt(var):.2f}')


nov = int(input("Input the size of population: "))
lis = numpy.array([])
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
media = c_table(lis, k, c, li)
stand_deviantion(lis, media)