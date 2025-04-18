import pygame
import sys
import random
from dusman_sinif import Dusman # DÜŞMAN SINIFINI EKLİYORUZ

# Pygame başlat
pygame.init()
GENISLIK, YUKSEKLIK = 800, 600
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Dik Uçak Yatay Hareket + Düşman")
clock = pygame.time.Clock()

# Uçak görseli
ucak_resim = pygame.image.load("assets/ucak.png")
ucak_resim = pygame.transform.rotate(ucak_resim, 90)  # Yukarı baktır

ucak_rect = ucak_resim.get_rect()
ucak_rect.midbottom = (GENISLIK // 2, YUKSEKLIK - 20)
ucak_hiz = 5

# Düşman listesi
dusmanlar = []
dusman_zaman = 0

# Oyun döngüsü
calisiyor = True
while calisiyor:
    clock.tick(60)
    ekran.fill((10, 10, 30))

    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            calisiyor = False

    # Tuşlarla uçağı hareket ettir
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT] and ucak_rect.left > 0:
        ucak_rect.x -= ucak_hiz
    if tuslar[pygame.K_RIGHT] and ucak_rect.right < GENISLIK:
        ucak_rect.x += ucak_hiz

    # Düşman üretimi
    dusman_zaman += 1
    if dusman_zaman > 60:
        dusman_zaman = 0
        x = random.randint(50, GENISLIK - 50)
        dusmanlar.append(Dusman(x, -40))

    # Düşmanları hareket ettir ve çiz
    for dusman in dusmanlar[:]:
        dusman.hareket_et()
        dusman.ciz(ekran)

        if dusman.ekran_disinda_mi(YUKSEKLIK):
            dusmanlar.remove(dusman)

    # Uçağı çiz
    ekran.blit(ucak_resim, ucak_rect)
    pygame.display.update()

# Çıkış
pygame.quit()
sys.exit()