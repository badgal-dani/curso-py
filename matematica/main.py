# Testando a eq_quadratica
import eq_quadratica as eq

a = float(input("Informe o valor de 'a' da equação quadrática: "))
b = float(input("Informe o valor de 'b' da equação quadrática: "))
c = float(input("Informe o valor de 'c' da equação quadrática: "))

res = eq.raiz_quad(a, b, c)
print(res)

