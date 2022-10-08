#импорт библиотек
import networkx as nx
import graph
from matplotlib import pyplot as plt
import random
import time

razmer = []

def alg():
    k = 1
    alla = 0
    zadanie = []
    zadanie4 = []
    for N in range(10, 110, 10):
        for asaasa in range(10):
            matrix = [[0]*N]
            for i in range(N-1):
                matrix.append([0]*N)

            matrix[0][1] = 1
            matrix[1][0] = 1

            ti = 0
            sum = 0.0

            alpha = 0
            qwerty = [0, 1]
            count = []
            for i in range(2, N):
                if i <= N//2 + 1:
                    qwerty.append(i) #все возможныe степени от 1 до N
                for j in range(0, i+1):
                    ti = j**k
                    sum += ti
                alpha = 1/sum
                veroiat = []
                verx = []
                chet = 0
                for q in range(i, 0, -1):
                    pi = alpha * q**k #вероятность выбора для 0 вершины, потом для 1-вой и тд
                    veroiat.append(pi)
                    verx.append(chet)
                    chet +=1
                date = random.choices(verx, weights = veroiat)
                a = date[0]
                matrix[a][i] = 1
                matrix[i][a] = 1
            #print(veroiat)
            #print(verx)
            count = 0
            qqq = []  # список степеней всех вершин для подсчета частоты каждой
            for a in range(0, N):
                ko = [] #список соседей для вершины a
                for i in range(len(matrix)):
                    if matrix[a - 1][i] != 0 or matrix[i][a - 1] != 0:
                        if i + 1 not in ko:
                            count += 1
                            ko.append(i + 1)
                eke = len(ko)
                qqq.append(eke)
            itog = []
            for i in qwerty:
                count = 0
                for j in range(len(qqq)):
                    if qqq[j] == i:
                        count += 1
                itog.append(count)

            '''plt.figure()
            plt.tick_params(axis='x', rotation=0)  # поворот подписи по оси х на 90 градусов
            plt.bar(qwerty, itog)
            plt.show()  # вывод гистограммы'''

            name = []
            for i in range(len(matrix)):
                q = 'x' + str(i)
                name.append(q)
            z = 0
            # построение списка ребер
            rebra_grafic = []
            ves = []
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] != 0:
                        rebra_grafic += [tuple([i, j])]
                        ves.append(matrix[i][j])

            z = len(rebra_grafic)
            G = igraph.Graph(directed=False)  # создание неориентированного графа
            G.add_vertices(len(matrix))  # добавление вершин в граф
            G.vs["label"] = name  # подписи вершин
            G.add_edges(rebra_grafic)  # добавление ребер в граф
            G.es["weight"] = ves  # задание весов ребрам
            G.es["label"] = ves  # подписи ребер

            alla += G.diameter(directed=True, unconn=True, weights=None) #диаметр графа
        zadanie.append(alla//10)
        zadanie4.append(N)

    plt.plot(zadanie, zadanie4)
    plt.title('График зависимости среднего диаметра \n от количества вершин при k= ' + str(k))
    plt.ylabel('Количество вершин')
    plt.xlabel('Средний диаметр')
    plt.show()



alg()
#график по всем возможным степеням от 1 до N по оси х и их кол-ву
name = []
def alina(): #вывод матрицы смежности
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 and j == 0:
                for k in range(len(matrix)):
                    print('x'+ str(k), end=" ")
                print()
            print(matrix[i][j], end="  ")
        print('x'+ str(i), end=" ")
        q = 'x'+ str(i)
        name.append(q)
        print()
z = 0
def alina2(): #вывод графического представления
    #построение списка ребер
    rebra_grafic = []
    ves = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                rebra_grafic += [tuple([i, j])]
                ves.append(matrix[i][j])
    z = len(rebra_grafic)
    G = igraph.Graph(directed = False) #создание неориентированного графа
    G.add_vertices(len(matrix)) #добавление вершин в граф
    G.vs["label"] = name  #подписи вершин
    G.add_edges(rebra_grafic) #добавление ребер в граф
    G.es["weight"] = ves #задание весов ребрам
    G.es["label"] = ves #подписи ребер
    G.es["curved"] = False
    igraph.plot(G, bbox=(300, 300), vertex_label_color='black', vertex_label_size=10, vertex_size=20, vertex_color='white')

