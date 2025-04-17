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

    def hareket(self, keys):
        if self.kontroller[0] == "w":  # Oyuncu 1
            if keys[pygame.K_w]:
                self.y -= self.hiz
            if keys[pygame.K_s]:
                self.y += self.hiz
        elif self.kontroller[0] == "up":  # Oyuncu 2
            if keys[pygame.K_UP]:
                self.y -= self.hiz
            if keys[pygame.K_DOWN]:
                self.y += self.hiz

    def ciz(self, ekran):
        pygame.draw.rect(ekran, self.renk, (self.x, self.y, self.genislik, self.yukseklik))
