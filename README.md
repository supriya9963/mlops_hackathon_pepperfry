# 🚗 🛋️ MLOps Project: SUV & Furniture Price Prediction

## 📌 Project Overview
This repository contains an end-to-end MLOps pipeline designed to solve pricing estimation problems using Machine Learning. It features two main projects:
1. **SUV Price Prediction:** Estimating resale values for used vehicles.
2. **Pepperfry Sofa Analysis:** Scraping and analyzing furniture market data to predict 2-seater sofa prices.

## 📁 Repository Artifacts
| Category | Files |
| :--- | :--- |
| **📈 Visualizations** | `plot_01_price_distribution.png` through `plot_11_feature_importance.png` |
| **🤖 ML Models** | `model.pkl`, `scaler.pkl`, `le_brand.pkl`, `le_fuel.pkl`, `feature_names.pkl` |
| **📊 Datasets** | `X_train.csv`, `y_train.csv`, `prepared_dataset.csv`, `pepperfry_sofas_enhanced.csv` |
| **📓 Notebooks** | `stage3_eda.ipynb`, `stage4_training.ipynb`, `stage5_deployment.ipynb` |
| **🐍 Scripts** | `app.py`, `pepperfry_scraper.py`, `stage6_streamlit_app.py` |

## 🎯 Problem Statement
A college transport department needs a data-driven system to estimate fair market prices for selling old SUV vehicles. Additionally, we expanded the scope to include the furniture market, scraping real-time data from **Pepperfry** to understand how brand popularity and material impact pricing.

## 🧠 MLOps Pipeline
1. **Data Acquisition:** Web scraping using **Selenium and XPath** for real-time furniture data.
2. **EDA:** Statistical analysis and visualization of price trends and feature correlations.
3. **Model Development:** Training regression models (Gradient Boosting, Random Forest) using Scikit-learn.
4. **Serialization:** Saving artifacts (`.pkl`) for reproducible deployment.
5. **Deployment:** - **API:** Flask backend for real-time inference.
   - **Frontend:** Streamlit UI for user interaction.
   - **Networking:** Public exposure via `ngrok`.

## ⚙️ Tech Stack
- **Language:** Python 🐍
- **Libraries:** Pandas, Scikit-learn, Matplotlib, Seaborn
- **Web Tools:** Selenium, Flask, Streamlit, Pyngrok
- **Version Control:** Git & GitHub

## 🚀 Quick Start
1. **Clone the repo:** `git clone https://github.com/supriya9963/mlops_hackathon_pepperfry.git`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Run API:** `python app.py`
4. **Run UI:** `streamlit run stage6_streamlit_app.py`

## 👨‍💻 Authors
- **R.Sanjana** — B.Tech CSE
- **K.Supriya** — B.Tech CSE
- **B.Laxmi Prasanna** — B.Tech CSE
- **G.Satwika** — B.Tech CSE

---
⭐ *If you find this project useful, please star the repository!*