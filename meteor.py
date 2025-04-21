import pygame
import random

class Meteor:
    def __init__(self, ekran_genislik):
        self.x = random.randint(0, ekran_genislik)
        self.y = random.randint(-600, -50)
        self.hiz_y = random.uniform(2.0, 5.0)
        self.uzunluk = random.randint(10, 25)
        self.renk = random.choice([
            (200, 200, 255),  # açık mavi
            (255, 100, 100),  # kırmızımsı
            (255, 255, 100),  # sarı
            (150, 255, 150),  # yeşil
            (255, 255, 255),  # beyaz
            (180, 150, 255)   # mor
        ])

    def hareket_et(self, carpan=1.0):  # ✅ yavaşlatma çarpanı eklendi
        self.y += self.hiz_y * carpan
        if self.y > 600:
            self.y = random.randint(-600, -50)
            self.x = random.randint(0, 800)
            self.renk = random.choice([
                (200, 200, 255),
                (255, 100, 100),
                (255, 255, 100),
                (150, 255, 150),
                (255, 255, 255),
                (180, 150, 255)
            ])

    def ciz(self, ekran):
        pygame.draw.line(ekran, self.renk, (self.x, self.y), (self.x, self.y + self.uzunluk), 1)
