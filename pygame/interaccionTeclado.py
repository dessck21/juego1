import pygame
from sys import exit
from Cuadrado import Cuadrado

pygame.init()
anchoV = 400    # Se define el ancho de la ventana
altoV = 400
tamPant = (anchoV,altoV)
pantalla = pygame.display.set_mode(tamPant)

reloj = pygame.time.Clock()

cRojo = Cuadrado(100,100,10,(255,50,50))

while True:
    pygame.Surface.fill(pantalla,(0,0,0),None)
    for event in pygame.event.get():
        #rint(event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            print("Tecla presionada: ",event.type)
            if event.key == pygame.K_a:
                print("Tecla a apretada",pygame.K_a)
        if event.type == pygame.KEYUP:
            print("Tecla liberada: ",event.type)
            
    pygame.draw.rect(pantalla, cRojo.color, (cRojo.posX, cRojo.posY, cRojo.tam,cRojo.tam)) # (Superficie en la cual dibuja, color, (objeto rect{x,y, tamx, tamy} ))
    xIni = 3
    yIni = 3
    #Actualizar posicion de los cuadrados
    cRojo.posX = cRojo.posX + (xIni*cRojo.velx)
    cRojo.posY = (cRojo.posY*cRojo.vely)
    cRojo.comprobarL(400,400)
    pygame.display.update()
    reloj.tick(60)
    pass