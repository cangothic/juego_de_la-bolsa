__author__ = 'rocka'
import pygame
def clic(boton):
    pulsacion=pygame.mouse.get_pressed()
    if pulsacion[boton]:
        return True
    else: return False
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def actualizar(self):
        self.left,self.top=pygame.mouse.get_pos()
