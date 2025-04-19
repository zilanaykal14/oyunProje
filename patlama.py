import pygame
import os
import random

class Patlama:
    efektler = []

    @classmethod
    def efektleri_yukle(cls):
        if not cls.efektler:
            klasor = os.path.join("assets")
            dosyalar = ["splat_g.png", "splat_p.png", "splat_y.png", "splat_r.png"]
            for dosya in dosyalar:
                try:
                    yol = os.path.join(klasor, dosya)
                    resim = pygame.image.load(yol).convert_alpha()
                    cls.efektler.append(resim)
                except Exception as e:
                    print(f"Patlama efekti yüklenemedi: {dosya} - {e}")

    def __init__(self, x, y):
        self.efektleri_yukle()
        self.gorsel = random.choice(self.efektler)
        self.rect = self.gorsel.get_rect(center=(x, y))
        self.sayac = 0
        self.sure = 15

    def guncelle(self):
        self.sayac += 1

    def ciz(self, ekran):
        ekran.blit(self.gorsel, self.rect)

    def bitti_mi(self):
        return self.sayac > self.sure