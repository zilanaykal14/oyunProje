import pygame
import sys
import random
from mermi import Mermi
from dusman_sinif import Dusman

# Başlat
pygame.init()
GENISLIK, YUKSEKLIK = 800, 600
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Savaş Oyunu")
clock = pygame.time.Clock()

# Yazı tipi, skor ve can
pygame.font.init()
font = pygame.font.SysFont("Arial", 24)
skor = 0
can = 3
oyun_bitti = False

# Uçak resmi
ucak_resim = pygame.image.load("assets/ucak.png")
ucak_resim = pygame.transform.rotate(ucak_resim, 90)
ucak_rect = ucak_resim.get_rect()
ucak_rect.midbottom = (GENISLIK // 2, YUKSEKLIK - 20)
ucak_hiz = 5

# Listeler
mermiler = []
dusmanlar = []
dusman_sayaci = 0

# Ana döngü
calisiyor = True
while calisiyor:
    clock.tick(60)
    ekran.fill((10, 10, 30))

    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            calisiyor = False
        elif etkinlik.type == pygame.KEYDOWN:
            if etkinlik.key == pygame.K_ESCAPE:
                calisiyor = False
            elif etkinlik.key == pygame.K_SPACE and not oyun_bitti:
                mermiler.append(Mermi(ucak_rect.centerx, ucak_rect.top))

    # Uçak hareket
    if not oyun_bitti:
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT] and ucak_rect.left > 0:
            ucak_rect.x -= ucak_hiz
        if tuslar[pygame.K_RIGHT] and ucak_rect.right < GENISLIK:
            ucak_rect.x += ucak_hiz

    # Mermiler
    for mermi in mermiler[:]:
        mermi.hareket_et()
        if mermi.ekran_disinda_mi():
            mermiler.remove(mermi)
        else:
            mermi.ciz(ekran)

    # Düşman üret
    if not oyun_bitti:
        dusman_sayaci += 1
        if dusman_sayaci > 60:
            dusman_sayaci = 0
            x = random.randint(50, GENISLIK - 50)
            dusmanlar.append(Dusman(x, -40))

    # Düşmanlar
    for dusman in dusmanlar[:]:
        dusman.hareket_et()

        # Mermi ile çarpışma
        for mermi in mermiler[:]:
            if dusman.rect.colliderect(mermi.rect):
                dusmanlar.remove(dusman)
                mermiler.remove(mermi)
                skor += 1
                break

        # Uçak ile çarpışma
        if dusman.rect.colliderect(ucak_rect):
            dusmanlar.remove(dusman)
            can -= 1
            if can <= 0:
                oyun_bitti = True
            continue

        # Dışarı çıktıysa sil
        if dusman.ekran_disinda_mi(YUKSEKLIK):
            dusmanlar.remove(dusman)
        else:
            dusman.ciz(ekran)

    # Uçak
    ekran.blit(ucak_resim, ucak_rect)

    # Skor ve can
    ekran.blit(font.render(f"Skor: {skor}", True, (255, 255, 255)), (10, 10))
    ekran.blit(font.render(f"Can: {can}", True, (255, 100, 100)), (10, 40))

    # Game Over
    if oyun_bitti:
        ekran.blit(font.render("GAME OVER", True, (255, 0, 0)), (GENISLIK // 2 - 80, YUKSEKLIK // 2))

    pygame.display.update()

pygame.quit()
sys.exit()
