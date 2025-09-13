# 📊 Financial Ratio Analysis Tool

This project automates the **extraction, storage, and analysis of financial ratios** for insurance and financial companies.
It integrates **Kaggle datasets, SQLite, and Python visualizations** to provide insights into solvency, profitability, and risk.

---

## 🚀 Project Workflow

1. **Dataset**

   * Kaggle dataset: [Unsupervised Labeled Financial Ratios from 503 Trial Balances](https://www.kaggle.com/datasets/agrafintech/unsupervised-labeled-financial-ratios)
   * Stored in: `data/unsupervised_labeled_financial_ratios_from_503_trial_balances.csv`

2. **Data Pipeline**

   * Load CSV → Pandas
   * Store in SQLite (`insurance_ratios.db`)
   * Query ratios with SQLAlchemy

3. **Exploratory Data Analysis (EDA)**

   * Summary statistics of ratios
   * Distribution plots (Debt-to-Equity, Net Profit Margin)
   * Correlation heatmap

4. **Clustering (Optional Extension)**

   * Applied **KMeans** to group companies by solvency & profitability
   * Visualized clusters to identify high-risk vs. stable companies

---

## 📂 Project Structure

```
financial_ratio_analysis_tool/
│── data/                           # Raw Kaggle dataset
│── sql/                            # SQLite database
│── notebooks/                      # Jupyter Notebook with analysis
│── requirements.txt                 # Dependencies
│── README.md                        # Project overview
```


## 💡 Key Insights

* Ratios vary significantly across companies and sectors.
* Correlation heatmap reveals strong links between solvency and profitability.
* Clustering highlights groups of companies that are **high-risk vs. low-risk**.
* Automating this pipeline saves time for actuaries and analysts.

---

## 🛠️ Tech Stack

* **Python**: Pandas, Matplotlib, Seaborn, Scikit-learn
* **SQLAlchemy + SQLite**
* **Jupyter Notebook**

