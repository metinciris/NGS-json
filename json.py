import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog, scrolledtext, Button
import numpy as np

def get_quality_label(value, high_best=True, is_paraffin=True):
    if value is None:
        return "❌"
    if high_best:
        if is_paraffin:
            if value >= 85:
                return "🟢"
            elif value >= 75:
                return "🟡"
            elif value >= 65:
                return "🟠"
            else:
                return "🔴"
        else:
            if value >= 90:
                return "💎"
            elif value >= 80:
                return "🥇"
            elif value >= 70:
                return "🥈"
            elif value >= 60:
                return "🥉"
            else:
                return "💩"
    else:
        if is_paraffin:
            if value <= 5:
                return "🟢"
            elif value <= 8:
                return "🟡"
            elif value <= 12:
                return "🟠"
            else:
                return "🔴"
        else:
            if value <= 2:
                return "💎"
            elif value <= 5:
                return "🥇"
            elif value <= 8:
                return "🥈"
            elif value <= 12:
                return "🥉"
            else:
                return "💩"

def calculate_weighted_quality_score(q30, mismatch, quality_score, total_reads,
                                     weight_q30=30, weight_mismatch=20, weight_quality=20, weight_reads=30,
                                     mismatch_threshold=10, max_quality_score=50, expected_reads=15):
    if q30 is None or mismatch is None or quality_score is None or total_reads is None:
        return None

    score_q30 = (q30 / 100) * weight_q30
    score_mismatch = max(0, (mismatch_threshold - mismatch)) / mismatch_threshold * weight_mismatch
    score_quality = (min(quality_score, max_quality_score) / max_quality_score) * weight_quality
    score_reads = min(total_reads / expected_reads, 1) * weight_reads

    total_score = score_q30 + score_mismatch + score_quality + score_reads
    return round(total_score, 2)

def calculate_gc_content(gc_histogram):
    total_bases = sum(count * gc for gc, count in enumerate(gc_histogram))
    total_reads = sum(gc_histogram)
    return round((total_bases / (total_reads * 151)) * 100, 2) if total_reads > 0 else 0

def load_json_data(json_files):
    data = []
    
    for json_path in json_files:
        try:
            with open(json_path, "r") as f:
                json_data = json.load(f)
            
            sample_name = json_data.get("SampleName", "Bilinmiyor")
            file_name = json_path.split("/")[-1].replace(".json", "")
            q30 = round(json_data["Occurrences"][0]["PercentQ30"], 2)
            q40 = round(json_data["Occurrences"][0]["PercentQ40"], 2)
            mismatch = round(json_data["Occurrences"][0]["PercentMismatch"], 2)
            quality_score = round(json_data["Occurrences"][0]["QualityScoreMean"], 2)
            total_reads = round(json_data.get("NumPolonies", 0) / 1_000_000, 2)

            gc_content = calculate_gc_content(json_data["Occurrences"][0]["Reads"][0]["PerReadGCCountHistogram"])
            mean_read_length = round(json_data["Occurrences"][0]["Reads"][0]["MeanReadLength"], 2)
            total_bases = round(total_reads * mean_read_length, 2)

            total_score = calculate_weighted_quality_score(q30, mismatch, quality_score, total_reads)
            quality_label = get_quality_label(total_score)

            data.append([sample_name, file_name, q30, q40, quality_score, mismatch, total_reads, gc_content, mean_read_length, total_bases, total_score, quality_label])
        
        except Exception:
            data.append([json_path, "Dosya Hatası", "", "", "", "", "", "", "", "", None, "❌"])

    df = pd.DataFrame(data, columns=["Sample", "File Name", "%Q30", "%Q40", "Quality Score Mean", "Mismatch %",
                                     "Total Reads (M)", "GC Content %", "Mean Read Length", "Total Bases (G)", "Total Score", "Kalite Değerlendirmesi"])
    return df

def display_results(report):
    root = tk.Tk()
    root.title("Genel Kalite Değerlendirme Raporu")
    root.geometry("600x500")
    
    text_area = scrolledtext.ScrolledText(root, width=70, height=25, wrap=tk.WORD)
    text_area.insert(tk.INSERT, report)
    text_area.pack(padx=10, pady=10, expand=True, fill='both')
    
    copy_button = Button(root, text="📋 Kopyala", command=lambda: root.clipboard_append(report))
    copy_button.pack(pady=5)
    
    root.mainloop()

def generate_whatsapp_report(df):
    report = "📊 *Genel Kalite Değerlendirme*\n\n"
    
    for _, row in df.iterrows():
        report += f"{row['Kalite Değerlendirmesi']} *{row['Sample']} ({row['File Name']})*\n"
        report += f"{get_quality_label(row['%Q30'])} %Q30: {row['%Q30']}\n"
        report += f"{get_quality_label(row['%Q40'])} %Q40: {row['%Q40']}\n"
        report += f"{get_quality_label(row['Quality Score Mean'])} Ortalama Kalite Skoru: {row['Quality Score Mean']}\n"
        report += f"{get_quality_label(row['Mismatch %'], high_best=False)} Hata Oranı: {row['Mismatch %']}\n"
        report += f"{get_quality_label(row['Total Reads (M)'])} Okuma Sayısı (Milyon): {row['Total Reads (M)']}\n"
        report += f"🧬 Guanin-Sitozin İçeriği: {'Yüksek' if row['GC Content %'] > 60 else 'Normal'} ({row['GC Content %']}%)\n"
        report += f"📏 Ortalama Okuma Uzunluğu: {row['Mean Read Length']} baz çifti\n"
        report += f"🔢 Toplam Baz Sayısı: {row['Total Bases (G)']} milyar\n"
        report += f"📊 Puan: {row['Total Score']}/100 {row['Kalite Değerlendirmesi']}\n\n"

    report += "🔹 *Beklenen Değerler:*\n"
    report += "   - Solid Tümör Paneli: 15M - 40M\n"
    report += "   - Akciğer Kanseri Paneli: 15M - 30M\n"
    report += "   - Hematoonkolojik Panel: 50M - 100M\n"
    report += "   - Genel Füzyon Paneli: 20M - 50M\n\n"

    report += "🔹 *Kalite Parametreleri:*\n"
    report += "   - %Q30: ≥ 85 iyi\n"
    report += "   - %Q40: ≥ 75 kabul edilebilir\n"
    report += "   - Ortalama Kalite Skoru: ≥ 45 olmalı\n"
    report += "   - Hata Oranı: ≤ 5 olmalı\n"
    report += "   - Guanin-Sitozin İçeriği: %40-%60 arası ideal\n"
    report += "   - Ortalama Okuma Uzunluğu:\n"
    report += "     -  Solid Tümör Paneli: 100-200 baz çifti\n"
    report += "     -  Akciğer Kanseri Paneli: 120-180 baz çifti\n"
    report += "     -  Hematoonkolojik Panel: 150-250 baz çifti\n"
    report += "     -  Genel Füzyon Paneli: 100-300 baz çifti\n"

    return report

def main():
    json_files = filedialog.askopenfilenames(title="JSON Dosyalarını Seç", filetypes=[("JSON files", "*.json")])
    
    df = load_json_data(json_files)
    report = generate_whatsapp_report(df)
    display_results(report)
    
if __name__ == "__main__":
    main()
