import pygame

class MermiKutusu:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/mermi_kutusu.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.hiz = 2

    def hareket_et(self, carpan=1.0):  # ✅ carpan parametresi eklendi
        self.rect.y += int(self.hiz * carpan)

    def ciz(self, ekran):
        ekran.blit(self.image, self.rect.topleft)

    def ekran_disinda_mi(self, yukseklik):
        return self.rect.top > yukseklik
