import numpy as np
import random

#MDC
def mdc(x,y):
    r = None
    while r != 0:
        r = x % y
        x = y
        y = r
    return x


#Algorítmo de Euclides Estendido
def euclid_est(x1,x2):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

if temp_phi == 1:
    return d + phi

#Teste de primariedade
def primo(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2,2):
        if num % n == 0:
            return False
    return True

#Entrada de valores RSA
n1 = int(input('Entre com um número primo:'))
n2 = int(input('Entre com um número primo diferente do anterior:'))

#Validação do n1 e n2


#Função Totiente
phi = (n1 - 1) * (n2 - 1) # Co-primos

#Calculo das Chaves Púlicas
e = random.randint(1, phi) # 'e' aleatório na faixa 1 < e < phi
m = mdc(e,phi)
while m != 1:
    e = random.randint(1, phi)
    m = mdc(e,phi)
    
    
    
   ''' 
#FAIL_PART   
import numpy as np
#RSA_valores
p = 17
q = 41
n = p * q 
phi = (p - 1) * (q - 1) 
e = 13
d = 197

def esconde(msg):
    msg =(input('Digite sua mensagem:'))
    for i in range (0, len(msg)):
        v1 = np.array((ord(msg[i])** e) % n )
        print(v1)
'''
####################### in construction #######################
