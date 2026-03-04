# 📱 Python QR Code Generator

Bu basit ve etkili Python betiği, metin veya URL verilerini saniyeler içinde taranabilir **QR kodlarına** dönüştürmenizi sağlar. Mevcut haliyle bir YouTube video bağlantısını (`Rickroll` uyarısı! 🎵) QR koduna dönüştürecek şekilde yapılandırılmıştır.

---

## ✨ Özellikler

* **Hızlı Dönüştürme:** Saniyeler içinde `.png` formatında çıktı üretir.
* **Esnek Veri:** URL, düz metin veya iletişim bilgilerini destekler.
* **Hafif:** Sadece `qrcode` kütüphanesini kullanarak minimum sistem kaynağı harcar.

---

## 🛠️ Kurulum

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

### 1. Depoyu Klonlayın
```bash
git clone [https://github.com/kullaniciadi/qr-generator.git](https://github.com/kullaniciadi/qr-generator.git)
cd qr-generator
2. Gerekli Kütüphaneleri Yükleyin
Görüntü oluşturma desteğiyle birlikte qrcode kütüphanesini yükleyin:

Bash
pip install qrcode[pil]
🚀 Kullanım
main.py dosyasını bir metin düzenleyici ile açarak data değişkenine istediğiniz linki yazın:

Python
data = "[https://your-link-here.com](https://your-link-here.com)"
Betiği çalıştırın:

Bash
python main.py
Aynı dizinde oluşan ikinci_qr_kod.png dosyasını kontrol edin. 🎉

📂 Dosya Yapısı
main.py: QR kod oluşturma mantığını içeren ana Python betiği.

ikinci_qr_kod.png: Betik çalıştırıldıktan sonra oluşan çıktı dosyası.

📝 Kod Detayları
Projede kullanılan temel Python kodu şu şekildedir:

Python
import qrcode

# QR kodun içereceği veri
data = "[https://youtu.be/PvB0kWs2IPQ?si=73aLVAHqOb8QrIde](https://youtu.be/PvB0kWs2IPQ?si=73aLVAHqOb8QrIde)"

# QR kod nesnesini oluşturma
resim = qrcode.make(data)

# Dosya olarak kaydetme
resim.save("ikinci_qr_kod.png")
🤝 Katkıda Bulunma
Geliştirme önerileriniz veya hata bildirimleriniz için lütfen bir Issue açın veya Pull Request gönderin.

📄 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.


---
