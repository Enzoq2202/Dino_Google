import pygame



#Obtendo todas as fotos para animar o godzilla: 
trex_run1 = pygame.image.load('Dino/ZillaRun1.png')
trex_run1 = pygame.transform.scale(trex_run1, (80, 80))
trex_run2 = pygame.image.load('Dino/ZillaRun2.png')
trex_run2 = pygame.transform.scale(trex_run2, (80, 80))
trex_duck1 = pygame.image.load('Dino/ZillaDuck1.png')
trex_duck1 = pygame.transform.scale(trex_duck1, (70, 70))
trex_duck2 = pygame.image.load('Dino/ZillaDuck2.png')
trex_duck2 = pygame.transform.scale(trex_duck2, (70, 70))
trex_jump = pygame.image.load('Dino/ZillaJump.png')
trex_jump = pygame.transform.scale(trex_jump, (80, 80))


#Obtendo os obstáculos

cactus = pygame.image.load('obstaculos/cactus.png')
cactus = pygame.transform.scale(cactus, (60, 70))
pedra = pygame.image.load('obstaculos/pedra.png')
pedra = pygame.transform.scale(pedra, (40, 50))
charizard = pygame.image.load('obstaculos/charizard.png')
charizard = pygame.transform.scale(charizard, (90, 60))



#Obtendo o background:
background = pygame.image.load('background_dino.png')
background = pygame.transform.scale(background, (1250, 500))
fim = pygame.image.load('fim.png')
fim = pygame.transform.scale(fim, (1250, 500))


backgrounds = {
    'cenário':{
        'imagem':background,
        'obstaculos':[
            cactus,
            pedra,
            charizard
        ]
    }
}
lista_backgrounds = list(backgrounds.keys())
index_background = 0


#Listas T-rex:
run = [trex_run1, trex_run2]
duck = [trex_duck1, trex_duck2]
jump = trex_jump



velocidade_background = 13
