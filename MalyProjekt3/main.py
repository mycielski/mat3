import math

from sympy import *


# plt.figure(figsize=(8, 8))
# plt.axis('equal')
# plt.fill(x, y)
# plt.show()

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


# Zadanie 2
# Obliczyć objętość równoległościanu zadanego współrzędnymi jego wierzchołków
def pole_równoległościanu(*points):
    # Zakładamy, że argumeny podane do funkcji to cztery punkty, z których utworzyć można trzy prostopadłe odcinki.
    # Na rysunku poniżej poprawną czwórką argumentów byłyby punkty c, a, d, g:
    #      e---------f
    #     /|        /|
    #    / |       / |
    #   a--|------b  |
    #   |  g------|--h
    #   | /       | /
    #   |/        |/
    #   c---------d

    for point in points:
        for coordinate in point.coordinates:
            if isinstance(coordinate, (int, float)):
                print(coordinate)
    return


print(pole_równoległoboku(Point3D(0, 0, 0), Point3D(5, 1, 0), Point3D(10, 1, 0)))
a = symbols('a')
pole_równoległościanu(Point3D(1, a, 3))
