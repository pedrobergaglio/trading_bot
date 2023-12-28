import numpy as np

album = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #creamos el album



print(album)

for i in range(10):
    
    figurita = np.random.randint(len(album)) #nos toca una figu

    if album[figurita] == 0:
        album[figurita] = 1 #pegamos la figu

    elif album[figurita] == 1:
        album[figurita] = 2 #la guardamos como repe    


    
print(album) #mostramos el album

