import hashlib

def sha256 (text):
    
    encoded_str = text.encode()

    
    hash_obj = hashlib.sha256(encoded_str)

    hexa_value = hash_obj.hexdigest()

    return hexa_value

def H(t1,t2):
    id = t1
    y = t2
    x = 0       

    while True :
        
        print('\n X = ',x ,'\n X apres le hashage est : ',sha256( str(x) ))
        h = sha256( id + str(x) )
        
        if h <= y :
            print('la valeur de H apres le hashage : ',sha256(id + str(x)) )
            return x
        
        x += 1
        
id = "GhomriAnis"
y = "03b16d10cc11e27bd8d4d1ce91bc725665ddbaa6ca2498ef38a88a58ad48cdb4"

x = H(id , y)