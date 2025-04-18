import pygame

class Dusman:
    def __init__(self, x, y, hiz=3):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.hiz = hiz

    def hareket_et(self):
        self.rect.y += self.hiz

    def ciz(self, ekran):
        pygame.draw.rect(ekran, (255, 0, 0), self.rect)

    def ekran_disinda_mi(self, yukseklik):
        return self.rect.top > yukseklik