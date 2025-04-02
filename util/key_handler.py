import os

def saveKey(fileName, encoded):
    keyFileName = fileName + "-key.txt"
    
    f = open(keyFileName, "w")
    
    f.write(encoded)
    print(f"Chave do arquivo salva em {keyFileName}")
    f.close()
    

def validateKey(fileName, encoded):
    
    keyFileName = fileName + "-key.txt"
    
    if not os.path.exists(keyFileName):
        print ("ERRO: Chave ou arquivo inexistente")
        return
    
    f = open(keyFileName, 'r')
    
    key = (f.read())
    
    if key == encoded:
        print("Arquivo Legitimo!")
        return True
    else:
        print("Arquivo Alterado!")
        return False
    