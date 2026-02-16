import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

kaggle = pd.read_csv("data/cleaned/kaggle_clean.csv")
cve = pd.read_csv("data/cleaned/cve_clean.csv")

sns.set_theme(style="whitegrid")
palette = ["#800080", "#ff69b4", "#dda0dd", "#ffb6c1", "#e6e6fa", "#ba55d3", "#c71585"]

cve["published"] = pd.to_datetime(cve["published"], errors="coerce")
cve["date"] = cve["published"].dt.date
cve_daily = cve.groupby("date").size().reset_index(name="count")

plt.figure(figsize=(12,6))
sns.lineplot(x="date", y="count", data=cve_daily, color="#ff69b4", linewidth=2.5)
plt.title("CVEs Published Over Time", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Number of CVEs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/cleaned/cve_time_series.png")
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(x="attack_type", data=kaggle, palette=palette)
plt.title("Frequency of Attack Types", fontsize=16)
plt.xlabel("Attack Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/cleaned/kaggle_attack_types.png")
plt.show()


plt.figure(figsize=(10,6))
sns.scatterplot(x="data_compromised_GB", y="attack_severity", 
                data=kaggle, hue="attack_type", palette=palette, s=100, alpha=0.8)
plt.title("Attack Severity vs Data Compromised", fontsize=16)
plt.xlabel("Data Compromised (GB)")
plt.ylabel("Attack Severity")
plt.tight_layout()
plt.savefig("data/cleaned/severity_vs_data.png")
plt.show()


industry_response = kaggle.groupby("industry")["response_time_min"].mean().reset_index()

plt.figure(figsize=(12,6))
sns.barplot(x="industry", y="response_time_min", data=industry_response, palette=palette)
plt.title("Average Response Time by Industry", fontsize=16)
plt.xlabel("Industry")
plt.ylabel("Avg Response Time (minutes)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/cleaned/industry_response.png")
plt.show()


numeric_cols = ["data_compromised_GB", "attack_duration_min", "attack_severity", "response_time_min"]
corr = kaggle[numeric_cols].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="PuRd", linewidths=0.5, fmt=".2f")
plt.title("Correlation Heatmap of Kaggle Features", fontsize=16)
plt.tight_layout()
plt.savefig("data/cleaned/kaggle_heatmap.png")
plt.show()


from collections import Counter
import re

all_text = " ".join(cve["description"].dropna().astype(str))
words = re.findall(r"\b\w+\b", all_text.lower())
common_words = Counter(words).most_common(10)
word_df = pd.DataFrame(common_words, columns=["word","count"])

plt.figure(figsize=(10,6))
sns.barplot(x="word", y="count", data=word_df, palette=palette)
plt.title("Top 10 Frequent Words in CVE Descriptions", fontsize=16)
plt.xlabel("Word")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("data/cleaned/cve_word_freq.png")
plt.show()
