# 🛍️ Online Retail Customer Segmentation

This project applies unsupervised machine learning techniques to segment customers based on transactional behavior in an online retail dataset. It demonstrates a full pipeline from data cleaning to clustering and visualization, offering actionable insights for marketing and business strategy.

## 📦 Dataset Overview

- **Source**: UCI Online Retail Dataset
- **Period**: December 2010 – December 2011
- **Scope**: Transactions from a UK-based gift retailer
- **Features**: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

## 🧹 Data Preprocessing

- Removed nulls and duplicates
- Filtered out canceled transactions (`InvoiceNo` starting with 'C')
- Engineered features:
  - `TotalAmount` = Quantity × UnitPrice
  - Temporal features: Year, Month, Day, Hour, TimeType (Morning/Afternoon/Evening)

## 📊 Exploratory Data Analysis

- Identified top-selling products and peak purchasing times
- Analyzed geographic distribution of customers
- Visualized distributions of key metrics (Quantity, UnitPrice, TotalAmount)

## 📈 Feature Engineering

- Created RFM (Recency, Frequency, Monetary) metrics
- Applied log transformation to reduce skewness
- Scaled features for clustering

## 🔍 Clustering Approach

- Used **KMeans** algorithm
- Determined optimal number of clusters using **Elbow Method** and **Silhouette Score**
- Labeled segments based on behavioral traits:
  - **Champions**
  - **Loyal Customers**
  - **At-Risk Customers**
  - **Lost Customers**

## 📌 Key Insights

- Majority of purchases originate from the UK
- Afternoon is the most active shopping period
- Seasonal spikes observed in Q4 (Oct–Dec)
- Cluster-specific strategies proposed for retention and targeting

## 🛠️ Tools & Libraries

- Python: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- Jupyter Notebook for analysis
- Tableau (optional) for interactive visualization
## 🚀 Author

**Walid Elsayed**  
Senior Data Scientist / ML Engineer  

---

Feel free to fork, star, or contribute!
