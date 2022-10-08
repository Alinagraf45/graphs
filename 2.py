#импорт библиотек
import igraph
import networkx as nx
from matplotlib import pyplot as plt
import random
import time

matrix = [[0, 2, 3, 4, 0],
          [2, 0, 1, 0, 2],
          [3, 1, 0, 1, 5],
          [4, 0, 1, 0, 0],
          [0, 2, 5, 0, 0]]
name = ["x0", "x1", "x2", "x3", "x4"]

def alina(): #вывод матрицы смежности
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 and j == 0:
                for k in range(len(name)):
                    print(name[k], end=" ")
                print()
            print(matrix[i][j], end="  ")
        print(name[i], end=" ")
        print()
alina()

def alina2(): #вывод графического представления
    #построение списка ребер
    rebra_grafic = []
    ves = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                rebra_grafic += [tuple([i, j])]
                ves.append(matrix[i][j])
    G = igraph.Graph(directed = False) #создание ориентированного графа
    G.add_vertices(len(matrix)) #добавление вершин в граф
    G.vs["label"] = name  #подписи вершин
    G.add_edges(rebra_grafic) #добавление ребер в граф
    G.es["weight"] = ves #задание весов ребрам
    G.es["label"] = ves #подписи ребер
    G.es["curved"] = False
    igraph.plot(G, bbox=(300, 300), vertex_label_color='black', vertex_label_size=10, vertex_size=20, vertex_color='white')
alina2()

def prima():
    free_verx = [0, 1, 2, 3, 4] #список свободных вершин
    with_which = [] #кортеж из связанных ребер
    rebra_ispolzovan = [] #ребра, которые нельзя использовать в циклах
    vesa = [] #веса этих ребер
    for e in range(len(free_verx)):
        ww = [] #временный кортеж, которому присваивается текущее значение ребер в цикле
        c_min = 10**6 #минимальный вес ребер после прохождения одной итерации главного цикла (по свободным вершинам)
        ves = 10**6 #вес при каждой итерации
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in free_verx:
                    if matrix[i][j] != 0 and (i == e):
                        if matrix[i][j] <= ves:
                            ves = matrix[i][j]
                            ww = [tuple([i, j])]
            if c_min > ves:
                c_min = ves
        vesa.append(c_min) #добавление в список весов текущего веса двух вершин с минимальным весом
        free_verx.remove(e) #удаление вершины из списка свободных вершин
        rebra_ispolzovan.append(e) #использованные ребра
        with_which += ww #итоговый кортеж вершин с ребрами минимальных весов
    print('Результат алгоритма Прима:', with_which)

    G = igraph.Graph(directed=False)  # создание ориентированного графа
    G.add_vertices(len(rebra_ispolzovan))  # добавление вершин в граф
    G.vs["label"] = name  # подписи вершин
    G.add_edges(with_which)  # добавление ребер в граф
    G.es["weight"] = vesa  # задание весов ребрам
    G.es["label"] = vesa  # подписи ребер
    G.es["curved"] = False
    igraph.plot(G, bbox=(300, 300), vertex_label_color='black', vertex_label_size=10, vertex_size=20,
                vertex_color='white')
prima()
#Правильная шестиугольная решетка
def reshetka():
    M = 6
    matrix1 = []
    for i in range(M**2):
        matrix1.append([0] * M**2)
    versiha = [i for i in range(len(matrix1))]
    #алгоритм заполнения матрицы зачениями
    for i in range(len(versiha)):
        r = versiha[i] // M
        c = versiha[i] % M
        if (r % 4 == 0 and c % 2 == 1) or (r % 4 == 2 and c % 2 == 0):
            if r > 0:
                matrix1[versiha[i]][versiha[i] - M] = matrix1[versiha[i] - M][versiha[i]] = 1
            if r < (M - 1) and c < (M - 1):
                matrix1[versiha[i]][versiha[i] + M + 1] = matrix1[versiha[i] + M + 1][versiha[i]] = 1
            if r < (M - 1) and c > 0:
                matrix1[versiha[i]][versiha[i] + M - 1] = matrix1[versiha[i] + M - 1][versiha[i]] = 1
    name = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x20', 'x21', 'x22', 'x23', 'x24', 'x25', 'x26', 'x27', 'x28', 'x29', 'x30', 'x31', 'x32', 'x33', 'x34', 'x35', 'x36' ]
    #вывод матрицы смежности ДО удаления
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            if i == 0 and j == 0:
                print()
            print(matrix1[i][j], end="  ")
        print(name[i], end=" ")
        print()
    count = 0
    ver = []
    #удаление лишних вершин
    for i in range(len(matrix1)-1, -1, -1):
        for j in range(len(matrix1)-1, -1, -1):
            count += matrix1[i][j]
        if count < 2:
            row = len(matrix1)
            for k in range(row):
                _ = matrix1[k].pop(i)
            _ = matrix1.pop(i)
        else:
            ver.append(i)
        count = 0
    # вывод матрицы смежности ПОСЛЕ удаления
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            if i == 0 and j == 0:
                print()
            print(matrix1[i][j], end="  ")
        print(name[i], end=" ")
        print()
    rebra = []
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            if matrix1[i][j] != 0:
                if ver[i] != ver[j]:
                    rebra.append([ver[i], ver[j], matrix1[i][j]])
                else:
                    rebra.append([ver[j], ver[i], matrix1[i][j]])
    # Отрисовка графа по списку ребер с весами
    DG = nx.Graph()
    DG.add_nodes_from(ver)
    DG.add_weighted_edges_from(rebra)
    pos = nx.planar_layout(DG)
    nx.draw(DG, pos=pos, node_color='#B0C4DE', with_labels=True, node_size=600)
    plt.show()
reshetka()

vrema = []
razmer = []
#ГРАФИК ВРЕМЕНИ ВЫПОЛНЕНИЯ ОТ КОЛЛИЧЕСТВА РЕБЕР - ДОП ЗАДАНИЕ
def alinatime():
    for qwerty in range(4, 15):
        M = qwerty
        matrix1 = []
        for i in range(M ** 2):
            matrix1.append([0] * M ** 2)
        versiha = [i for i in range(len(matrix1))]
        # алгоритм заполнения матрицы смежности графа
        for i in range(len(versiha)):
            r = versiha[i] // M
            c = versiha[i] % M
            if (r % 4 == 0 and c % 2 == 1) or (r % 4 == 2 and c % 2 == 0):
                if r > 0:
                    matrix1[versiha[i]][versiha[i] - M] = matrix1[versiha[i] - M][versiha[i]] = 1
                if r < (M - 1) and c < (M - 1):
                    matrix1[versiha[i]][versiha[i] + M + 1] = matrix1[versiha[i] + M + 1][versiha[i]] = 1
                if r < (M - 1) and c > 0:
                    matrix1[versiha[i]][versiha[i] + M - 1] = matrix1[versiha[i] + M - 1][versiha[i]] = 1
        count = 0
        # удаление лишних вершин
        for i in range(len(matrix1) - 1, -1, -1):
            for j in range(len(matrix1) - 1, -1, -1):
                count += matrix1[i][j]
            if count < 2:
                row = len(matrix1)
                for k in range(row):
                    _ = matrix1[k].pop(i)
                _ = matrix1.pop(i)
            count = 0
        for i in range(len(matrix1)):
            for j in range(len(matrix1)):
                if matrix1[i][j] != 0:
                    matrix1[i][j] = random.randint(1, 99)
        alina = []
        for i in range(len(matrix1)):
            alina.append(i)
        def prima():
            free_verx = alina  # список свободных вершин
            with_which = []  # кортеж из связанных ребер
            vesa = []  # веса этих ребер
            for e in range(len(free_verx)):
                ww = []  # временный кортеж, которому присваивается текущее значение ребер в цикле
                c_min = 10 ** 6  # минимальный вес ребер после прохождения одной итерации главного цикла (по свободным вершинам)
                ves = 10 ** 6  # вес при каждой итерации
                for i in range(len(matrix1)):
                    for j in range(len(matrix1[i])):
                        if i in free_verx:
                            if matrix1[i][j] != 0 and (i == e):
                                if matrix1[i][j] <= ves:
                                    ves = matrix1[i][j]
                                    ww = [tuple([i, j])]
                    if c_min > ves:
                        c_min = ves
                vesa.append(c_min)  # добавление в список весов текущего веса двух вершин с минимальным весом
                free_verx.remove(e)  # удаление вершины из списка свободных вершин
                with_which += ww  # итоговый кортеж вершин с ребрами минимальных весов
        #print('Результат алгоритма Прима:', with_which)
        start_time = time.time()
        for k in range(10 ** 6):
            prima()
        average_time = time.time() - start_time
        vrema.append(average_time / 10 ** 6)
        razmer.append(M)
    # Визуализация графика
    plt.figure(figsize=(12, 5))
    plt.plot(razmer, vrema)
    plt.xlabel("Количество вершин")
    plt.ylabel("Время")
    plt.show()

alinatime()


