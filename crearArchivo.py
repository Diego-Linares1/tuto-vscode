def crearArchivo(nombre, apellido):
    f = open('Archivo1.txt', 'a')
    f.write(nombre + ' ' + apellido)
    f.close()
    
crearArchivo('Diego', 'Linares')