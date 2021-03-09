import hashlib

def shaone (text):

    encoded_str = text.encode()

    hash_obj = hashlib.sha1(encoded_str)

    hexa_value = hash_obj.hexdigest()

    return hexa_value

def H(t1,t2):
    id = t1
    y = t2
    x = 0  

    while True :
        
        print('\nX = ',x ,'\nX apres le hashage : ',shaone( str(x) ))
        h = shaone( id + str(x) )
        
        if h <= y :
            print('la valeur de H apres le hashage : ',shaone(id + str(x)) )
            return x
        
        x += 1
        
id ="GhomriAnis"
y = "03b1663dda6549a0939ffdd712a852e0d4234e6b"

x = H(id , y)
