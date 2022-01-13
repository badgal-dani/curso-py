# Crie um programa em Python que calcule as raizes reais de uma 
# equação do segundo grau. Ax^2 +Bx + C = 0 x1 e x2
import math


def raiz_quad(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        r_delta = math.sqrt(delta)
        x1 = (-b + r_delta) / (2 * a)
        x2 = (-b - r_delta) / (2 * a)
        return f"\nA equação possui duas raízes reais diferentes:\nx' = {x1} e x'' = {x2}\n"
    elif delta == 0:
        x = -b / (2 * a)
        return f"\nA equação possui apenas uma raiz real:\nx = {x}\n"
    else:
        return f"\nA equação não possui valores reais.\n"
