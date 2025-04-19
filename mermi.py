import pygame

class Mermi:
    def __init__(self, x, y, hiz=7):
        self.x = x
        self.y = y
        self.hiz = hiz
        self.radius = 6
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)

    def hareket_et(self):
        self.y -= self.hiz
        self.rect.y = self.y

    def ciz(self, ekran):
        # Glow efekti için birkaç yarı saydam daire çiziyoruz (ışık yayılıyor gibi)
        for i in range(3, 0, -1):
            alpha = 50 * i  # dış halkalar daha saydam
            glow_color = (255, 255, 100, alpha)  # Sarımsı ışık
            glow_surface = pygame.Surface((self.radius * 4, self.radius * 4), pygame.SRCALPHA)
            pygame.draw.circle(glow_surface, glow_color, (self.radius * 2, self.radius * 2), self.radius * i)
            ekran.blit(glow_surface, (self.x - self.radius * 2, self.y - self.radius * 2))

        # Merkeze küçük bir dolu daire (merminin kendisi)
        pygame.draw.circle(ekran, (255, 255, 0), (self.x, self.y), self.radius // 2)

    def ekran_disinda_mi(self):
        return self.y + self.radius < 0
