#Listor:
my_variable = "hello"

lista = []

grade1 = 33
grade2 = 55
grade3 = 66
grade4 = 45
grade5 = 76

#Append lägger till i slutet av listan
lista.append(grade1)
lista.append(grade2)
lista.append(grade3)
lista.append(grade4)
lista.append(grade5)

print(sum(lista)/len(lista))

grade = [33,44,55,66,77]

print(grade)

#Tuples: IMMUTABLE!!! Som en statisk lista. Elementen går ej att ändra. Fin# ns två sätt att skriva på.
tuple_grade = (77, 66, 55, 44)
tuple_grade_variant2 = 4,5,6,
print(tuple_grade)
print(tuple_grade_variant2)

#OBS!! GÅR ATT KOMMA RUNT DET STATISKA, se nedan.
tuple_grade = tuple_grade + (100,)
print(tuple_grade)
#Komma tecknet är viktigt.

#Sets vare element är unikt och är ej i ordning! printa flera ggr. och se.

set_grades = {grade1 ,grade1,55,55,77,88,99}
#kommer bara skriva ut grade1 och 55 en gång pga att elementen skall vara unika.
print(set_grades)
#Add lägger till i din set.
set_grades.add(11)
print(set_grades)

#Set operations
lottorad = {1, 2, 3 ,4 , 5}
vintsrad = {1, 3 ,5 , 7, 9, 11}
#Intersection jämför dina sets
print(lottorad.intersection(vintsrad))

#Union lägger ihop dina sets
print(lottorad.union(vintsrad))

#Differance tittar på skillanden mellan set a OCH set b. I det här fallet är skillanden 3,4.
print({1, 2, 3, 4}.difference({1,2,5,6}))

my_list = [10 ,20 ,70]
print(sum(my_list))

my_tuple1 = (1)
my_tuple2 = 2,

set1 = {14, 67, 8, 31, 5, 77, 9, 12}
set2 = {14, 67, 8, 31}
print(set1.intersection(set2))
if (set1.intersection(set2) != {5, 77, 9, 12}):
    print(True)
else:
    print(False)




