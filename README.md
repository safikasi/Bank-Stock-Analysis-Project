# 📊 Bank Stock Analysis (2006-2016): Crisis to Recovery

![Project Banner](https://img.freepik.com/free-vector/gradient-stock-market-concept_23-2149166910.jpg)

*A comprehensive analysis of major US banks through the 2008 financial crisis using Python's data science stack.*

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.0%2B-orange?logo=pandas)](https://pandas.pydata.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 🌟 Highlights
- **10-year analysis** of 6 major US banks
- **Interactive visualizations** with Plotly
- **Crisis impact comparison** (2008 vs 2015)
- **Technical indicators**: SMA, Bollinger Bands
- **Correlation heatmaps** for portfolio insights

## 📌 Table of Contents
1. [Visual Dashboard](#-visual-dashboard)
2. [Key Findings](#-key-findings)
3. [Technologies Used](#-technologies-used)
4. [Installation](#-installation)
5. [Usage](#-usage)
6. [Code Walkthrough](#-code-walkthrough)
7. [Contributing](#-contributing)
8. [License](#-license)

## 📊 Visual Dashboard

### Comparative Stock Performance (2006-2016)
![Bank Stock Trends](Screenshot%202025-07-10%20015430.png)
*All banks show dramatic drops during 2008, with varying recovery patterns*

---

### Citigroup 2008 Returns (Crisis Period)
![C 2008 Returns](Screenshot%202025-07-10%20015408.png)
*Extreme volatility with frequent >5% daily moves*

---

### Morgan Stanley 2015 Returns (Stable Period)
![MS 2015 Returns](Screenshot%202025-07-10%20015343.png)
*Normal distribution showing market stabilization*

---

### BAC Technical Analysis (2008)
![BAC 30-day MA](Screenshot%202025-07-10%20015816.png)
*30-day moving average vs price during crisis*

---

### Bank Correlation Matrix
![Correlation Heatmap](Screenshot%202025-07-10%20015835.png)
*Goldman Sachs (GS) and Morgan Stanley (MS) show 0.97 correlation*

## 🔍 Key Findings

| Metric | Insight |
|--------|---------|
| **Worst Performer** | Citigroup (-98% from peak) |
| **Best Survivor** | Wells Fargo (50% less drop than peers) |
| **Highest Volatility** | BAC (σ=0.038 daily returns in 2008) |
| **Fastest Recovery** | Goldman Sachs (3 years to new highs) |
| **Most Correlated Pair** | GS-MS (0.97 correlation) |

**Notable Events:**
- Lehman collapse (Sep 2008) caused synchronized drops
- Bank bailouts (Oct 2008) marked inflection points
- Volcker Rule implementation (2014) reduced correlations

## 🛠 Technologies Used

| Technology | Purpose | 
|------------|---------|
| ![Python](https://img.icons8.com/color/48/000000/python.png) Python 3.7+ | Core analysis |
| ![Pandas](https://img.icons8.com/color/48/000000/pandas.png) Pandas | Data manipulation |
| ![Plotly](https://img.icons8.com/color/48/000000/chart.png) Plotly | Interactive viz |
| Seaborn | Statistical graphics |
| pandas-datareader | Market data fetching |

## 👨‍💻 About Me
**Safwan Khan Kasi**  
DS & ML Enthusiast   

[![GitHub](https://img.shields.io/badge/GitHub-safikasi-blue?logo=github)](https://github.com/safikasi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Safwan_Kasi-blue?logo=linkedin)](https://www.linkedin.com/in/safwan-kasi-2b5358292/)

## ⚙️ Installation

1. Clone the repo:
```bash
git clone https://github.com/safikasi/Bank-Stock-Analysis-Project.git
cd Bank-Stock-Analysis