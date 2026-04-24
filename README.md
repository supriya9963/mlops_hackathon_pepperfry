# 🚗 🛋️ MLOps Project: SUV & Furniture Price Prediction

## 📌 Project Overview
This repository contains an end-to-end MLOps pipeline designed to solve pricing estimation problems using Machine Learning and Prompt Engineering. It features two core solutions:
1. **SUV Price Prediction:** Resale value estimation for college transport departments.
2. **Pepperfry Price Optimizer:** Market-driven pricing for new furniture businesses.

## 🌟 Business Case: The Furniture Challenge
**The Scenario:** A friend has designed a new **contemporary 2-seater sofa set** and needs to determine the optimal online selling price. 
**Our Solution:** - **Inventory Benchmarking:** As suggested by the business owner, we targeted sites with the **maximum online inventory** (Pepperfry) to scrape real-world competitor data.
- **Prompt Engineering:** Utilized advanced prompts to build robust **Selenium + XPath** scrapers and to engineer features like "Brand Popularity Scores."
- **Decision Support:** Using ML, we provide a data-backed price that ensures the new contemporary design is competitive yet profitable against established brands.

## 📁 Repository Artifacts
| Category | Files |
| :--- | :--- |
| **📈 Visualizations** | `plot_01_price_distribution.png` through `plot_11_feature_importance.png` |
| **🤖 ML Models** | `model.pkl`, `scaler.pkl`, `le_brand.pkl`, `le_fuel.pkl`, `feature_names.pkl` |
| **📊 Datasets** | `X_train.csv`, `y_train.csv`, `prepared_dataset.csv`, `pepperfry_sofas_enhanced.csv` |
| **📓 Notebooks** | `stage3_eda.ipynb`, `stage4_training.ipynb`, `stage5_deployment.ipynb` |
| **🐍 Scripts** | `app.py`, `pepperfry_scraper.py`, `stage6_streamlit_app.py` |

## 🧠 MLOps Pipeline
1. **Data Acquisition:** Selenium-based scraping of high-inventory furniture platforms.
2. **Feature Engineering:** Calculation of brand popularity ranges (1-10) and material-based price weighting.
3. **Model Development:** Trained Gradient Boosting and Random Forest Regressors for precise estimation.
4. **Serialization:** Artifacts saved as `.pkl` for seamless deployment.
5. **Deployment:** Flask API for backend logic and Streamlit for the friend's business dashboard.

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
- **R. Sanjana** — B.Tech CSE
- **K. Supriya** — B.Tech CSE
- **B. Laxmi Prasanna** — B.Tech CSE
- **G. Satwika** — B.Tech CSE

---
⭐ *If you find this project useful, please star the repository!*