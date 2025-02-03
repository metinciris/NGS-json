import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog, scrolledtext, Button

def calculate_weighted_quality_score(q30, mismatch, quality_score,
                                     weight_q30=30, weight_mismatch=30, weight_quality=40,
                                     mismatch_threshold=10, max_quality_score=50):
    if q30 is None or mismatch is None or quality_score is None:
        return None

    score_q30 = (q30 / 100) * weight_q30
    score_mismatch = max(0, (mismatch_threshold - mismatch)) / mismatch_threshold * weight_mismatch
    score_quality = (min(quality_score, max_quality_score) / max_quality_score) * weight_quality

    total_score = score_q30 + score_mismatch + score_quality
    return round(total_score, 2)

def get_quality_label(value, high_best=True):
    if value is None:
        return "❌"
    if high_best:
        if value >= 85:
            return "🟢"
        elif value >= 75:
            return "🟡"
        elif value >= 65:
            return "🟠"
        else:
            return "🔴"
    else:
        if value <= 5:
            return "🟢"
        elif value <= 8:
            return "🟡"
        elif value <= 12:
            return "🟠"
        else:
            return "🔴"

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

            total_score = calculate_weighted_quality_score(q30, mismatch, quality_score)
            quality_label = get_quality_label(total_score)

            data.append([quality_label + " " + sample_name + " (" + file_name + ")",
                         "🟢 %Q30: " + str(q30),
                         "🟢 %Q40: " + str(q40),
                         "🔴 Ortalama Kalite Skoru: " + str(quality_score),
                         "🟡 Hata Oranı: " + str(mismatch),
                         "🔴 Okuma Sayısı (Milyon): " + str(total_reads),
                         "📊 Puan: " + str(total_score) + "/100 " + quality_label])
        except Exception:
            data.append([json_path, "Dosya Hatası"])

    return data

def display_results(report):
    root = tk.Tk()
    root.title("Genel Kalite Değerlendirme Raporu")
    root.geometry("600x500")
    
    text_area = scrolledtext.ScrolledText(root, width=70, height=25, wrap=tk.WORD)
    text_area.insert(tk.INSERT, report)
    text_area.pack(padx=10, pady=10, expand=True, fill='both')
    text_area.config(state=tk.DISABLED)
    
    copy_button = Button(root, text="📋 Kopyala", command=lambda: root.clipboard_append(report))
    copy_button.pack(pady=5)
    
    root.mainloop()

def main():
    json_files = filedialog.askopenfilenames(title="JSON Dosyalarını Seç", filetypes=[("JSON files", "*.json")])
    
    data = load_json_data(json_files)
    report = "\n\n".join(["\n".join(sample) for sample in data])
    display_results(report)
    
if __name__ == "__main__":
    main()
