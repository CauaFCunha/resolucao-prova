import sympy as sp

# Questao 1
A = sp.Matrix([[1, 0], [2, 1]])
B = sp.Matrix([[0, 2], [6, 1]])
resultado1 = 2 * A + 3 * B
print("Questao 1:")
print(resultado1)

# Questao 2
matriz = sp.Matrix(3, 3, sp.symbols("a0:9"))
resultado2 = sp.simplify(sp.det(3 * matriz) - 27 * sp.det(matriz)) == 0
print("Questao 2:")
if resultado2:
    print("Alternativa A")

# Questao 3
detA = -2
detB = 4
alternativas = {
    "A": detA**3 * detB**2,
    "B": sp.Rational(1, detA) * detB,
    "C": detA**4 * sp.Rational(1, detB**2),
    "D": 3**3 * detA,
    "E": detA**2 * detB,
}
print("Questao 3:")
print(alternativas)
for letra in alternativas:
    if alternativas[letra] == 1:
        print("Alternativa", letra)

# Questao 4a
simetrica = sp.Matrix([[2, 5], [5, -3]])
print("Questao 4a:")
print(simetrica)
print(simetrica == simetrica.T)

# Questao 4b
M = sp.Matrix([[1, 2, 3], [4, 5, 6]])
N = sp.Matrix([[7, 8, 9], [10, 11, 12]])
resultado4 = sp.simplify((M + N).T - (M.T + N.T)) == sp.zeros(3, 2)
print("Questao 4b:")
print(resultado4)

