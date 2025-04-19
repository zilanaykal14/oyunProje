import pygame
import sys
import random
from mermi import Mermi
from dusman_sinif import Dusman

pygame.init()
GENISLIK, YUKSEKLIK = 800, 600
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Savaş Oyunu")
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont("Arial", 24)
skor = 0
can = 3
max_can = 3
oyun_bitti = False

def en_yuksek_skoru_oku(dosya="skor.txt"):
    try:
        with open(dosya, "r") as f:
            return int(f.read())
    except:
        return 0

def skoru_yaz(skor, dosya="skor.txt"):
    with open(dosya, "w") as f:
        f.write(str(skor))

en_yuksek_skor = en_yuksek_skoru_oku()

# Uçak resmi
ucak_resim = pygame.image.load("assets/ucak.png")
ucak_resim = pygame.transform.rotate(ucak_resim, 90)
ucak_rect = ucak_resim.get_rect()
ucak_rect.midbottom = (GENISLIK // 2, YUKSEKLIK - 20)
ucak_hiz = 5

mermiler = []
dusmanlar = []
dusman_sayaci = 0

# ✅ MODERN CAN BARI
def can_bari_ciz(ekran, can, max_can):
    oran = can / max_can
    bar_genislik = 120
    bar_yukseklik = 20
    x = GENISLIK - bar_genislik - 20
    y = 20

    pygame.draw.rect(ekran, (60, 60, 60), (x, y, bar_genislik, bar_yukseklik), border_radius=10)

    if oran > 0.5:
        renk = (0, 220, 0)
    elif oran > 0.25:
        renk = (255, 165, 0)
    else:
        renk = (255, 50, 50)

    dolu_genislik = int(bar_genislik * oran)
    pygame.draw.rect(ekran, renk, (x, y, dolu_genislik, bar_yukseklik), border_radius=10)

    # Yazı ortalanmış
    yazi = font.render(f"Can: {can}/{max_can}", True, (255, 255, 255))
    yazi_rect = yazi.get_rect(center=(x + bar_genislik // 2, y + bar_yukseklik // 2))
    ekran.blit(yazi, yazi_rect)

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

    # Uçak hareketi
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

    # Düşman işlemleri
    for dusman in dusmanlar[:]:
        dusman.hareket_et()

        for mermi in mermiler[:]:
            if dusman.rect.colliderect(mermi.rect):
                dusmanlar.remove(dusman)
                mermiler.remove(mermi)
                skor += 1
                break

        if dusman.rect.colliderect(ucak_rect):
            dusmanlar.remove(dusman)
            can -= 1
            if can <= 0:
                oyun_bitti = True
                if skor > en_yuksek_skor:
                    skoru_yaz(skor)
                    en_yuksek_skor = skor
            continue

        if dusman.ekran_disinda_mi(YUKSEKLIK):
            dusmanlar.remove(dusman)
        else:
            dusman.ciz(ekran)

    # Uçak çizimi
    ekran.blit(ucak_resim, ucak_rect)

    # Skor ve can barı çizimleri
    ekran.blit(font.render(f"Skor: {skor}", True, (255, 255, 255)), (10, 10))
    ekran.blit(font.render(f"En Yüksek Skor: {en_yuksek_skor}", True, (200, 200, 200)), (10, 40))
    can_bari_ciz(ekran, can, max_can)

    if oyun_bitti:
        ekran.blit(font.render("GAME OVER", True, (255, 0, 0)), (GENISLIK // 2 - 80, YUKSEKLIK // 2))

    pygame.display.update()

pygame.quit()
sys.exit()
