# Cybersecurity ELT Pipeline

## Overview

This project implements a modular ELT pipeline for cybersecurity data using:

- CIRCL CVE Search API (recent vulnerabilities)
- Kaggle Cybersecurity Incidents dataset
- Google Trends (search interest in cybersecurity topics)

## Structure

- `extract_api.py` → CVE API
- `extract_kaggle.py` → Kaggle dataset
- `extract_trends.py` → Google Trends
- `load_data.py` → Save processed data
- `run_pipeline.py` → Orchestrates pipeline
- `config.py` → Configuration parameters

## Output

- Raw data → `data/raw/`
- Processed data → `data/processed/`

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn requests pytrends
   ```
2. Run Files :
   ```bash
   python run_pipeline.py , python transform_clean.py ,  python analysis_visuals.py
   ```

# Part 2: Transform, Clean, and Analyze

I checked missing values and duplicates in both Kaggle and CVE datasets. I cleaned them by filling missing values with "Unknown", removing duplicates, and standardizing date formats. I generated summary statistics to understand the data better.

For analysis, I created many visualizations like:

1. A time-series chart showing CVEs published per year.
2. A bar chart showing incidents by industry from the Kaggle dataset.
3. A scatter plot showing the relationship between CVE publication year and attack types.

The cleaned datasets are stored in `data/cleaned/` and the visualizations are saved as PNG files in the same folder.
