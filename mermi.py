import pygame

class Mermi:
    def __init__(self, x, y, resim_yolu):
        # Mermi görselini yükle ve boyutlandır
        self.gorsel = pygame.image.load(resim_yolu)
        self.gorsel = pygame.transform.scale(self.gorsel, (40, 40))
        
        # Rect nesnesi: mermiyi ekran üstünde konumlandırmak için
        self.rect = self.gorsel.get_rect(center=(x, y))
        
        # Mermi hızı (negatif çünkü yukarı gidecek)
        self.hiz = -10

    def hareket_et(self, carpan=1.0):
        # Mermi yukarı doğru hareket eder
        self.rect.y += int(self.hiz * carpan)

    def ciz(self, ekran):
        # Mermiyi ekrana çizer
        ekran.blit(self.gorsel, self.rect)

    def ekran_disinda_mi(self):
        # Mermi ekran üstünden çıktıysa True döner
        return self.rect.bottom < 0
