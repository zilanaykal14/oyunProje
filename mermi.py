import pygame  # pygame modülünü import etmelisiniz

class Mermi:
    def __init__(self, x, y, resim_yolu):
        # Mermi görselini yükle
        self.gorsel = pygame.image.load(resim_yolu)
        self.gorsel = pygame.transform.scale(self.gorsel, (40, 40))  # Boyutları küçült

        # Rect nesnesi oluşturuyoruz
        self.rect = self.gorsel.get_rect(center=(x, y))

        self.hiz = -10  # Merminin hareket hızı

    def hareket_et(self):
        self.rect.y += self.hiz  # Y ekseninde hareket ettir

    def ciz(self, ekran):
        ekran.blit(self.gorsel, self.rect)

    def ekran_disinda_mi(self):
        return self.rect.bottom < 0  # Eğer mermi ekranın dışına çıktıysa True döner
