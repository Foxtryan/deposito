''' DOC '''
import hashlib

def ash(binary):
    """ Criptografa a senha"""
    hashed = hashlib.sha384(binary)
    return hashed.hexdigest()

def toBinary(string):
    ''' Converte para byte string'''
    return bytes(string, 'UTF-8')

if __name__ == '__main__':
    crip = input("O que criptografar?\n>>> ")
    converter = toBinary(crip)
    criarHash = ash(converter)
    print(criarHash)
    
