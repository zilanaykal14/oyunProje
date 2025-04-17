import pygame
import sys
from araba import Araba
from engel import Engel

pygame.init()

# Ekran boyutu
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("İki Kişilik Araba Yarışı")

# FPS ayarı
clock = pygame.time.Clock()

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Bitiş çizgisi
bitis_y = 50

# Engeller
engeller = [
    Engel(300, 400),
    Engel(150, 300),
    Engel(500, 200)
]

# Arabalar (Tuşlar büyük harfli olmalı)
araba1 = Araba(200, 500, RED, ["W", "S", "A", "D"])
araba2 = Araba(400, 500, BLUE, ["UP", "DOWN", "LEFT", "RIGHT"])

kazanan = None

# Zorluk sayacı (her 10 saniyede bir hız artırma)
zorluk_sayaci = pygame.time.get_ticks()

# Ana oyun döngüsü
running = True
while running:
    screen.fill(WHITE)

    # Engelleri çiz ve çarpışma kontrolü yap
    for engel in engeller:
        engel.hareket_et(WIDTH, HEIGHT, bitis_y)  # Ekran boyutları ve bitiş çizgisi parametrelerini ekleyin
        engel.ciz(screen)

        # Çarpışma kontrolü
        if engel.carpti_mi(araba1):
            print("Oyuncu 1 kaza yaptı!")
            font = pygame.font.SysFont(None, 60)
            text = font.render("Oyuncu 1 Kaza Yaptı!", True, (255, 0, 0))
            screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

        if engel.carpti_mi(araba2):
            print("Oyuncu 2 kaza yaptı!")
            font = pygame.font.SysFont(None, 60)
            text = font.render("Oyuncu 2 Kaza Yaptı!", True, (255, 0, 0))
            screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

    # Zorluk seviyesini artır (her 10 saniyede bir engel hızını arttır)
    if pygame.time.get_ticks() - zorluk_sayaci > 10000:  # 10.000 ms = 10 sn
        for engel in engeller:
            engel.hizi_arttir()  # Engelin hızını artır
        zorluk_sayaci = pygame.time.get_ticks()  # Zamanı sıfırla

    # Bitiş çizgisi
    pygame.draw.rect(screen, GREEN, (0, bitis_y, WIDTH, 10))

    # Olayları dinle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tuşları kontrol et
    keys = pygame.key.get_pressed()
    araba1.hareketEt(keys, WIDTH, HEIGHT)
    araba2.hareketEt(keys, WIDTH, HEIGHT)

    araba1.ciz(screen)
    araba2.ciz(screen)

    # Kazanan kontrolü
    if araba1.y <= bitis_y and kazanan is None:
        kazanan = "Oyuncu 1"
    if araba2.y <= bitis_y and kazanan is None:
        kazanan = "Oyuncu 2"

    if kazanan:
        font = pygame.font.SysFont(None, 60)
        text = font.render(f"{kazanan} Kazandı!", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
