# 🇮🇳 OlympINDIA28 — India Olympic Medal Prediction System

> **How many medals can India win at the 2028 Los Angeles Olympics?**
> 
> This project answers that question using machine learning, historical Olympic data (1896–2024), and multi-layer predictive intelligence to forecast India's performance at LA 2028.

---

## 📊 Quick Overview

**OlympINDIA28** is an end-to-end data science and machine learning project that predicts India's medal performance at the 2028 Summer Olympics. It combines:

- 📈 **Macroeconomic indicators** (GDP per capita, population trends)
- 🏅 **Historical performance analysis** (128 years of Olympic data from 1896–2024)
- 🎯 **Sport-level intelligence** (sport-wise medal probabilities & opportunity detection)
- 🌍 **Global comparative analysis** (India vs. top performers per sport)
- 🤖 **Advanced ML models** (XGBoost with hyperparameter tuning & scenario simulation)

### 🎯 Key Predictions

| Scenario | Medal Count | Conditions |
|----------|------------|-----------|
| **Baseline** | ~3 medals | Current structural trends & policy |
| **Conditional Ceiling** | 10–15 medals | Improved sporting ecosystem & training |
| **Structural Breakout** | 15–20 medals | Major policy reform + funding surge |

---

## 🏗️ Architecture — 5-Layer Intelligence System

The model uses a **multi-dimensional prediction framework** with interconnected layers:

```
┌─────────────────────────────────────────────────────────────┐
│  🎯 CORE PREDICTION LAYER                                   │
│  Historical India data + Weighted XGBoost + 2028 Forecast   │
└─────────────────────────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────────────────────────┐
│  1️⃣  ECONOMIC IMPACT ANALYSIS                               │
│  GDP correlation + Feature importance + Scenario simulation │
└─────────────────────────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────────────────────────┐
│  2️⃣  SPORT INTELLIGENCE ENGINE                              │
│  Sport-wise breakdown + Per-sport probabilities             │
│  + ROI matrix + Breakout detection                          │
└─────────────────────────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────────────────────────┐
│  3️⃣  GLOBAL COMPETITIVE POSITIONING                         │
│  India vs. Top 5 per sport + Radar comparison               │
│  + Competitive pressure index                               │
└─────────────────────────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────────────────────────┐
│  4️⃣  STRATEGIC INSIGHTS & OPPORTUNITIES                     │
│  Global efficiency mapping + Country explorer               │
│  + Host advantage analysis + Opportunity identification     │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
OlympINDIA28/
│
├── 📊 data/
│   ├── raw/                                    # Original datasets
│   │   ├── olympic_history.csv                 # 1896–2016 athlete-event records
│   │   ├── tokyo_2020_final.csv                # Tokyo 2020 Olympic results
│   │   ├── paris_2024_final.csv                # Paris 2024 Olympic results
│   │   ├── country_codes.csv                   # NOC ↔ country mapping
│   │   ├── socioeconomics.csv                  # GDP & socioeconomic data
│   │   └── population.csv                      # Population trends
│   │
│   └── processed/                              # Pipeline output datasets
│       ├── olympic_base.csv
│       ├── olympic_1896_2024_extended.csv
│       ├── world_summer_master_final.csv       # Master ML dataset (231 NOCs, 1896–2024)
│       ├── india_model_ready.csv               # India-specific ML features
│       ├── india_sport_predictions_2028.csv    # Sport-wise 2028 predictions
│       ├── india_sport_sensitivity.csv         # Feature sensitivity matrix
│       ├── india_sport_roi.csv                 # Strategic ROI per sport
│       ├── india_sport_breakout.csv            # Breakout opportunity sports
│       ├── india_global_intelligence.csv       # Global comparative analysis
│       ├── india_opportunity_sports.csv        # High-impact opportunity sports
│       └── global_sport_competition.csv        # Competitive pressure index
│
├── 🤖 models/
│   ├── india_2028_model.pkl                    # Tuned XGBoost (country-level)
│   ├── india_sport_model.pkl                   # XGBoost (sport-level)
│   └── model_meta.json                         # Model metadata & metrics
│
├── 📓 notebooks/                               # Analysis & model notebooks
│   ├── 01_data_loading_and_validation.ipynb    # Data ingestion & validation
│   ├── 02_clean_tokyo_2020_noc.ipynb           # NOC code cleaning
│   ├── 03_paris_dataset.ipynb                  # Paris 2024 preprocessing
│   ├── 04_adding_2020_2024.ipynb               # Historical integration
│   ├── World_summer_master.ipynb                # Master dataset creation
│   ├── W1_world_master_from_events.ipynb        # Comprehensive world data
│   ├── India_Olympic_Deep_Analysis.ipynb        # India-specific analysis
│   ├── W3_world_weighted_medal_model.ipynb      # Country-level model training
│   ├── W4_Sports_Intelligence.ipynb             # Sport-level model & analysis
│   └── W5_global_comparative_intelligence.ipynb # Global comparison engine
│
├── 📚 src/                                      # Source code modules
├── 📖 docs/                                     # Documentation files
├── app.py                                       # Streamlit web application
├── run_pipeline.py                              # Full pipeline orchestrator
├── requirements.txt                             # Python dependencies
└── README.md
```

---

## 🔄 Data Processing Pipeline

The project uses a **sequential 10-stage notebook pipeline** to transform raw data into predictions:

| Stage | Notebook | Purpose | Output |
|-------|----------|---------|--------|
| **01** | `01_data_loading_and_validation` | Load raw data, merge NOC codes, validate schema | `olympic_base.csv` |
| **02** | `02_clean_tokyo_2020_noc` | Standardize NOC codes for Tokyo 2020 | `tokyo_2020_final.csv` |
| **03** | `03_paris_dataset` | Process Paris 2024 Olympic data | `paris_2024_final.csv` |
| **04** | `04_adding_2020_2024` | Integrate 2020 + 2024 with historical data | `olympic_1896_2024_extended.csv` |
| **W0** | `World_summer_master` | Build comprehensive Summer Olympics dataset | `world_summer_master_final.csv` |
| **W1** | `W1_world_master_from_events` | Create all-seasons master dataset (reference) | `world_master_final.csv` |
| **IA** | `India_Olympic_Deep_Analysis` | Deep analysis: CAGR, GDP correlation, statistics | `india_model_ready.csv` |
| **W3** | `W3_world_weighted_medal_model` | Model comparison, XGBoost tuning, 2028 forecast | `india_2028_model.pkl` |
| **W4** | `W4_Sports_Intelligence` | Sport-level modeling, ROI, breakout detection | `india_sport_predictions_2028.csv` |
| **W5** | `W5_global_comparative_intelligence` | Global sport power index, competitive positioning | `india_global_intelligence.csv` |

---

## 🤖 Machine Learning Models

### Country-Level Model (Layer W3)
- **Algorithm:** XGBoost regression (grid search tuned: 243 combinations)
- **Features:** 
  - `career_avg` — Historical average medals per Olympic cycle (55% importance)
  - `delta_last` — Recent performance momentum (31% importance)
  - `gdp_pc_log` — GDP per capita (12% importance)
- **Training Strategy:** Weighted by recency (2024=4x, 2020=3x, 2016=2x, older=1x)
- **Validation:** 2024 Paris Olympics (unseen test set)
- **Output:** 2028 LA prediction + confidence intervals

### Sport-Level Model (Layer W4)
- **Algorithm:** XGBoost per sport (sport × year matrix)
- **Features:** `career_avg` and `delta_last` per sport
- **Output:** Predicted medals per sport for 2028
- **Reconciliation:** Scaled to align with country-level prediction

---

## 🔍 Key Insights & Findings

1. **Baseline 2028 Prediction: ~3 medals**
   - Under current structural trends and policy environment
   
2. **Economic Impact: Limited to ~12%**
   - GDP explains only 12% of medal variance
   - Sporting ecosystem maturity > economic wealth
   
3. **India's Structural Challenge**
   - Underperforms relative to GDP rank globally
   - Policy gaps and infrastructure deficits identified
   
4. **Post-2016 Momentum** ✅
   - Medal average significantly higher post-2016 (Welch t-test confirmed)
   - Uptrend in recent Olympics
   
5. **Growth Ceiling: 10–15 medals**
   - Achievable if: career avg reaches 3.5+, momentum sustains
   - Requires sustained policy support
   
6. **Breakout Scenario: 15–20 medals**
   - Requires: Major policy reform + funding surge + infrastructure investment
   - Structural transformation needed
   
7. **Top Opportunity Sports** 🎯
   - Shooting, Badminton, Wrestling, Boxing, Athletics
   - High ROI, competitive advantage possible

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Kashyap-Ladva/OlympINDIA28.git
cd OlympINDIA28

# Install dependencies
pip install -r requirements.txt
```

### Running the Pipeline

**Option 1: Run complete pipeline**
```bash
python run_pipeline.py
```
Executes all 10 notebooks in sequence, regenerating all datasets and models.

**Option 2: Run individual notebooks**
```bash
jupyter notebook notebooks/India_Olympic_Deep_Analysis.ipynb
```

**Option 3: Launch web application**
```bash
streamlit run app.py
```
Opens interactive dashboard at http://localhost:8501

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `pandas` | Data manipulation & analysis |
| `numpy` | Numerical computing |
| `scikit-learn` | Machine learning utilities |
| `xgboost` | Gradient boosting models |
| `matplotlib` | Static visualizations |
| `seaborn` | Statistical graphics |
| `statsmodels` | Statistical modeling & tests |
| `scipy` | Scientific computing |
| `streamlit` | Web app framework |
| `plotly` | Interactive visualizations |
| `jupyter` | Notebook environment |

---

## 📊 Data Sources

- **Olympic History:** Kaggle's Olympic Games dataset (1896–2024)
- **Economic Data:** World Bank (GDP per capita, socioeconomic indicators)
- **Population Data:** UN World Population Prospects
- **Recent Games:** Official IOC records (2020, 2024)

---

## 🎓 Project Insights

This project demonstrates:

✅ **End-to-end ML pipeline**  
✅ **Multi-model ensemble approach**  
✅ **Scenario analysis & sensitivity testing**  
✅ **Sports analytics & domain-specific insights**  
✅ **Business intelligence visualization**  
✅ **Time-series forecasting**  
✅ **Statistical hypothesis testing**  

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional feature engineering (athlete demographics, coaching quality, etc.)
- Deep learning models (LSTM for time-series, neural networks)
- Real-time model updates as 2028 approaches
- API endpoint for predictions
- Mobile application
- Enhanced visualizations

To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📧 Contact & Questions

For questions, suggestions, or collaboration:
- **GitHub Issues:** [Open an issue](https://github.com/Kashyap-Ladva/OlympINDIA28/issues)
- **Email:** Your contact information

---

## 🙏 Acknowledgments

- Thanks to the Olympic data community & Kaggle
- World Bank for socioeconomic data
- The data science community for ML best practices

---

**Last Updated:** April 2026  
**Status:** Active Development  
**Next Update:** Quarterly, following major Olympic events
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
