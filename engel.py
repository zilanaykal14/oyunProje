import pygame

class Engel:
    def __init__(self, x, y, genislik=60, yukseklik=20):
        self.rect = pygame.Rect(x, y, genislik, yukseklik)
        self.renk = (120, 120, 120)

    def ciz(self, ekran):
        pygame.draw.rect(ekran, self.renk, self.rect)

    def carpti_mi(self, araba):
        araba_rect = pygame.Rect(araba.x, araba.y, araba.genislik, araba.yukseklik)
        return self.rect.colliderect(araba_rect)