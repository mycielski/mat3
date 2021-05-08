# MAT3 Mały Projekt 4
# Tomasz Mycielski (304248)

from sympy import *


def metoda_najmniejszych_kwadratow(deg, *points):
    Y = Matrix([
        []
    ])
    X = Matrix([
        []
    ])
    for point in points:
        Y = Y.col_join(Matrix([
            [point[1]]
        ]))
        X = X.col_join(Matrix([
            [1, point[0]]
        ]))
    XT = X.T
    XTX = XT * X
    if XTX.det() == 0:
        print("Macierz X^T * X ma wyznacznik równy 0, nie jest więc odwracalna.")
        return
    B = XTX ** -1 * XT * Y
    x, y = symbols("x, y")
    line_matrix = Matrix([
        [1, x]
    ]) * B
    print("y = " + str(simplify(line_matrix[0, 0])))
    # for plotting to work the Python interpreter must have matplotlib available for use
    # otherwise it will use a TextBackend library which sucks and does not work whatsoever
    # p1 = plot(line_matrix[0, 0], show=True)


print("Zadanie 1")
metoda_najmniejszych_kwadratow(1,
                               Point2D(0, 4.43),
                               Point2D(3, 6.43),
                               Point2D(6, 8.71),
                               Point2D(9, 9.08),
                               Point2D(12, 11.7)
                               )

print("Zadanie 2")
metoda_najmniejszych_kwadratow(1,
                               Point2D(1, 18),
                               Point2D(2, 16),
                               Point2D(3, 13),
                               Point2D(4, 11),
                               Point2D(5, 9),
                               Point2D(6, 7),
                               Point2D(7, 5),
                               Point2D(8, 4),
                               Point2D(9, 1),
                               Point2D(10, 1)
                               )
