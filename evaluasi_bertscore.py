import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bert_score import score

# ============================
# 1. Load Dataset
# ============================
df = pd.read_csv("eval_dataset.csv")  # Pastikan file CSV ada di folder yang sama

reference_texts = df["gold_answer"].tolist()  # jawaban benar
generated_texts = df["chatbot_answer"].tolist()     # jawaban chatbot

# ============================
# 2. Hitung BERTScore
# ============================
P, R, F1 = score(generated_texts, reference_texts, model_type="bert-base-multilingual-cased")

# ============================
# 3. Tambahkan ke DataFrame
# ============================
df["BERT_Precision"] = P.tolist()
df["BERT_Recall"] = R.tolist()
df["BERT_F1"] = F1.tolist()

# ============================
# 4. Simpan hasil
# ============================
df.to_csv("hasil_evaluasi_bertscore.csv", index=False)

print("Evaluasi selesai! File tersimpan sebagai hasil_evaluasi_bertscore.csv")

print("\nRata-rata BERTScore:")
print("Precision:", P.mean().item())
print("Recall:", R.mean().item())
print("F1:", F1.mean().item())

avg_precision = P.mean().item()
avg_recall = R.mean().item()
avg_f1 = F1.mean().item()

metrics = ["Precision", "Recall", "F1 Score"]
values = [avg_precision, avg_recall, avg_f1]

plt.figure(figsize=(8, 5))
plt.bar(metrics, values)
plt.title("Rata-rata BERTScore")
plt.ylabel("Skor")
plt.ylim(0, 1)  # BERTScore range
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Simpan gambar
plt.savefig("bertscore_chart.png", dpi=300)



plt.show()