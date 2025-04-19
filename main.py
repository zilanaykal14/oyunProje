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

pygame.init()
GENISLIK, YUKSEKLIK = 800, 600
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Savaş Oyunu")
clock = pygame.time.Clock()

arka_plan = pygame.image.load("assets/arkaplan.png")
arka_plan = pygame.transform.scale(arka_plan, (GENISLIK, YUKSEKLIK))

lazer_sesi = pygame.mixer.Sound("assets/lazer_sesi.wav")
lazer_sesi.set_volume(0.5)

pygame.font.init()
font = pygame.font.SysFont("Arial", 24)
skor = 0
can = 3
max_can = 3
oyun_bitti = False

seviye = 1
dusman_hiz_carpani = 1.0
mermi_sayisi = 20
max_mermi = 20
mermi_kutulari = []
mermi_kutu_sayaci = 0

boss = None
boss_aktif = False
meteorlar = [Meteor(GENISLIK) for _ in range(20)]

sarsinti_suresi = 0
max_sarsinti_suresi = 15  # Ekranın ne kadar süre sarsılacağını belirler (FPS cinsinden)

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

mermi_resim_yolu = "assets/mermi.png"
mermiler = []
dusmanlar = []
patlamalar = []
can_kutulari = []
dusman_sayaci = 0
can_kutu_sayaci = 0

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
    yazi = font.render(f"Can: {can}/{max_can}", True, (255, 255, 255))
    ekran.blit(yazi, (x, y - 25))

def oyunu_sifirla():
    global ucak_rect, skor, can, oyun_bitti, mermiler, dusmanlar, patlamalar, can_kutulari
    global dusman_sayaci, can_kutu_sayaci, seviye, dusman_hiz_carpani
    global mermi_sayisi, mermi_kutulari, mermi_kutu_sayaci, boss, boss_aktif, meteorlar
    ucak_rect.midbottom = (GENISLIK // 2, YUKSEKLIK - 20)
    skor = 0
    can = max_can
    oyun_bitti = False
    mermiler.clear()
    dusmanlar.clear()
    patlamalar.clear()
    can_kutulari.clear()
    dusman_sayaci = 0
    can_kutu_sayaci = 0
    seviye = 1
    dusman_hiz_carpani = 1.0
    mermi_sayisi = max_mermi
    mermi_kutulari.clear()
    mermi_kutu_sayaci = 0
    boss = None
    boss_aktif = False
    meteorlar = [Meteor(GENISLIK) for _ in range(20)]

def sarsinti_efekti():
    """Ekranın rastgele kaydırılmasını sağlar."""
    x_sarsinti = random.randint(-5, 5)
    y_sarsinti = random.randint(-5, 5)
    return x_sarsinti, y_sarsinti

calisiyor = True
while calisiyor:
    clock.tick(60)
    if sarsinti_suresi > 0:
        sarsinti_x, sarsinti_y = sarsinti_efekti()
        ekran.blit(arka_plan, (sarsinti_x, sarsinti_y))  # Arka planı kaydır
        sarsinti_suresi -= 1  # Sarsıntı süresi azalır
    else:
        ekran.blit(arka_plan, (0, 0))  # Arka planı normal şekilde yerleştir

    for meteor in meteorlar:
        meteor.hareket_et()
        meteor.ciz(ekran)

    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            calisiyor = False
        elif etkinlik.type == pygame.KEYDOWN:
            if etkinlik.key == pygame.K_ESCAPE:
                calisiyor = False
            elif etkinlik.key == pygame.K_SPACE and not oyun_bitti and mermi_sayisi > 0:
                lazer_sesi.play()
                mermiler.append(Mermi(ucak_rect.centerx, ucak_rect.top, mermi_resim_yolu))
                mermi_sayisi -= 1
            elif etkinlik.key == pygame.K_r and oyun_bitti:
                oyunu_sifirla()

    if not oyun_bitti:
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT] and ucak_rect.left > 0:
            ucak_rect.x -= ucak_hiz
        if tuslar[pygame.K_RIGHT] and ucak_rect.right < GENISLIK:
            ucak_rect.x += ucak_hiz

    for mermi in mermiler[:]:
        mermi.hareket_et()
        if mermi.ekran_disinda_mi():
            mermiler.remove(mermi)
        else:
            mermi.ciz(ekran)

    onceki_seviye = seviye
    seviye = skor // 20 + 1
    if seviye != onceki_seviye:
        dusman_hiz_carpani += 0.2
        if not boss_aktif:
            boss = BossDusman(GENISLIK // 2, -80)
            boss_aktif = True

    if not oyun_bitti:
        dusman_sayaci += 1
        if dusman_sayaci > 60:
            dusman_sayaci = 0
            x = random.randint(50, GENISLIK - 50)
            dusmanlar.append(Dusman(x, -40, hiz_carpani=dusman_hiz_carpani))

    if not oyun_bitti:
        can_kutu_sayaci += 1
        if can_kutu_sayaci > 300:
            can_kutu_sayaci = 0
            x = random.randint(50, GENISLIK - 50)
            can_kutulari.append(CanKutusu(x, -30))

    if not oyun_bitti:
        mermi_kutu_sayaci += 1
        if mermi_kutu_sayaci > 500:
            mermi_kutu_sayaci = 0
            x = random.randint(50, GENISLIK - 50)
            mermi_kutulari.append(MermiKutusu(x, -30))

    for dusman in dusmanlar[:]:
        dusman.hareket_et()
        for mermi in mermiler[:]:
            if dusman.rect.colliderect(mermi.rect):
                dusmanlar.remove(dusman)
                mermiler.remove(mermi)
                skor += 1
                patlamalar.append(Patlama(dusman.rect.centerx, dusman.rect.centery))
                break
        if dusman.rect.colliderect(ucak_rect):
            dusmanlar.remove(dusman)
            can -= 1
            
            # Ekranın sarsılması için
            sarsinti_suresi = max_sarsinti_suresi

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

    for patlama in patlamalar[:]:
        patlama.guncelle()
        patlama.ciz(ekran)
        if patlama.bitti_mi():
            patlamalar.remove(patlama)

    for kutu in can_kutulari[:]:
        kutu.hareket_et()
        kutu.ciz(ekran)
        vuruldu = False
        for mermi in mermiler[:]:
            if kutu.rect.colliderect(mermi.rect):
                if can < max_can:
                    can += 1
                can_kutulari.remove(kutu)
                mermiler.remove(mermi)
                vuruldu = True
                break
        if not vuruldu and kutu.ekran_disinda_mi(YUKSEKLIK):
            can_kutulari.remove(kutu)

    for mk in mermi_kutulari[:]:
        mk.hareket_et()
        mk.ciz(ekran)
        if mk.rect.colliderect(ucak_rect):
            mermi_sayisi = min(max_mermi, mermi_sayisi + 10)
            mermi_kutulari.remove(mk)
        elif mk.ekran_disinda_mi(YUKSEKLIK):
            mermi_kutulari.remove(mk)

    if boss:
        boss.hareket_et()
        boss.ciz(ekran)
        for mermi in mermiler[:]:
            if boss and boss.rect.colliderect(mermi.rect):
                mermiler.remove(mermi)
                boss.can -= 1
                if boss.can <= 0:
                    skor += 5
                    boss = None
                    boss_aktif = False
        if boss and boss.ekran_disinda_mi(YUKSEKLIK):
            boss = None
            boss_aktif = False
        ekran.blit(font.render("BOSS GELDİ!", True, (255, 0, 0)), (GENISLIK//2 - 60, 10))

    ekran.blit(ucak_resim, ucak_rect)
    ekran.blit(font.render(f"Skor: {skor}", True, (255, 255, 255)), (10, 10))
    ekran.blit(font.render(f"En Yüksek Skor: {en_yuksek_skor}", True, (200, 200, 200)), (10, 40))
    ekran.blit(font.render(f"Seviye: {seviye}", True, (255, 255, 0)), (10, 70))
    ekran.blit(font.render(f"Mermi: {mermi_sayisi}/{max_mermi}", True, (0, 200, 255)), (10, 100))
    can_bari_ciz(ekran, can, max_can)

    if oyun_bitti:
        ekran.blit(font.render("GAME OVER - R: Yeniden Başlat", True, (255, 0, 0)),
                    (GENISLIK // 2 - 160, YUKSEKLIK // 2))

    pygame.display.update()

pygame.quit()
sys.exit()