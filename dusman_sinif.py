import pygame
import random
import os

class Dusman:
    sprite_boyut = 32
    tum_sprite_lar = []

    @classmethod
    def sprite_yukle(cls):
        if not cls.tum_sprite_lar:
            klasor = os.path.join("assets")
            for dosya in os.listdir(klasor):
                if dosya.endswith(".png") and dosya.startswith("alien"):
                    tam_yol = os.path.join(klasor, dosya)
                    try:
                        sheet = pygame.image.load(tam_yol).convert_alpha()
                        cls.tum_sprite_lar.extend(cls.sprite_sheet_parcala(sheet))
                    except Exception as e:
                        print(f"HATA: {dosya} yüklenemedi - {e}")

    @staticmethod
    def sprite_sheet_parcala(sheet):
        sprite_liste = []
        sprite_boyut = Dusman.sprite_boyut
        sheet_genislik, sheet_yukseklik = sheet.get_size()

        for y in range(0, sheet_yukseklik, sprite_boyut):
            for x in range(0, sheet_genislik, sprite_boyut):
                kare = sheet.subsurface(pygame.Rect(x, y, sprite_boyut, sprite_boyut))
                sprite_liste.append(kare)

        return sprite_liste

    def __init__(self, x, y, hiz_carpani=1.0):
        self.rect = pygame.Rect(x, y, self.sprite_boyut, self.sprite_boyut)
        self.hiz = 3 * hiz_carpani
        self.sprite_yukle()
        self.gorsel = random.choice(self.tum_sprite_lar)

    def hareket_et(self):
        self.rect.y += self.hiz

    def ciz(self, ekran):
        ekran.blit(self.gorsel, self.rect.topleft)

    def ekran_disinda_mi(self, yukseklik):
        return self.rect.top > yukseklik
