
# 🛩️ Uçak Savaş Oyunu

Uçak Savaş Oyunu, Python ve Pygame kullanılarak geliştirilen 2D arcade tarzı bir nişancı oyunudur. Oyuncu, yukarıdan gelen uzaylı düşmanları yok ederek skor kazanmaya çalışır. Oyunda seviye sistemi, boss düşmanlar, sınırlı mermi ve çeşitli güçlendirici kutular gibi özelliklerle heyecanlı bir savaş atmosferi sunulmaktadır.

---

## 🎮 Oynanış

- **Kontroller:**
  - Hareket: `W`, `A`, `S`, `D` veya Yön Tuşları
  - Ateş Et: `SPACE`
  - Oyunu Yeniden Başlat: `R`
  - Menüden Çıkış: `ESC`

- **Oyun Mekanikleri:**
  - Oyuncu bir uçak ile ekranın alt kısmında sola/sağa hareket ederek düşmanlara mermi fırlatır.
  - Mermiler sınırlıdır, yukarıdan gelen mermi kutuları ile yenilenir.
  - Can azalırsa, can kutuları ile artırılabilir.
  - Seviye atladıkça düşmanlar hızlanır.
  - Her 20 skor sonrası "Boss Düşman" belirir, 3 mermi ile yok edilir.
  - Yavaşlatma kutusu vurulursa düşmanlar geçici süreyle yavaşlar.

---

## 🧩 Oyun Özellikleri

- 🔫 **Sınırlı Mermi:** Merminiz biterse yukarıdan gelen kutularla doldurabilirsiniz.
- ❤️ **Can Sistemi:** Oyuncunun canı 3'tür, can kutusu ile dolabilir.
- 🧊 **Yavaşlatma:** Ekrandaki tüm düşmanları belirli süre yavaşlatan kutu.
- 👾 **Boss Düşman:** Her 20 skor sonrası ortaya çıkar, 3 isabetle yok edilir.
- 🎧 **Ses Efektleri:** Ateş, vurulma ve boss ölümü için özel efektler içerir.

---

## 📸 Ekran Görüntüleri

### 🎯 Ana Menü - Oyuna Başlangıç
![Ana Menü](IMG/Ekran%20Resmi%202025-04-23%2015.41.55.png)

### 🕹️ Oyun İçi - Can Fullken Savaş
![Oyun Can 3/3](IMG/Ekran%20Resmi%202025-04-23%2015.42.30.png)

### ☠️ Game Over - Can 0
![Oyun Bitti](IMG/Ekran%20Resmi%202025-04-23%2015.42.20.png)

### 🚨 Boss Geldi - Yavaşlatma Aktif
![Boss Düşman](IMG/Ekran%20Resmi%202025-04-23%2015.53.21.jpg)

### 💥 Boss Ölümü ve Game Over
![Boss Öldü](IMG/Ekran%20Resmi%202025-04-23%2015.53.25.jpg)

---

## ⚙️ Kurulum

1. Python 3.x sisteminizde kurulu olmalı.
2. Terminale şu komutu yazın:
```bash
pip install pygame
```
3. Proje klasörüne girin ve oyunu başlatın:
```bash
python main.py
```

---

## 👨‍💻 Geliştiriciler

Bu oyun Pamukkale Üniversitesi Bilgisayar Mühendisliği öğrencileri tarafından geliştirilmiştir:

- **Beyzanur Merkepçioğlu**
- **Zilan Aykal**
- **Şevval Büyükyalıoğlu**

🔗 [GitHub Proje Sayfası](https://github.com/zilanaykal14/oyunProje)

---

## 📄 Lisans

Bu proje yalnızca eğitim, geliştirme ve akademik kullanım içindir. Tüm hakları geliştiricilerine aittir.

---

Her türlü geri bildirim ve katkı için GitHub sayfasını ziyaret edebilirsiniz. İyi eğlenceler ve bol skorlar! 🎯
