import pygame
import sys
import random
from mermi import Mermi
from dusman_sinif import Dusman
from patlama import Patlama
from can_kutusu import CanKutusu
from mermi_kutusu import MermiKutusu
from boss_dusman import BossDusman
from meteor import Meteor
from yavaslatma_kutusu import YavaslatmaKutusu

pygame.init()
GENISLIK, YUKSEKLIK = 800, 600
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Savaş Oyunu")
clock = pygame.time.Clock()

arka_plan = pygame.image.load("assets/arkaplan.png")
arka_plan = pygame.transform.scale(arka_plan, (GENISLIK, YUKSEKLIK))

lazer_sesi = pygame.mixer.Sound("assets/lazer_sesi.wav")
lazer_sesi.set_volume(0.5)

boss_vurulma_sesi = pygame.mixer.Sound("assets/boss_patlama.wav")
boss_vurulma_sesi.set_volume(0.7)

pygame.font.init()
font = pygame.font.SysFont("Arial", 24)
skor, can, max_can = 0, 3, 3
oyun_bitti = False
seviye = 1
dusman_hiz_carpani = 1.0
mermi_sayisi = 20
max_mermi = 20

mermiler, dusmanlar, patlamalar = [], [], []
can_kutulari, mermi_kutulari, yavaslatma_kutulari = [], [], []
dusman_sayaci, can_kutu_sayaci, mermi_kutu_sayaci, yavaslatma_kutu_sayaci = 0, 0, 0, 0

boss, boss_aktif = None, False
meteorlar = [Meteor(GENISLIK) for _ in range(20)]

sarsinti_suresi = 0
max_sarsinti_suresi = 15

yavaslatma_aktif = False
yavaslatma_geri_sayim = 0
yavaslatma_carpani = 0.3

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

ucak_resim = pygame.image.load("assets/ucak.png")
ucak_resim = pygame.transform.rotate(ucak_resim, 90)
ucak_rect = ucak_resim.get_rect()
ucak_rect.midbottom = (GENISLIK // 2, YUKSEKLIK - 20)
ucak_hiz = 5

def can_bari_ciz(ekran, can, max_can):
    oran = can / max_can
    bar_genislik = 120
    bar_yukseklik = 20
    x = GENISLIK - bar_genislik - 20
    y = 20
    pygame.draw.rect(ekran, (60, 60, 60), (x, y, bar_genislik, bar_yukseklik), border_radius=10)
    renk = (0, 220, 0) if oran > 0.5 else (255, 165, 0) if oran > 0.25 else (255, 50, 50)
    pygame.draw.rect(ekran, renk, (x, y, int(bar_genislik * oran), bar_yukseklik), border_radius=10)
    ekran.blit(font.render(f"Can: {can}/{max_can}", True, (255, 255, 255)), (x, y - 25))

def sarsinti_efekti():
    return random.randint(-5, 5), random.randint(-5, 5)

def oyunu_sifirla():
    global ucak_rect, skor, can, oyun_bitti, mermiler, dusmanlar, patlamalar
    global can_kutulari, dusman_sayaci, can_kutu_sayaci, seviye, dusman_hiz_carpani
    global mermi_sayisi, mermi_kutulari, mermi_kutu_sayaci, boss, boss_aktif
    global yavaslatma_aktif, yavaslatma_geri_sayim, yavaslatma_kutulari
    ucak_rect.midbottom = (GENISLIK // 2, YUKSEKLIK - 20)
    skor, can, oyun_bitti = 0, max_can, False
    seviye, dusman_hiz_carpani = 1, 1.0
    mermi_sayisi = max_mermi
    mermiler.clear(), dusmanlar.clear(), patlamalar.clear()
    can_kutulari.clear(), mermi_kutulari.clear(), yavaslatma_kutulari.clear()
    dusman_sayaci = can_kutu_sayaci = mermi_kutu_sayaci = yavaslatma_kutu_sayaci = 0
    boss, boss_aktif = None, False
    meteorlar[:] = [Meteor(GENISLIK) for _ in range(20)]
    yavaslatma_aktif, yavaslatma_geri_sayim = False, 0

calisiyor = True
while calisiyor:
    clock.tick(60)
    if yavaslatma_aktif:
        yavaslatma_geri_sayim -= 1
        if yavaslatma_geri_sayim <= 0:
            yavaslatma_aktif = False
    carpan = yavaslatma_carpani if yavaslatma_aktif else 1.0

    ekran.blit(arka_plan, sarsinti_efekti() if sarsinti_suresi > 0 else (0, 0))
    sarsinti_suresi = max(0, sarsinti_suresi - 1)

    for meteor in meteorlar:
        meteor.hareket_et(carpan)
        meteor.ciz(ekran)

    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            calisiyor = False
        elif etkinlik.type == pygame.KEYDOWN:
            if etkinlik.key == pygame.K_ESCAPE:
                calisiyor = False
            elif etkinlik.key == pygame.K_SPACE and not oyun_bitti and mermi_sayisi > 0:
                lazer_sesi.play()
                mermiler.append(Mermi(ucak_rect.centerx, ucak_rect.top, "assets/mermi.png"))
                mermi_sayisi -= 1
            elif etkinlik.key == pygame.K_r and oyun_bitti:
                oyunu_sifirla()

    if not oyun_bitti:
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT] and ucak_rect.left > 0:
            ucak_rect.x -= ucak_hiz
        if tuslar[pygame.K_RIGHT] and ucak_rect.right < GENISLIK:
            ucak_rect.x += ucak_hiz

    for m in mermiler[:]:
        m.hareket_et()
        if m.ekran_disinda_mi():
            mermiler.remove(m)
        else:
            m.ciz(ekran)

    if skor // 20 + 1 != seviye:
        seviye = skor // 20 + 1
        dusman_hiz_carpani += 0.2
        if not boss_aktif:
            boss = BossDusman(GENISLIK // 2, -80)
            boss_aktif = True

    if not oyun_bitti:
        dusman_sayaci += 1
        if dusman_sayaci > 60:
            dusman_sayaci = 0
            dusmanlar.append(Dusman(random.randint(50, GENISLIK - 50), -40, dusman_hiz_carpani))

    if not oyun_bitti:
        can_kutu_sayaci += 1
        if can_kutu_sayaci > 300:
            can_kutu_sayaci = 0
            can_kutulari.append(CanKutusu(random.randint(50, GENISLIK - 50), -30))

    if not oyun_bitti:
        mermi_kutu_sayaci += 1
        if mermi_kutu_sayaci > 500:
            mermi_kutu_sayaci = 0
            mermi_kutulari.append(MermiKutusu(random.randint(50, GENISLIK - 50), -30))

    if not oyun_bitti:
        yavaslatma_kutu_sayaci += 1
        if yavaslatma_kutu_sayaci > 600:
            yavaslatma_kutu_sayaci = 0
            yavaslatma_kutulari.append(YavaslatmaKutusu(random.randint(50, GENISLIK - 50), -30))

    for yk in yavaslatma_kutulari[:]:
        yk.hareket_et(carpan)
        yk.ciz(ekran)
        for m in mermiler[:]:
            if yk.rect.colliderect(m.rect):
                yavaslatma_aktif = True
                yavaslatma_geri_sayim = 240
                yavaslatma_kutulari.remove(yk)
                mermiler.remove(m)
                break
            elif yk.ekran_disinda_mi(YUKSEKLIK):
             yavaslatma_kutulari.remove(yk)

    for d in dusmanlar[:]:
        d.hareket_et(carpan)
        for m in mermiler[:]:
            if d.rect.colliderect(m.rect):
                dusmanlar.remove(d)
                mermiler.remove(m)
                skor += 1
                patlamalar.append(Patlama(d.rect.centerx, d.rect.centery))
                break
        if d.rect.colliderect(ucak_rect):
            dusmanlar.remove(d)
            can -= 1
            sarsinti_suresi = max_sarsinti_suresi
            if can <= 0:
                oyun_bitti = True
                if skor > en_yuksek_skor:
                    skoru_yaz(skor)
                    en_yuksek_skor = skor
        elif d.ekran_disinda_mi(YUKSEKLIK):
            dusmanlar.remove(d)
        else:
            d.ciz(ekran)

    for p in patlamalar[:]:
        p.guncelle()
        p.ciz(ekran)
        if p.bitti_mi():
            patlamalar.remove(p)

    for k in can_kutulari[:]:
        k.hareket_et(carpan)
        k.ciz(ekran)
        for m in mermiler[:]:
            if k.rect.colliderect(m.rect):
                if can < max_can:
                    can += 1
                can_kutulari.remove(k)
                mermiler.remove(m)
                break
            elif k.ekran_disinda_mi(YUKSEKLIK):
             can_kutulari.remove(k)

    for mk in mermi_kutulari[:]:
        mk.hareket_et(carpan)
        mk.ciz(ekran)
        if mk.rect.colliderect(ucak_rect):
            mermi_sayisi = min(max_mermi, mermi_sayisi + 10)
            mermi_kutulari.remove(mk)
        elif mk.ekran_disinda_mi(YUKSEKLIK):
            mermi_kutulari.remove(mk)

    if boss:
        boss.hareket_et(carpan)
        boss.ciz(ekran)
        for m in mermiler[:]:
            if boss.rect.colliderect(m.rect):
                mermiler.remove(m)
                boss.can -= 1
                boss_vurulma_sesi.play()
                if boss.can <= 0:
                    skor += 5
                    boss, boss_aktif = None, False
        if boss.ekran_disinda_mi(YUKSEKLIK):
            boss, boss_aktif = None, False
        ekran.blit(font.render("BOSS GELDİ!", True, (255, 0, 0)), (GENISLIK // 2 - 60, 10))

    ekran.blit(ucak_resim, ucak_rect)
    ekran.blit(font.render(f"Skor: {skor}", True, (255, 255, 255)), (10, 10))
    ekran.blit(font.render(f"En Yüksek Skor: {en_yuksek_skor}", True, (200, 200, 200)), (10, 40))
    ekran.blit(font.render(f"Seviye: {seviye}", True, (255, 255, 0)), (10, 70))
    ekran.blit(font.render(f"Mermi: {mermi_sayisi}/{max_mermi}", True, (0, 200, 255)), (10, 100))

    if yavaslatma_aktif:
        kalan_saniye = round(yavaslatma_geri_sayim / 60, 1)
        yazi = font.render(f"YAVAŞLATMA: {kalan_saniye} SN", True, (0, 255, 255))
        ekran.blit(yazi, (GENISLIK - 250, YUKSEKLIK - 30))

    can_bari_ciz(ekran, can, max_can)

    if oyun_bitti:
        ekran.blit(font.render("GAME OVER - R: Yeniden Başlat", True, (255, 0, 0)),
                    (GENISLIK // 2 - 160, YUKSEKLIK // 2))

    pygame.display.update()

pygame.quit()
sys.exit() 