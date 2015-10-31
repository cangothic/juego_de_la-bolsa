__author__ = 'rocka'
import pygame
from mannanger.Imagen import *
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2):
        pygame.sprite.Sprite.__init__(self)
        self.image_normal=load_image(imagen1,True)
        self.image_seleccion=load_image(imagen2,True)
        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top=(680,300)

    def actualizar(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.image=self.image_seleccion
        else: self.image=self.image_normal
        pantalla.blit(self.image,(680,300))