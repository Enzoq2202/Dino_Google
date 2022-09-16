import pygame
from imagens import *


class Trex(pygame.sprite.Sprite):
    posicao_x = 10 
    posicao_y = 175
    posicao_abaixando = 185
    
    #Inicializando
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Acessando as listas criadas no arquivo de imagem
        self.imagens_correndo = run
        self.imagens_agachando = duck 
        self.imagem_pulando = jump 

        self.trex_correndo = True 
        self.trex_agachando = False 
        self.trex_pulando = False 

        self.step_index = 0 
        self.image = self.imagens_correndo[0] 
        self.rect = self.image.get_rect() 
        self.rect.x = self.posicao_x 
        self.rect.y = self.posicao_y

    #Função para atualizar os estados do dino
    def update(self): 
        if self.trex_agachando: 
            self.agachar()
        if self.trex_correndo:
            self.correr()
        if self.trex_pulando:
            self.pular()
        if self.step_index >= 10: 
            self.step_index = 0 
    #Função para o dino agachar
    def agachar(self): 
        self.image = self.imagens_agachando[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.posicao_x 
        self.rect.y = self.posicao_abaixando 
        self.step_index += 1
    #Função para o dino correr
    def correr(self):
        self.image = self.imagens_correndo[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.posicao_x 
        self.rect.y = self.posicao_y 
        self.step_index += 1
    #Função para o dino pular
    def pular(self):     
        self.image = self.imagem_pulando
        if self.trex_pulando:
            self.rect.y -= self.v_jump * 1.5
            self.v_jump -= 0.8
        if self.rect.y >= self.posicao_y:
            self.trex_pulando = False
            self.rect.y = self.posicao_y
        if self.rect.y < 0:
            self.rect.y = 0
        
    #Função para dar o blit na tela
    def draw(self,tela):    
        tela.blit(self.image, (self.rect.x,self.rect.y))

class Obstaculos(pygame.sprite.Sprite):
    #Inicializando
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x= 1250
    
    #Dando update nos obstáculos e definindo a quantidade de pixels
    def update(self):  
        self.rect.x -= velocidade_background
        if self.rect.x < -self.rect.width:
            self.kill()
        if self.image == pedra:
            self.rect.y = 200
        elif self.image == cactus:
            self.rect.y = 180
        elif self.image == charizard:
            self.rect.y = 130
           