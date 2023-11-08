from math import sqrt

# x^2 + 2x - 3
#a = 1
#b = 2
#c = -3

a = int(input("vlozte a:"))
b = int(input("vlozte b:"))
c = int(input("vlozte c:"))

def solve_quadratic_equation(a, b, c):
    print(f"Rovnice: {a}x² {b}x {c}")

    D = b * b - 4 * a * c

    if D == 0:
        print("Jedno reseni:", -b / (2 * a))
    elif D > 0:
        print("Dve reseni,",
              "prvni: ", (-b + sqrt(D)) / (2 * a),
              ", druhe:", (-b - sqrt(D)) / (2 * a)
              )
    else:
        print("Zadne reseni")

    if a == 0
        print("Dve reseni,",
            "prvni:", (-b + sqrt(D)),
            ", druhe:", (-b -sqrt(D))
            )


solve_quadratic_equation(a, b, c)

solve_quadratic_equation(a, b, c)

for a in range(2):
    for b in range(2):
        for c in range(2):
            solve_quadratic_equation(a, b, c)

# Vytvorili jsme funkci a pri testovani narazili problem
# TODO: Opravit problem s delenim nulou (co kdyz plati a == 0)?
# TODO: Opravdu pekny vypis rovnice, napr. -9x² - 17 = 0 (pro a = -9, b = 0, c = -17)