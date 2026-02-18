# ☕ Pricing of chocolate and coffee 🍫

> Using share prices and statistics from the German goverment we predict the prices of chocolate and coffee. 

## 📊 Project overview

**Problem:** 
Prices of chocolate products increased in the last years. We use data such as global chocolate and coffee future prices, and share prices from companies producing chocolate products, e.g. Lindt and Mondelez, to model the price elasticity of chocolate products. 

**Objective:** 
Our target is the price elasticity, which we calculate using data from the German goverment according to the following formula: price elasticity = change of demand / change of price.

**Methods:** 
- Time Series Analysis
- Support Vector Regressor
- Artificial Neuronal Networks
- Random Forests
- ARIMAX
- XGBoost



## Setup

Clone the repository
```bash
# Clone repository
git clone https://github.com/salimaabdalla/dpp_projekt_2026
cd dpp_projekt_2026
```

Install [uv](https://uv.dev) (if not installed already) and synchronise dependencies
```bash
# Install dependencies
uv sync
```

### Execution

Run notebooks in the following order:
1. notebooks/01_preprocessing_monthly_data.ipynb
2. notebooks/02_shareprice_daily_to_monthly.ipynb
3. notebooks/03_combining_all_data.ipynb
4. notebooks/04_exploration.ipynb
5. notebooks/05_preprocessing.ipynb
6. notebooks/06_first_prediction.ipynb
7. notebooks/07_prediction_with_monthly_new_data.ipynb
8. notebooks/08_estimation_price_elasticity.ipynb
9. notebooks/09_models_shareprices_stepwise.ipynb
10. notebooks/10_ARIMAX_parameter_selection.ipynb
11. notebooks/11_ARIMAX_monthly_updated_prediction.ipynb
12. notebooks/12_XGBoost.ipynb
13. notebooks/13_XGBoost_for_Presentation.ipynb



