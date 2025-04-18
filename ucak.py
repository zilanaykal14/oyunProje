import pygame

class Ucak:
    def __init__(self, x, y, resim):
        self.gorsel = pygame.image.load(resim)
        self.rect = self.gorsel.get_rect(center=(x, y))
        self.hiz = 5

    def hareket_et(self, tuslar, ekran_genisligi):
        if tuslar[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.hiz
        if tuslar[pygame.K_RIGHT] and self.rect.right < ekran_genisligi:
            self.rect.x += self.hiz

    def ciz(self, ekran):
        ekran.blit(self.gorsel, self.rect)
