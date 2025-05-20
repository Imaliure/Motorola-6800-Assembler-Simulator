# 🧠 Motorola 6800 Assembler & Simulator

[🟢 Canlı Demo İçin Tıklayın](https://motorola-6800-assembler-simulator.onrender.com)

Bu proje, **Motorola 6800 mikroişlemcisi** için bir Assembly dili çevirici (assembler) ve simülatör uygulamasıdır. Kullanıcılar, web arayüzü üzerinden assembly kodlarını girerek bu kodların nasıl çalıştığını görebilir; işlemcinin **register** ve **hafıza** durumlarını anlık olarak inceleyebilir.

---

## 📸 Demo Görseli

> Arayüz iki bölmeden oluşur: Sol tarafta kod giriş alanı, sağda simülasyon çıktısı yer alır.

![image](https://github.com/user-attachments/assets/df4e373d-3a6a-49b0-9719-b6d188672f61)


---

## 🚀 Özellikler

- ✅ 6800 Assembly dili desteği (örn. `LDAA`, `STAA`, `BNE`, `BRA`)
- ✅ Label (etiket) tanıma ve adres çözümleme
- ✅ Register'ların (`A`, `B`) güncel durumunu görme
- ✅ Hafıza (`0x3200` gibi) adreslerindeki veri görüntüleme
- ✅ Kodun adım adım yürütülmesi ve sonuçların eş zamanlı simülasyonu
- ✅ Modern, responsive ve kullanıcı dostu arayüz
- ✅ Flask ile geliştirilen backend, HTML/CSS ile sade tasarım

---

## 🛠️ Teknolojiler

| Katman     | Teknoloji     |
|------------|----------------|
| Backend    | Python (Flask) |
| Frontend   | HTML5, CSS3    |
| Hosting    | Render.com     |

---

## 📂 Proje Yapısı

```text
├── app.py               # Flask sunucu dosyası
├── assembler.py         # Assembly dili yorumlayıcısı (assembler motoru)
├── templates/
│   └── index.html       # Ana HTML dosyası (Flask template)
├── static/
│   └── style.css        # CSS stilleri
├── requirements.txt     # Gerekli Python paketleri
├── README.md            # Proje tanıtımı (bu dosya)
└── screenshots/
    └── demo.png         # Arayüz ekran görüntüsü
```
⚙️ Kurulum ve Çalıştırma
1. Ortamı Hazırlayın
Python ortamınızı oluşturun ve bağımlılıkları yükleyin:
bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
2. Uygulamayı Başlatın
bash
python app.py

Tarayıcınızda şu adresi açın:
arduino
http://localhost:5000


✍️Örnek Kod Kullanımı
assembly

LDAA  #$01
BNE   NOT_ZERO
LDAA  #$00
NOT_ZERO:
STAA  $3200
```
LDAA: A register’ına veri yükler.
BNE: Eğer A sıfır değilse belirli etikete dallanır.
STAA: A register’ındaki değeri belirtilen hafıza adresine yazar.
```
🌐 Canlı Uygulama
Herhangi bir şey yüklemeden doğrudan deneyin:

🔗 https://motorola-6800-assembler-simulator.onrender.com
