'''
Autor: Antonio Lucas de Oliveira Duarte Bezerra
Projeto implementado: Cifra de César    
Descrição do algoritmo: Um deslocamento de 15 caracteres na tabela ASCII.
Descrição de como compilar/executar o programa: 
- Abra o arquivo na ide
- Para criptografar utilize: encripta('Mensagem')
- Para descriptografar utilize: decripta('Código criptografado')
'''
def encripta(msg):
    s = ''
    for c in msg: s = s + chr(ord(c) + 15)
    return s
def decripta(msg):
    s = ''
    for c in msg: s = s + chr(ord(c) - 15)
    return s
