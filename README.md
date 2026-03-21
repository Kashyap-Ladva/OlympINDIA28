# 🇮🇳 OlympINDIA28 — India Olympic Medal Prediction System

> **How many medals can India win at the 2028 Los Angeles Olympics?**
> This project answers that question using machine learning, historical Olympic data, and multi-layer predictive intelligence.

---

##  Project Overview

OlympINDIA28 is an end-to-end data science and machine learning project that predicts India's medal performance at the 2028 Summer Olympics. It combines macroeconomic indicators, historical performance trends, sport-level intelligence, and global comparative analysis into a layered prediction architecture.

**Core Question:** *How many medals can India win at LA 2028?*

**Baseline Prediction:** ~3 medals under current structural trends
**Conditional Ceiling:** 10–15 medals with improved sporting ecosystem maturity

---

##  Architecture — Layered Intelligence System

```
Core       →  Historical India data + Weighted XGBoost model + 2028 prediction
Layer 1    →  GDP impact + Feature importance + Scenario simulation
Layer 2    →  Sport-wise medal breakdown + Probability per sport
Layer 3    →  India vs Top 5 per sport + Radar comparison
Layer 4    →  Global efficiency map + Country explorer + Host advantage
```

---

##  Project Structure

```
OlympINDIA28/
│
├── data/
│   ├── raw/                          # Source datasets
│   │   ├── olympic_history.csv       # 1896–2016 athlete-event data
│   │   ├── tokyo_2020_final.csv      # Tokyo 2020 data
│   │   ├── paris_2024_final.csv      # Paris 2024 data
│   │   ├── country_codes.csv         # NOC → country mapping
│   │   ├── socioeconomics.csv        # GDP per capita (World Bank)
│   │   └── population.csv
│   │
│   └── processed/                    # Pipeline outputs
│       ├── olympic_base.csv
│       ├── olympic_1896_2024_extended.csv
│       ├── world_summer_master_final.csv     # Master ML dataset (231 NOCs, 1896–2024)
│       ├── india_model_ready.csv             # India-specific model features
│       ├── india_sport_predictions_2028.csv  # Sport-wise 2028 predictions
│       ├── india_sport_sensitivity.csv       # Sport sensitivity matrix
│       ├── india_sport_roi.csv               # Strategic ROI per sport
│       ├── india_sport_breakout.csv          # Breakout sport candidates
│       ├── india_global_intelligence.csv     # Global comparative table
│       ├── india_opportunity_sports.csv      # Medal opportunity sports
│       └── global_sport_competition.csv      # Competitive pressure index
│
├── models/
│   ├── india_2028_model.pkl          # Tuned XGBoost — country-level predictor
│   ├── india_sport_model.pkl         # XGBoost — sport-level predictor
│   └── model_meta.json               # Best params, R2, MAE, 2028 prediction
│
├── notebooks/
│   ├── 01_data_loading_and_validation.ipynb
│   ├── 02_clean_tokyo_2020_noc.ipynb
│   ├── 03_paris_dataset.ipynb
│   ├── 04_adding_2020_2024.ipynb
│   ├── World_summer_master.ipynb
│   ├── W1_world_master_from_events.ipynb
│   ├── India_Olympic_Deep_Analysis.ipynb
│   ├── W3_world_weighted_medal_model.ipynb
│   ├── W4_Sports_Intelligence.ipynb
│   └── W5_global_comparative_intelligence.ipynb
│
├── src/
├── docs/
├── run_pipeline.py                   # Runs all notebooks in order
├── requirements.txt
└── README.md
```

---

##  Notebook Pipeline

| # | Notebook | Purpose | Output |
|---|----------|---------|--------|
| 01 | `01_data_loading_and_validation` | Load raw data, merge NOC codes, validate schema | `olympic_base.csv` |
| 02 | `02_clean_tokyo_2020_noc` | Clean Tokyo 2020 NOC codes | `tokyo_2020_final.csv` |
| 03 | `03_paris_dataset` | Process Paris 2024 data | `paris_2024_final.csv` |
| 04 | `04_adding_2020_2024` | Merge 2020 + 2024 into main dataset | `olympic_1896_2024_extended.csv` |
| W0 | `World_summer_master` | Build Summer Olympics master dataset with GDP, host boost, efficiency | `world_summer_master_final.csv` |
| W1 | `W1_world_master_from_events` | World master with all seasons (reference) | `world_master_final.csv` |
| IA | `India_Olympic_Deep_Analysis` | Deep India analysis — CAGR, GDP correlation, percentile rank, t-test, VIF | `india_model_ready.csv` |
| W3 | `W3_world_weighted_medal_model` | Multi-model comparison + tuned XGBoost + 2028 prediction + scenario simulation | `india_2028_model.pkl` |
| W4 | `W4_Sports_Intelligence` | Sport-level XGBoost + sensitivity matrix + ROI + breakout detector | `india_sport_predictions_2028.csv` |
| W5 | `W5_global_comparative_intelligence` | Global sport power index + closeness score + strategic classification | `india_global_intelligence.csv` |

---

##  ML Models

### Layer 1 — Country-Level Model (W3)
- **Algorithm:** XGBoost (tuned via 243-combination grid search)
- **Features:** `career_avg`, `delta_last`, `gdp_pc_log`
- **Training:** Weighted by recency (2024=4x, 2020=3x, 2016=2x, others=1x)
- **Test set:** 2024 Olympics results
- **Feature Importance:** career_avg (55%) > delta_last (31%) > GDP (12%)

### Layer 2 — Sport-Level Model (W4)
- **Algorithm:** XGBoost (sport × year matrix)
- **Features:** `career_avg`, `delta_last` per sport
- **Output:** Predicted medals per sport for 2028
- **Scaled** to match Layer 1 total prediction

---

##  Key Findings

1. **Baseline 2028 prediction: ~3 medals** under current structural trends
2. **GDP explains ~12% of medal variance** — sporting ecosystem maturity matters more
3. **India structurally underperforms** relative to its GDP rank — policy and infrastructure gaps exist
4. **Post-2016 medal mean is significantly higher** than pre-2016 (Welch t-test confirmed)
5. **Conditional ceiling: 10–15 medals** if career average reaches 3.5+ and momentum improves
6. **Structural breakout scenario: 15–20 medals** — requires policy reform + funding surge
7. **Top opportunity sports:** Shooting, Badminton, Wrestling, Boxing, Athletics

---

## ⚙️ Setup & Installation

```bash
# Clone the repo
git clone https://github.com/Kashyap-Ladva/OlympINDIA28.git
cd OlympINDIA28

# Install dependencies
pip install -r requirements.txt

# Run full pipeline
python run_pipeline.py
```

### Requirements
```
pandas
numpy
scikit-learn
xgboost
matplotlib
seaborn
statsmodels
scipy
jupyter
nbconvert
```

---

##  Run Pipeline

```bash
python run_pipeline.py
```

Executes all 10 notebooks in order. Outputs are saved to `data/processed/` and `models/`.

---

##  Roadmap

- [x] Data collection (1896–2024)
- [x] Data cleaning + feature engineering
- [x] World Summer Master dataset
- [x] India deep analysis
- [x] Country-level XGBoost model
- [x] Sport-level prediction model
- [x] Global comparative intelligence
- [ ] Streamlit dashboard (in progress)
- [ ] Deployment on Streamlit Cloud
- [ ] Research paper (planned)

---

##  Author

**Kashyap Ladva**
B.E. Computer Engineering 
Data Science and Machine Learning
[GitHub](https://github.com/Kashyap-Ladva) | [LinkedIn](https://linkedin.com/in/kashyap-ladva)

---

> ⚠️ *This README is temporary. It will be updated after the Streamlit dashboard is deployed with live app link, screenshots, and demo GIF.*
