import pygame
from pygame import mixer


#Música principal
def musica_principal():
    mixer.init()
    pygame.mixer.music.load('10. Rupert Holmes - Escape (The Piña Colada Song).mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)