def encripta(msg):
    s = ''
    for c in msg: s = s + chr(ord(c) + 15)
    return s
def decripta(msg):
    s = ''
    for c in msg: s = s + chr(ord(c) - 15)
    return s
