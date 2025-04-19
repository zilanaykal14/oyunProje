import pygame

class CanKutusu:
    def __init__(self, x, y):
        self.resim = pygame.image.load("assets/can.png")  # Yıldız görseli
        self.resim = pygame.transform.scale(self.resim, (35, 35))  # İstersen boyutlandır
        self.rect = self.resim.get_rect(center=(x, y))
        self.hiz = 2

    def hareket_et(self):
        self.rect.y += self.hiz

    def ekran_disinda_mi(self, yukseklik):
        return self.rect.top > yukseklik

    def ciz(self, ekran):
        ekran.blit(self.resim, self.rect)
