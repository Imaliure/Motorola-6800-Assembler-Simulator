Motorola 6800 Assembler & Simulator
Live Demo

Bu proje, Motorola 6800 mikroişlemcisi için bir assembler ve simülatör sunar. Kullanıcı dostu arayüzü sayesinde, yazdığınız 6800 assembly kodlarını kolayca makine koduna çevirebilir ve simüle ederek register ve hafıza durumlarını gözlemleyebilirsiniz.

🚀 Özellikler
✅ Motorola 6800 assembly kodlarını nesne koduna çevirme (assembler)

✅ Etiket çözümleme ve adres atama

✅ Pseudo komut desteği (ORG, END)

✅ Gerçek zamanlı satır-satır çeviri

✅ Register ve hafıza durumunu simüle etme

✅ Kullanıcı dostu Flask + HTML/CSS arayüzü

![image](https://github.com/user-attachments/assets/a00b5336-bdc9-4606-a57a-eecf6c6cadc7)


📦 Kurulum
1. Gerekli ortamı kurun
bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

2. Uygulamayı çalıştır
bash
python app.py

3. Tarayıcıda aç
arduino
http://localhost:5000

🔧 Teknolojiler
Backend: Python, Flask

Frontend: HTML5, CSS3 (Flexbox), JavaScript (opsiyonel)

Deployment: Render.com (free tier)

📁 Proje Yapısı
├── app.py               # Flask sunucusu
├── assembler.py         # 6800 assembler logic
├── templates/
│   └── index.html       # HTML arayüz
├── static/
│   └── style.css        # CSS dosyası
├── requirements.txt     # Python bağımlılıkları
└── README.md            # Bu dosya
