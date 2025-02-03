# NGS-json
NGS json dosyaları Kalite Değerlendirme Aracı

Bu proje, **NGS (Next-Generation Sequencing) verileri** için temel kalite metriklerini hızlı ve okunabilir şekilde raporlamaya yarayan bir Python aracıdır. JSON formatında gelen verileri analiz ederek **%Q30, %Q40, Ortalama Kalite Skoru, Hata Oranı ve Okuma Sayısı** gibi kritik bilgileri içerir.

## 🚀 Özellikler
- JSON formatındaki **NGS kalite verilerini hızlı bir şekilde işler**.
- **Her veri için kalite değerlendirmesi yapar** ve uygun bir **emoji kodlaması** ile sunar.
- **WhatsApp için optimize edilmiş çıktı formatı** üretir.
- **Windows 10-11 üzerinde çalışır** ve doğrudan kopyalanarak Web WhatsApp üzerinden paylaşılabilir.
- **Kapsamlı ve anlaşılır sonuçlar sağlar.**

## 📂 Girdi Dosyaları
Bu araç, **NGS okuma kalite metriklerini içeren JSON dosyalarını** işler. Örnek bir JSON formatı şu şekildedir:

```json
{
    "SampleName": "Dummy-Sample",
    "Occurrences": [
        {
            "PercentQ30": 96.5,
            "PercentQ40": 89.4,
            "QualityScoreMean": 42.8,
            "PercentMismatch": 4.2
        }
    ],
    "NumPolonies": 15230000
}
```

## 📜 Çıktı Formatı
Aracın ürettiği WhatsApp uyumlu çıktı formatı örneği:

```
📊 **Genel Kalite Değerlendirme**

🥈 *VAKA44 (MP44_stats)*
   🥈 %Q30: 97.57
   🥈 %Q40: 92.19
   🥈 Ortalama Kalite Skoru: 43.28
   🥈 Hata Oranı: 5.4
   🥈 Okuma Sayısı (Milyon): 18.94M
   🥈 Puan: 78.8/100

🥇 *VAKA48 (MP48_stats)*
   🥇 %Q30: 97.27
   🥇 %Q40: 91.42
   🥇 Ortalama Kalite Skoru: 43.16
   🥇 Hata Oranı: 4.44
   🥇 Okuma Sayısı (Milyon): 15.53M
   🥇 Puan: 81.48/100
```

## 📥 Kurulum & Kullanım

1. **Python 3.x sürümünü yükleyin.**
2. Gerekli kütüphaneleri yükleyin:
   ```sh
   pip install pandas tkinter
   ```
3. **Python betiğini çalıştırın** ve JSON dosyalarını seçin:
   ```sh
   python ngs_quality_analysis.py
   ```
4. Çıktıyı kopyalayarak Web WhatsApp üzerinde paylaşabilirsiniz.

## 📌 Gelecek Güncellemeler
✅ **Hematoonkolojik Panel ve Genel Füzyon Paneli desteği** eklenecek.  
✅ **Variant Allele Frequency (VAF) ve CNV analizleri** için ek değerlendirmeler yapılacak.  

## 📄 Lisans
Bu proje **MIT Lisansı** ile sunulmaktadır. Herkesin kullanımına açıktır. 🎯

