#импорт библиотек
import sys
from datetime import datetime
import igraph
import time

matrix = [[0, 1, 1, 0, 0, 0, 2, 0],
          [0, 0, 1, 0, 2, 0, 3, 0],
          [0, 0, 0, 0, 5, 0, 0, 0],
          [4, 0, 0, 0, 0, 0, 3, 2],
          [0, 0, 0, 0, 0, 12, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 5, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]
name = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]

def alina(): #вывод матрицы смежности
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 and j == 0:
                for k in range(len(name)):
                    print(name[k], end=" ")
                print()
            if matrix[i][j] == 12:
                print(matrix[i][j], end=" ")
            else:
                print(matrix[i][j], end="  ")
        print(name[i], end=" ")
        print()
alina()

def alina2(): #вывод списка ребер
    start_time = datetime.now()
    #построение списка ребер
    global rebra, ves, rebra_grafic
    rebra = []
    mas = []
    rebra_grafic = []
    ves = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                k = i+1
                q = j+1
                rebra += [tuple([k, q])]
                rebra_grafic += [tuple([i, j])]
                ves.append(matrix[i][j])
    print("Список ребер:", rebra)
    print("Cписок весов:", ves)
alina2()

def alina4(): #графическое представление
    G = igraph.Graph(directed = True) #создание ориентированного графа
    G.add_vertices(8) #добавление вершин в граф
    G.vs["label"] = name  #подписи вершин
    G.add_edges(rebra_grafic) #добавление ребер в граф
    G.es["weight"] = ves #задание весов ребрам
    G.es["label"] = ves #подписи ребер
    G.es["curved"] = False
    igraph.plot(G, bbox=(300, 300), vertex_label_color='black',
                vertex_label_size=10, vertex_size=20, vertex_color='white')
alina4()

def alina5(): #вывод массива записей
    dict = {0:'x1', 1: 'x2', 2: 'x3', 3: 'x4', 4: 'x5', 5: 'x6', 6: 'x7', 7: 'x8'}
    global zap
    zap = []
    num = [[] for i in range(len(matrix))]
    boor = [[] for i in range(len(matrix))]
    chill = [[] for i in range(len(matrix))]
    wei = [0 for i in range(len(matrix))]
    isxod = [0 for i in range(len(matrix))]
    rod = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                wei[i] += matrix[i][j]
                isxod[i] += matrix[i][j]
                num[j] += [i]
                num[i] += [j]
                chill[i] += [1 + j]
            if matrix[j][i] != 0:
                wei[i] += matrix[j][i]
                rod[i].append(j+1)
    for i in range(len(boor)):
        boor[i] += [j+1 for j in num[i]]
    for i in range(len(matrix)):
        zap += [{'№ вершины': i, 'Подпись': dict[i], 'Кол-во соседей': len(boor[i]), 'Соседи': boor[i],
                 'Кол-во детей': len(chill[i]), 'Дети': chill[i], 'Кол-во родителей': len(rod[i]), 'Родители': rod[i],
                 'Веса исходящих ребер': isxod[i], 'Веса входящих ребер': wei[i]-isxod[i], 'Веса инциндентных ребер': wei[i]}]
        print(zap[i])
alina5()

#пункт 6 для каждого из вида записей:

def sosed_massivzapisei(): #соседи заданной вершины графа для массива записей
    a = int(input("Введите номер вершины графа: "))
    start_time = datetime.now()
    q, w = "", ""
    for q in range(10**6):
        for i in range(len(zap)):
            for key, value in zap[i].items():
                if key == "Соседи" and i == a-1:
                    q = key
                    w = value
    time.sleep(5)
    print(q, ":", w)
    print("Время поиска соседей для массива записей", (datetime.now() - start_time)/10**6)
sosed_massivzapisei()

def posled_massivzapisei(): #последовательность вершин для массива записей
    alla = input('Введите номера вершин через пробел: ').split()
    start_time = datetime.now()
    yt = ""
    for q in range(10 ** 6):
        for k in alla:
            k = int(k)
            flag_local = False
            for key, value in zap[k - 1].items():
                if key == "Дети":
                    for i in range(len(alla) - 1):
                        for j in range(len(value)):
                            if value[j] == int(alla[i + 1]):
                                flag_local = True
            if flag_local == False and k != int(alla[-1]):
                yt = "Данная последовательность вершин НЕ образует цепь"
                break
            if k == int(alla[-1]):
                yt = "Данная последовательность вершин образует цепь"
    time.sleep(5)
    print(yt)
    print("Время ответа возможности цепочки для массива записей", (datetime.now() - start_time)/10**6)
posled_massivzapisei()

def numbervverx_massivzapisei(): #номера вершин для массива записей
    eue = int(input('Введите число: '))
    start_time = datetime.now()
    for q in range(10 ** 6):
        qwerty = []
        for i in range(len(zap)):
            for key, value in zap[i].items():
                if key == "Веса инциндентных ребер" and value > eue:
                    qwerty.append(i+1)
    time.sleep(5)
    print("Номера вершин, веса инц. ребер которых больше", eue, ":", qwerty)
    print("Время ответа номеров вершин для массива записей", (datetime.now() - start_time)/10**6)
numbervverx_massivzapisei()

def rebra_massixzapisei(): #кол-во ребер в графе по массиву записей
    for q in range(10 ** 6):
        start_time = datetime.now()
        count = 0
        for i in range(len(zap)):
            for key, value in zap[i].items():
                if key == "Кол-во родителей":
                    count += value
    print("Количество ребер графа:", count)
    time.sleep(5)
    print("Время ответа кол-ва ребер для массива записей", (datetime.now() - start_time)/10**6)
rebra_massixzapisei()

def sosed_spisokrebra(): #соседи для списка ребер
    a = int(input("Введите номер вершины графа: "))
    mas = []
    start_time = datetime.now()
    for q in range(10**6):
        for i in rebra:
            popl = list(i)
            if a == popl[0] and popl[1] not in mas:
                mas.append(popl[1])
            if a == popl[1] and popl[0] not in mas:
                mas.append(popl[0])
    print("Соседи", mas)
    time.sleep(5)
    print("Время поиска соседей для списка ребер", (datetime.now() - start_time)/10**6)
sosed_spisokrebra()


def tsep_spisokrebra(): #ответ, образует ли заданная последовательность вершин цепь для списка ребер
    alla = input('Введите номера вершин через пробел: ').split()
    start_time = datetime.now()
    for e in range(10**6):
        flag = True
        for w in range(len(alla)-1):
            for i in rebra:
                popl = list(i)
                if (int(alla[w]) == popl[0] and int(alla[w])+1 != popl[1]) or (int(alla[w]) == popl[1] and int(alla[w])+1 != popl[0]):
                    flag = False
                else:
                    flag = True
            if flag == False:
                break
            if not flag:
                break
        if not flag:
            break
    if flag:
        print("Образует")
    else:
        print("Не образует")
    time.sleep(5)
    print("Время ответа возможности цепочки для списка ребер", (datetime.now() - start_time) / 10 ** 6)
tsep_spisokrebra()


def summa_rebra(): #номера вершин для списка ребер
    vel = int(input('Введите число: '))
    start_time = datetime.now()
    ccc = []
    for w in range(10**6):
        for i in range(1, 9):
            count = 0
            for q in range(len(rebra)):
                popl = list(rebra[q])
                if popl[0] == i or popl[1] == i:
                    count += ves[q]
            if count > vel and i not in ccc:
                ccc.append(i)
    print("Номера вершин, сумма весов инцидентных ребер которых больше", vel, ":", ccc)
    time.sleep(5)
    print("Время ответа номеров вершин для списка ребер", (datetime.now() - start_time) / 10 ** 6)
summa_rebra()

def count_rebra(): #Количество ребер для списка ребер
    start_time = datetime.now()
    a = 0
    for i in range(10 ** 6):
        a = len(rebra)
    print("Количество ребер:", a)
    time.sleep(5)
    print("Время нахождения количества ребер для списка ребер:", (datetime.now() - start_time) / 10 ** 6)
count_rebra()

def sosed_matrix(): #нахождение соседей для матрицы смежности
    a = int(input("Введите номер вершины графа: "))
    ko = []
    start_time = datetime.now()
    for i in range(10 ** 6):
        for i in range(len(matrix)):
            if matrix[a - 1][i] != 0 or matrix[i][a - 1] != 0:
                if i+1 not in ko:
                    ko.append(i + 1)
    print("Соседи заданной вершины: ", ko)
    time.sleep(5)
    print("Время нахождения соседей для матрицы смежности", (datetime.now() - start_time) / 10 ** 6)
sosed_matrix()

def tsep_matrix(): #ответ возможности цепочки для матрицы смежности
    rices = input('Введите номера вершин через пробел: ').split()
    start_time = datetime.now()
    flag = "Данная последовательность вершин образует цепь"
    for i in range(10 ** 6):
        for k in range(len(rices) - 1):
            if 0 > int(rices[k]) or int(rices[k]) >= 8:
                flag = "Таких вершин не существует"
                break
            elif matrix[int(rices[k]) - 1][int(rices[k + 1]) - 1] == 0:
                flag = "Данная последовательность вершин НЕ образует цепь"
                break
    print(flag)
    time.sleep(5)
    print("Время ответа возможности цепочки для матрицы смежности", (datetime.now() - start_time) / 10 ** 6)
tsep_matrix()

def count_matrix(): #вершины сумма инц. ребер которых больше введенного числа для матрицы смежности
    alla = int(input('Введите число: '))
    massa = []
    start_time = datetime.now()
    for w in range(10 ** 6):
        for i in range(len(matrix)):
            count = 0
            for j in range(len(matrix)):
                if matrix[i][j] != 0:
                    count += matrix[i][j]
                if matrix[j][i] != 0:
                    count += matrix[j][i]
            if count > alla and i+1 not in massa:
                massa.append(i + 1)
    print("Номера вершин, сумма весов инцидентных ребер которых больше заданного числа", massa)
    time.sleep(5)
    print("Время ответа номеров вершин для матрицы смежности", (datetime.now() - start_time) / 10 ** 6)
count_matrix()

def rebra_matrix(): #количество ребер для матрицы смежности
    start_time = datetime.now()
    count = 0
    for w in range(10 ** 6):
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != 0:
                    count += 1
    print("Количество ребер для матрицы смежности равно", count)
    time.sleep(5)
    print("Время нахождения количества ребер для матрицы смежности:", (datetime.now() - start_time) / 10 ** 6)
rebra_matrix()

def alina7(): #размер каждого вида записи
    s = sys.getsizeof(matrix)
    print("Размер матрицы смежности:", s, "байт")
    s = sys.getsizeof(rebra)
    print("Размер списка ребер:", s, "байт")
    s = sys.getsizeof(zap)
    print("Размер массива записей:", s, "байт")
alina7()
