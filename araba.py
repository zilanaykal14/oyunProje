import pygame

class Araba:
    def __init__(self, x, y, renk, kontroller):
        self.x = x
        self.y = y
        self.renk = renk
        self.genislik = 50
        self.yukseklik = 80
        self.hiz = 5
        self.kontroller = kontroller

    def hareketEt(self, keys, ekran_genislik, ekran_yukseklik):
        if self.kontroller[0] == "W":  # Oyuncu 1 (WASD)
            if keys[pygame.K_w]:
                self.y -= self.hiz
            if keys[pygame.K_s]:
                self.y += self.hiz
            if keys[pygame.K_a]:
                self.x -= self.hiz
            if keys[pygame.K_d]:
                self.x += self.hiz

        elif self.kontroller[0] == "UP":  # Oyuncu 2 (Yön tuşları)
            if keys[pygame.K_UP]:
                self.y -= self.hiz
            if keys[pygame.K_DOWN]:
                self.y += self.hiz
            if keys[pygame.K_LEFT]:
                self.x -= self.hiz
            if keys[pygame.K_RIGHT]:
                self.x += self.hiz

        # EKRAN SINIRLARI (çıkmayı engeller)
        self.x = max(0, min(self.x, ekran_genislik - self.genislik))
        self.y = max(0, min(self.y, ekran_yukseklik - self.yukseklik))

    def ciz(self, ekran):
        pygame.draw.rect(ekran, self.renk, (self.x, self.y, self.genislik, self.yukseklik))
