import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog, scrolledtext, Button

def calculate_weighted_quality_score(q30, mismatch, quality_score,
                                     weight_q30=40, weight_mismatch=25, weight_quality=35,
                                     mismatch_threshold=12, max_quality_score=50):
    if q30 is None or mismatch is None or quality_score is None:
        return None

    score_q30 = (q30 / 100) * weight_q30
    score_mismatch = max(0, (mismatch_threshold - mismatch)) / mismatch_threshold * weight_mismatch
    score_quality = (min(quality_score, max_quality_score) / max_quality_score) * weight_quality

    total_score = score_q30 + score_mismatch + score_quality
    return round(total_score, 2)

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

def load_json_data(file_paths):
    data = []
    for file_path in file_paths:
        try:
            with open(file_path, "r") as f:
                json_data = json.load(f)
            
            sample_name = json_data.get("SampleName", "Bilinmiyor")
            file_name = file_path.split("/")[-1].replace(".json", "")
            q30 = round(json_data["Occurrences"][0]["PercentQ30"], 2)
            q40 = round(json_data["Occurrences"][0]["PercentQ40"], 2)
            mismatch = round(json_data["Occurrences"][0]["PercentMismatch"], 2)
            quality_score = round(json_data["Occurrences"][0]["QualityScoreMean"], 2)
            total_reads = round(json_data.get("NumPolonies", 0) / 1_000_000, 2)
            
            total_score = calculate_weighted_quality_score(q30, mismatch, quality_score)
            quality_label = get_quality_label(total_score)
            
            data.append([sample_name, file_name, q30, q40, quality_score, mismatch, total_reads, total_score, quality_label])
        except Exception:
            data.append([file_path, "Dosya Hatası", "", "", "", "", "", None, "❌"])
    
    df = pd.DataFrame(data, columns=["Sample", "File Name", "%Q30", "%Q40", "Quality Score Mean", "Mismatch %", "Total Reads (M)", "Total Score", "Kalite Değerlendirmesi"])
    return df

def generate_whatsapp_report(df):
    report = "📊 **Genel Kalite Değerlendirme**\n\n"
    report += "⚠️ Not: Bu örnekler parafin kesitlerinden elde edilmiştir. Kalite ölçütleri buna göre değerlendirilmelidir.\n\n"
    for _, row in df.iterrows():
        report += f"{row['Kalite Değerlendirmesi']} **{row['Sample']} ({row['File Name']})**\n"
        report += f"{get_quality_label(row['%Q30'])} %Q30: {row['%Q30']}\n"
        report += f"{get_quality_label(row['%Q40'])} %Q40: {row['%Q40']}\n"
        report += f"{get_quality_label(row['Quality Score Mean'])} Ortalama Kalite Skoru: {row['Quality Score Mean']}\n"
        report += f"{get_quality_label(row['Mismatch %'], high_best=False)} Hata Oranı: {row['Mismatch %']}\n"
        report += f"{get_quality_label(row['Total Reads (M)'])} Okuma Sayısı (Milyon): {row['Total Reads (M)']}M\n"
        report += f"Puan: {row['Total Score']}/100 {row['Kalite Değerlendirmesi']}\n\n"
    
    return report

def copy_to_clipboard(report, root):
    root.clipboard_clear()
    root.clipboard_append(report)
    root.update()

def display_results(report):
    root = tk.Tk()
    root.title("Genel Kalite Değerlendirme Raporu")
    root.geometry("600x500")
    
    text_area = scrolledtext.ScrolledText(root, width=70, height=25, wrap=tk.WORD)
    text_area.insert(tk.INSERT, report)
    text_area.pack(padx=10, pady=10, expand=True, fill='both')
    text_area.config(state=tk.DISABLED)
    
    copy_button = Button(root, text="📋 Kopyala", command=lambda: copy_to_clipboard(report, root))
    copy_button.pack(pady=5)
    
    root.mainloop()

def select_files():
    return filedialog.askopenfilenames(title="JSON Dosyalarını Seç", filetypes=[("JSON files", "*.json")])

def main():
    json_files = select_files()
    if not json_files:
        print("Dosya seçilmedi.")
        return
    
    df = load_json_data(json_files)
    report = generate_whatsapp_report(df)
    display_results(report)
    
    print("\n📊 WhatsApp Formatında Kalite Değerlendirme Raporu:\n")
    print(report)

if __name__ == "__main__":
    main()
