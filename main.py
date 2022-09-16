import pygame
from imagens import *
from classes import *
import random
from music import *
import time
#inicilizando o pygame
pygame.init()

#definição da tela
altura = 500
largura = 1250
#definindo a tela
window = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('T-rex Runner')
#variaveis do jogo
game = True
contador = 0
limite = largura
pontuacao = 0
#obtendo o fonte usada na pontuação
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()
#Pegando as sprites
todas_sprites = pygame.sprite.Group()  
todos_obstaculos = pygame.sprite.Group()
#Chamando a classe do T-rex
player = Trex()
todas_sprites.add(player)
vidas = 3
jogo = True


#loop para fazer a tela inicial.
while jogo:
    window.blit(background, (0,0))
    text = font.render('Aperte Qualquer Tecla', False, (128,128,128))
    text_baixo = font.render('Para Começar', False, (128,128,128))
    textRect = text.get_rect()
    window.blit(text_baixo, (550,60))
    textRect.center = (625, 40)
    window.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
            game = False
        if event.type == pygame.KEYDOWN:
            jogo = False

    pygame.display.update()





#dando inicio ao jogo
musica_principal()
while game:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    

    #verificando as teclas pressionadas
    teclas = pygame.key.get_pressed()
    
    
    #dando ações para as teclas apertadas e atribuindo ações para o T-rex
    if teclas[pygame.K_UP] and not player.trex_pulando:
        player.trex_correndo = False
        player.trex_agachando = False 
        player.trex_pulando = True 
        player.v_jump = 9
    elif teclas[pygame.K_DOWN] and not player.trex_pulando: 
        player.trex_correndo = False
        player.trex_agachando = True 
        player.trex_pulando = False
    elif not (player.trex_pulando or teclas[pygame.K_DOWN]): 
        player.trex_correndo = True
        player.trex_agachando = False 
        player.trex_pulando = False
    
    #fazer o background andar em um loop infinito
    window.blit(background, (contador,0))
    window.blit(background, (contador + limite,0))
    contador -= velocidade_background
    if contador <= -limite:
        contador = 0
    contador -= velocidade_background
    cenario = backgrounds[lista_backgrounds[index_background]]
    imagem_background = cenario['imagem']


    #Gerando os obstáculos
    while len(todos_obstaculos) < 2:
        tipo = random.randint(0,2)
        obstaculo = Obstaculos(cenario['obstaculos'][tipo])
        todos_obstaculos.add(obstaculo)
        todas_sprites.add(obstaculo)

        if len(todos_obstaculos) < 2: 
            obstaculo.rect.x += 800 

    #verificar se o T-rex colidiu com algum obstáculo e se sim, diminuir uma vida
    hit = pygame.sprite.spritecollide(player, todos_obstaculos, True, collided=pygame.sprite.collide_mask)
    if hit:
        vidas -= 1
        if vidas == 0:
            time.sleep(0.2)
            window.blit(fim,(0,0)) 
            text = font.render('Pontuação Final:' + str(pontuacao), False, (128,128,128))
            textRect = text.get_rect()
            textRect.center = (625, 40)
            window.blit(text, textRect)
            pygame.display.update()
            time.sleep(3.0)
            game = False
    
    #a velocidade do background aumenta a cada 1000 pontos
    if pontuacao % 1000 == 0 and pontuacao != 0:
        velocidade_background += 2
        pontuacao += 1
    else:
        pontuacao += 1

    #atualizando a tela com as spritez
    todas_sprites.draw(window)
    todas_sprites.update()
    
    #blitando a pontuação na tela
    text = font.render('Pontos:' + str(pontuacao), False, (128,128,128))
    text_vida = font.render('Vidas:' + str(vidas), False, (128,128,128))
    window.blit(text_vida, (100,40))
    textRect = text.get_rect()
    textRect.center = (1100, 40)
    window.blit(text, textRect)

    
    
    
    
    
    pygame.display.update() 



