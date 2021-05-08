# MAT3 Mały Projekt 4
# Tomasz Mycielski (304248)

from sympy import *


def metoda_najmniejszych_kwadratow(polynomial_degree, *points):
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
        auxiliary = Matrix([
            []
        ])
        for i in range(polynomial_degree + 1):
            auxiliary = auxiliary.row_join(Matrix([
                [point[0] ** i]
            ]))
        X = X.col_join(auxiliary)

    XT = X.T
    XTX = XT * X
    if XTX.det() == 0:
        print("Macierz X^T * X ma wyznacznik równy 0, nie jest więc odwracalna.")
        return
    B = XTX ** -1 * XT * Y
    x, y = symbols("x, y")
    polynomial_formula_matrix = Matrix([
        []
    ])
    for i in range(polynomial_degree + 1):
        polynomial_formula_matrix = polynomial_formula_matrix.row_join(Matrix([
            [x ** i]
        ]))
    polynomial_formula_matrix = polynomial_formula_matrix * B
    print("y = " + str(simplify(polynomial_formula_matrix[0, 0])) + "\n")
    # for plotting to work the Python interpreter must have matplotlib available for use
    # otherwise it will use a TextBackend library which sucks and does not work whatsoever
    p1 = plot(polynomial_formula_matrix[0, 0], show=True)


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

print("Zadanie 3")
metoda_najmniejszych_kwadratow(2,
                               Point2D(1, 7),
                               Point2D(2, 10),
                               Point2D(3, 11),
                               Point2D(4, 24),
                               Point2D(5, 35),
                               Point2D(6, 46),
                               Point2D(7, 55)
                               )

print("Zadanie 4")
metoda_najmniejszych_kwadratow(3,
                               Point2D(1, 2.54968),
                               Point2D(2, 2.57332),
                               Point2D(3, 3.77028),
                               Point2D(4, 4.50018),
                               Point2D(5, 6.23465)
                               )
