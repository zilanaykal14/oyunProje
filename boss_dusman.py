import pygame
import random

class BossDusman:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/boss.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(center=(x, y))
        self.can = 3
        self.hiz = 1.5

    def hareket_et(self, carpan=1.0):  # ✅ yavaşlatma çarpanı eklendi
        self.rect.y += self.hiz * carpan

    def ciz(self, ekran):
        ekran.blit(self.image, self.rect.topleft)

    def ekran_disinda_mi(self, yukseklik):
        return self.rect.top > yukseklik
