def cifrado_cesar(mensaje, clave):
    cifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            nuevo_caracter = ord(caracter) + clave
            if caracter.isupper():
                if nuevo_caracter > ord("Z"):
                    nuevo_caracter -= 26
                elif nuevo_caracter < ord("A"):
                    nuevo_caracter += 26
                cifrado += chr(nuevo_caracter)
            else:
                if nuevo_caracter > ord("z"):
                    nuevo_caracter -= 26
                elif nuevo_caracter < ord("a"):
                    nuevo_caracter += 26
                cifrado += chr(nuevo_caracter)
        else:
            cifrado += caracter
    return cifrado

def descifrado_cesar(cifrado, clave):
    mensaje = ""
    for caracter in cifrado:
        if caracter.isalpha():
            nuevo_caracter = ord(caracter) - clave
            if caracter.isupper():
                if nuevo_caracter > ord("Z"):
                    nuevo_caracter -= 26
                elif nuevo_caracter < ord("A"):
                    nuevo_caracter += 26
                mensaje += chr(nuevo_caracter)
            else:
                if nuevo_caracter > ord("z"):
                    nuevo_caracter -= 26
                elif nuevo_caracter < ord("a"):
                    nuevo_caracter += 26
                mensaje += chr(nuevo_caracter)
        else:
            mensaje += caracter
    return mensaje

mensaje = "Hola, mundo!"
clave = 3
cifrado = cifrado_cesar(mensaje, clave)
print("Mensaje original:", mensaje)
print("Mensaje cifrado:", cifrado)
descifrado = descifrado_cesar(cifrado, clave)
print("Mensaje descifrado:", descifrado)