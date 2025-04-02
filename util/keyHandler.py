import os

def saveKey(fileName, encoded):
    keyFileName = fileName + "-key.bin"
    
    f = open(keyFileName, "wb")
    
    f.write(encoded.encode())
    print(f"Chave do arquivo salva em {keyFileName}")
    f.close()
    

def validateKey(fileName, encoded):
    
    keyFileName = fileName + "-key.bin"
    
    if not os.path.exists(keyFileName):
        print ("ERRO: Chave ou arquivo inexistente")
        return
    
    f = open(keyFileName, 'rb')
    
    key = (f.read().decode())
    
    if key == encoded:
        print("Arquivo Legitimo!")
        return True
    else:
        print("Arquivo Alterado!")
        return False
    