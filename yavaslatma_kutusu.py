import pygame

class YavaslatmaKutusu:
    def __init__(self, x, y):
        self.resim = pygame.image.load("assets/yavaslatma_kutusu.png")  # ❗ Dosya bu isimde olmalı
        self.resim = pygame.transform.scale(self.resim, (45, 45))
        self.rect = self.resim.get_rect(center=(x, y))
        self.hiz = 2

    def hareket_et(self, carpan=1.0):
        self.rect.y += int(self.hiz * carpan)

    def ekran_disinda_mi(self, yukseklik):
        return self.rect.top > yukseklik

    def ciz(self, ekran):
        ekran.blit(self.resim, self.rect)
