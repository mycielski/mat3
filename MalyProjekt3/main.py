# Wykonanie: Tomasz Mycielski (304248)

import math

from numpy import radians
from sympy import *


# Zadanie 1
# Obliczyć pole równoległoboku zadanego współrzędnymi jego wierzchołków

# funkcja zwracająca pole równoległoboku dla zadanych jego wierzchołków
def pole_równoległoboku(*points):
    # Zakładamy, że wierzchołki równoległoboku zostały oznaczone w poprawnej kolejności:
    #    p4--------p3
    #   /         /
    # p1--------p2

    vectors = [[], []]
    for i in range(2):
        for j in range(3):
            vectors[i].append(points[i + 1].coordinates[j] - points[0].coordinates[j])
    matrices = []
    matrices.append(Matrix([
        [vectors[0][1], vectors[0][2]],
        [vectors[1][1], vectors[1][2]]
    ]))
    matrices.append(Matrix([
        [vectors[0][0], vectors[0][2]],
        [vectors[1][0], vectors[1][2]]
    ]))
    matrices.append(Matrix([
        [vectors[0][0], vectors[0][1]],
        [vectors[1][0], vectors[1][1]]
    ]))
    uxv = [matrices[0].det(), -1 * matrices[1].det(), matrices[2].det()]
    vector_length = 0
    for coordinate in uxv:
        vector_length = vector_length + pow(coordinate, 2)
    return math.sqrt(vector_length)


# driver code
print(pole_równoległoboku(Point3D(0, 0, 0), Point3D(5, 1, 0), Point3D(10, 1, 0)))


# Zadanie 2
# Obliczyć objętość równoległościanu zadanego współrzędnymi jego wierzchołków
def pole_równoległościanu(*points):
    # Zakładamy, że argumeny podane do funkcji to cztery punkty, z których utworzyć można trzy prostopadłe odcinki.
    # Na rysunku poniżej poprawną czwórką argumentów byłyby punkty c, a, d, g (jako pierwszy podany musi być punkt, z którym sąsiadują pozostałe punkty):
    #      e---------f
    #     /|        /|
    #    / |       / |
    #   a--|------b  |
    #   |  g------|--h
    #   | /       | /
    #   |/        |/
    #   c---------d

    matrix = Matrix([
        []
    ])
    for i in range(1, 4):
        auxiliary = Matrix([
            []
        ])
        for j in range(3):
            cell = simplify(
                points[i][j] - points[0][j]
            )
            cell = Matrix([[cell]])
            auxiliary = auxiliary.col_join(cell)
        auxiliary = auxiliary.T
        matrix = matrix.col_join(auxiliary)
    return matrix.det()


# driver code
print(pole_równoległościanu(Point3D(1, 1, 3), Point3D(3, 5, 7), Point3D(2, 4, 6), Point3D(10, 20, 30)))


# Zadanie 3
# Obrócić trójkąt o podanych wierzchołkach o zadany kąt (w stopniach) przeciwnie do ruchu wskazóweg zegara, wokół początku układu współrzędnych.
def obróć_o_kąt(angle, *points):
    angle = radians(angle)
    matrix = Matrix([
        [cos(angle), -1 * sin(angle)],
        [sin(angle), cos(angle)]
    ])
    vectors = []
    for point in points:
        vectors.append(
            Matrix([
                point.coordinates[0],
                point.coordinates[1]
            ])
        )
    list = []
    for vector in vectors:
        vectors.append(matrix * vector)
        vectors.pop(0)
    for vector in vectors:
        list.append(
            Point2D(
                vector[0,0],
                vector[1,0]
            )
        )
    return list

print(obróć_o_kąt(60, Point2D(4, 9), Point2D(3, 8), Point2D(6, 5)))


# Zadanie 4
# Powiększyć kwadrat jednostkowy (kwadrat, którego boki mają długość jeden) trzykrotnie względem osi OX i dwukrotnie względem osi OY
def powiększyć_kwadrat(ox, oy):
