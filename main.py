import pygame
import sys

# Pygame başlat
pygame.init()
GENISLIK, YUKSEKLIK = 800, 600
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Dik Uçak Yatay Hareket")
clock = pygame.time.Clock()

# Uçak görseli yükle ve dik hale getir (burnu yukarı bakacak şekilde)
ucak_resim = pygame.image.load("assets/ucak.png")
ucak_resim = pygame.transform.rotate(ucak_resim, 90)  # Saat yönünde 90 derece döndür

# Uçak konumu
ucak_rect = ucak_resim.get_rect()
ucak_rect.midbottom = (GENISLIK // 2, YUKSEKLIK - 20)
ucak_hiz = 5

# Oyun döngüsü
calisiyor = True
while calisiyor:
    clock.tick(60)
    ekran.fill((10, 10, 30))  # Uzay efekti için koyu arka plan

    # Etkinlik kontrolü
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            calisiyor = False

    # Tuş kontrolü
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT] and ucak_rect.left > 0:
        ucak_rect.x -= ucak_hiz
    if tuslar[pygame.K_RIGHT] and ucak_rect.right < GENISLIK:
        ucak_rect.x += ucak_hiz

    # Uçağı çiz
    ekran.blit(ucak_resim, ucak_rect)
    pygame.display.update()

# Çıkış
pygame.quit()
sys.exit()
