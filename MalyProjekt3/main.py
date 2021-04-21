# Wykonanie: Tomasz Mycielski (304248)

from numpy import radians
from sympy import *
import threading

# deklaracja zmiennych SymPy, które będę wykorzystywał w zadaniach
alfa, a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, p = symbols(
"alfa, a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, p")

# Zadanie 1
# Obliczyć pole równoległoboku zadanego współrzędnymi jego wierzchołków
def zadanie1():
    def pole_równoległoboku(*points):
        # Zakładamy, że wierzchołki równoległoboku zostały oznaczone w poprawnej kolejności:
        #    d---------c
        #   /         /
        #  a---------b
        # W przypadku z tego obrazka poprawne byłoby podanie punktów a, b, d (pierwszy jest punkt będący wierzchołkiem kąta stworzonego przez sąsiadujące boki)
        matrices = []
        matrices.append(
            Matrix([
                [points[1].coordinates[1] - points[0].coordinates[1],
                 points[1].coordinates[2] - points[0].coordinates[2]],
                [points[2].coordinates[1] - points[0].coordinates[1],
                 points[2].coordinates[2] - points[0].coordinates[2]]
            ])
        )
        matrices.append(
            Matrix([
                [points[1].coordinates[0] - points[0].coordinates[0],
                 points[1].coordinates[2] - points[0].coordinates[2]],
                [points[1].coordinates[1] - points[0].coordinates[1],
                 points[1].coordinates[2] - points[0].coordinates[2]]
            ])
        )
        matrices.append(
            Matrix([
                [points[1].coordinates[0] - points[0].coordinates[0],
                 points[1].coordinates[1] - points[0].coordinates[1]],
                [points[2].coordinates[0] - points[0].coordinates[0],
                 points[2].coordinates[1] - points[0].coordinates[1]]
            ])
        )
        vector = [matrices[0].det(), -1 * matrices[1].det(), matrices[2].det()]
        output = 0
        for i in range(len(vector)):
            vector[i] = vector[i] ** 2
            output = simplify(output + vector[i])
        return simplify(sqrt(output))

    # driver code
    print("ZADANIE 1:")
    print(pole_równoległoboku(Point3D(a1, a2, a3), Point3D(b1, b2, b3), Point3D(c1, c2, c3)))


# Zadanie 2
# Obliczyć objętość równoległościanu zadanego współrzędnymi jego wierzchołków
def zadanie2():
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
        return simplify(matrix.det())

    # driver code
    print("ZADANIE 2:")
    print(pole_równoległościanu(Point3D(a1, a2, a3), Point3D(b1, b2, b3), Point3D(c1, c2, c3), Point3D(d1, d2, d3)))


# Zadanie 3
# Obrócić trójkąt o podanych wierzchołkach o zadany kąt (w stopniach) przeciwnie do ruchu wskazóweg zegara, wokół początku układu współrzędnych.
def zadanie3():
    def obróć_o_kąt(angle, *points):
        if angle.is_number:
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
                    simplify(vector[0, 0]),
                    simplify(vector[1, 0])
                )
            )
        return list

    # driver code
    print("ZADANIE 3:")
    print(obróć_o_kąt(alfa, Point2D(a1, a2), Point2D(b1, b2), Point2D(c1, c2)))


# Zadanie 4
# Powiększyć kwadrat jednostkowy (kwadrat, którego boki mają długość jeden) trzykrotnie względem osi OX i dwukrotnie względem osi OY
def zadanie4():
    def powiększyć_kwadrat(ox, oy, *points):
        matrix = Matrix([
            [ox, 0],
            [0, oy]
        ])
        vectors = []
        for point in points:
            M = Matrix([
                point.coordinates[0],
                point.coordinates[1]
            ])
            vectors.append(
                M
            )

        for i in range(len(vectors)):
            vectors[i] = (matrix * vectors[i])

        list = []
        for vector in vectors:
            list.append(
                Point2D(
                    simplify(vector[0, 0]),
                    simplify(vector[1, 0])
                )
            )
        return list

    # driver code
    print("ZADANIE 4:")
    print(powiększyć_kwadrat(3, 2, Point2D(0, 0), Point2D(1, 0), Point2D(1, 1), Point2D(0, 1)))


# Zadanie 5
# Zadany odcinek obrócić o podany kąt \alpha oraz powiększyć o p%
def zadanie5():
    def odcinek_obrócić_i_powiększyć(angle, p, *points):
        if angle.is_number:
            angle = radians(angle)
        p = 1 + p / 100
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
        for i in range(len(vectors)):
            vectors[i] = matrix * vectors[i]
        list = []
        for vector in vectors:
            list.append(
                Point2D(
                    vector[0, 0] * p,
                    vector[1, 0] * p
                )
            )
        return list

    # driver code
    print("ZADANIE 5:")
    print(odcinek_obrócić_i_powiększyć(alfa, p, Point2D(a1, a2), Point2D(b1, b2)))

# driver code:
zadanie1()
zadanie2()
zadanie3()
zadanie4()
zadanie5()