# NGS-json

NGS (Next Generation Sequencing) JSON dosyaları için Kalite Değerlendirme Aracı

## Açıklama

Bu araç, NGS verilerinin kalite değerlendirmesini yapmak için JSON dosyalarını analiz eder ve sonuçları kullanıcı dostu bir formatta sunar. Tkinter arayüzü kullanılarak sonuçlar görselleştirilir ve WhatsApp uyumlu bir rapor oluşturulur.

## Özellikler

- JSON dosyalarından kalite verilerini okuma
- Kalite metriklerini hesaplama (Q30, Q40, GC içeriği, vb.)
- Tkinter ile kullanıcı dostu arayüz
- WhatsApp uyumlu rapor oluşturma
- Farklı NGS panel türleri için beklenen değerler

## Kullanım

1. Gerekli kütüphaneleri yükleyin: `pip install pandas numpy tkinter`
2. `json.py` dosyasını çalıştırın: `python json.py`
3. Açılan pencereden analiz etmek istediğiniz JSON dosyalarını seçin
4. Sonuçları görüntüleyin ve kopyalayın


## Kullanım

İşte örnek hastalar üzerinden oluşturulmuş renkli ve görsel bir kalite değerlendirme raporu:

📊 *Genel Kalite Değerlendirme*

🟢 *Hasta-A (FFPE-001)*
🟢 %Q30: 98.32
🟢 %Q40: 94.15
🟢 Ortalama Kalite Skoru: 46.78
🟢 Hata Oranı: 2.14
🟢 Okuma Sayısı (Milyon): 35.62
🧬 Guanin-Sitozin İçeriği: Normal (52.18%)
🔬 Adaptör Yüzdesi: 0.82%
📏 Ortalama Okuma Uzunluğu: 151.0 baz çifti
🔢 Toplam Baz Sayısı: 5.38 milyar
📊 Puan: 97.45/100 🟢

🟡 *Hasta-B (FFPE-002)*
🟢 %Q30: 95.76
🟢 %Q40: 89.23
🟡 Ortalama Kalite Skoru: 43.91
🟡 Hata Oranı: 5.87
🟡 Okuma Sayısı (Milyon): 22.45
🧬 Guanin-Sitozin İçeriği: Yüksek (68.73%)
🔬 Adaptör Yüzdesi: 1.24%
📏 Ortalama Okuma Uzunluğu: 150.8 baz çifti
🔢 Toplam Baz Sayısı: 3.39 milyar
📊 Puan: 84.62/100 🟡

🔴 *Hasta-C (FFPE-003)*
🟡 %Q30: 92.14
🟡 %Q40: 82.56
🔴 Ortalama Kalite Skoru: 40.23
🔴 Hata Oranı: 8.92
🔴 Okuma Sayısı (Milyon): 11.87
🧬 Guanin-Sitozin İçeriği: Yüksek (71.45%)
🔬 Adaptör Yüzdesi: 3.56%
📏 Ortalama Okuma Uzunluğu: 149.5 baz çifti
🔢 Toplam Baz Sayısı: 1.77 milyar
📊 Puan: 68.31/100 🔴

🔹 *Beklenen Değerler:*
   - Solid Tümör Paneli: 15M - 40M
   - Akciğer Kanseri Paneli: 15M - 30M
   - Hematoonkolojik Panel: 50M - 100M
   - Genel Füzyon Paneli: 20M - 50M

🔹 *Kalite Parametreleri:*
   - %Q30: ≥ 85 iyi
   - %Q40: ≥ 75 kabul edilebilir
   - Ortalama Kalite Skoru: ≥ 45 olmalı
   - Hata Oranı: ≤ 5 olmalı
   - Guanin-Sitozin İçeriği: %40-%60 arası ideal
   - Adaptör Yüzdesi: < %10 olmalı
   - Ortalama Okuma Uzunluğu:
     -  Solid Tümör Paneli: 100-200 baz çifti
     -  Akciğer Kanseri Paneli: 120-180 baz çifti
     -  Hematoonkolojik Panel: 150-250 baz çifti
     -  Genel Füzyon Paneli: 100-300 baz çifti


## Gereksinimler

- Python 3.6+
- pandas
- numpy
- tkinter

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.
