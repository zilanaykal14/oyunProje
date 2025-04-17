import pygame
import random

class Engel:
    def __init__(self, x, y, hiz_x=None, hiz_y=None):
        self.x = x
        self.y = y
        self.genislik = 50
        self.yukseklik = 50
        self.renk = (0, 0, 0)  # Siyah renkli engel

        # Başlangıçta daha yavaş hızlarla başlat (titremeyi önlemek için)
        self.hiz_x = hiz_x if hiz_x is not None else random.choice([-1.5, -1, 1, 1.5])
        self.hiz_y = hiz_y if hiz_y is not None else random.choice([-1.5, -1, 1, 1.5])

    def hareket_et(self, ekran_genislik, ekran_yukseklik, bitis_y):
        self.x += self.hiz_x
        self.y += self.hiz_y

        # Hareket alanı: bitiş çizgisi ile ekranın ortası arası
        ust_sinir = bitis_y + 10
        alt_sinir = int(ekran_yukseklik * 0.7)

        # YATAY sınırlar ve yön değiştirme
        if self.x <= 0:
            self.x = 0
            self.hiz_x *= -1
        elif self.x + self.genislik >= ekran_genislik:
            self.x = ekran_genislik - self.genislik
            self.hiz_x *= -1

        # DİKEY sınırlar ve yön değiştirme
        if self.y <= ust_sinir:
            self.y = ust_sinir
            self.hiz_y *= -1
        elif self.y + self.yukseklik >= alt_sinir:
            self.y = alt_sinir - self.yukseklik
            self.hiz_y *= -1

    def ciz(self, ekran):
        pygame.draw.rect(ekran, self.renk, (self.x, self.y, self.genislik, self.yukseklik))

    def carpti_mi(self, araba):
        araba_rect = pygame.Rect(araba.x, araba.y, araba.genislik, araba.yukseklik)
        engel_rect = pygame.Rect(self.x, self.y, self.genislik, self.yukseklik)
        return araba_rect.colliderect(engel_rect)

    def hizi_arttir(self):
        # Hızı artırırken çok fazla zıplamaması için hassas artış yap
        artis = 0.3
        self.hiz_x += artis if self.hiz_x > 0 else -artis
        self.hiz_y += artis if self.hiz_y > 0 else -artis
