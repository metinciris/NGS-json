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

## Gereksinimler

- Python 3.6+
- pandas
- numpy
- tkinter

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.
