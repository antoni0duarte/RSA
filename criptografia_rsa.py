import numpy as np
import random

# GCD // MDC
def mdc(n1,n2):
    r = 0
    while r != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
        return n1

# RSA_values // Entrada de valores RSA
n1 = int(input('Entre com um número primo:'))
n2 = int(input('Entre com um número primo diferente do anterior:'))

# Totient_function // Função Totiente
phi = (n1 - 1) * (n2 -1) # Coprime integers // co-primos

# Public_Key // Calculo das Chaves Púlicas
e = random.randint(1, phi)
if mdc(e,phi) != 1:
    e = random.randint(1,phi)



####################### in construction #######################
