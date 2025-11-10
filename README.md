# Cement Sales Analysis & ETL Pipeline

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English Version Below](#english-version)

---

<a name="thai-version"></a>
## 🇹🇭 เวอร์ชั่นภาษาไทย

### ภาพรวมโปรเจกต์
โปรเจกต์นี้เป็นการวิเคราะห์ข้อมูลยอดขายปูนซีเมนต์รายเดือนตั้งแต่ปี 2010 ถึง 2022 โดยมีวัตถุประสงค์เพื่อทำความเข้าใจแนวโน้มการเติบโตและรูปแบบตามฤดูกาล คำนวณและประเมิน Key Performance Indicators (KPIs) ที่สำคัญ เช่น ประสิทธิภาพการผลิตและการตอบสนองต่อความต้องการของตลาด รวมถึงการพยากรณ์ยอดขายในอนาคต 12 เดือนข้างหน้าโดยใช้โมเดล Time Series (Prophet) โปรเจกต์นี้จัดทำขึ้นเพื่อแสดงทักษะด้านการวิเคราะห์ข้อมูลและการสร้างแบบจำลอง ซึ่งเป็นส่วนหนึ่งของการเตรียมตัวสมัครฝึกงานในตำแหน่ง Data Analyst/Data Scientist

### โครงสร้างไฟล์
```text
.
├── 📊 dashboard/
│   └── dashboard.pbix
├── 💾 data/
│   ├── processed/
│   │   ├── cement_factory.db
│   │   └── cleaned_cement_data.csv
│   ├── query_results/
│   │   ├── gdp_correlation.csv
│   │   ├── kpi_efficiency.csv
│   │   ├── low_efficiency.csv
│   │   ├── production_gap.csv
│   │   └── yearly_summary.csv
│   └── raw/
│       └── raw_cement_data.csv
├── 📓 notebooks/
│   ├── 01_analysis_and_forecasting.ipynb
│   └── 02_sql_query_examples.ipynb
├── 🔍 sql_queries/
│   ├── gdp_correlation.sql
│   ├── kpi_efficiency.sql
│   ├── low_efficiency.sql
│   ├── production_gap.sql
│   └── yearly_summary.sql
├── 🛠️ src/
│   ├── __init__.py
│   ├── data_cleaner.py
│   └── pipeline.py
├── .gitignore
├── 📝 README.md
└── 📦 requirements.txt
```

**คำอธิบายเพิ่มเติม**

* **📊 dashboard/**: ไฟล์ Power BI สำหรับแสดงผลข้อมูล
* **💾 data/**: เก็บข้อมูลทุกขั้นตอน
    * `raw/`: ข้อมูลดิบเริ่มต้น
    * `processed/`: ข้อมูลที่ผ่านการทำความสะอาดแล้ว (CSV และ SQLite DB)
    * `query_results/`: ผลลัพธ์ที่ได้จากการรัน SQL query
* **📓 notebooks/**: Jupyter Notebook สำหรับการวิเคราะห์ พยากรณ์ และตัวอย่างการใช้ SQL
* **🔍 sql_queries/**: ไฟล์ SQL แยกตามจุดประสงค์การวิเคราะห์
* **🛠️ src/**: ซอร์สโค้ด Python สำหรับการทำ Data Cleaning และ Pipeline หลัก
* **📦 requirements.txt**: รายชื่อ Library ที่จำเป็นสำหรับโปรเจกต์นี้


### ชุดข้อมูล
* **แหล่งที่มา:** [Kaggle: Cement Sales Demand](https://www.kaggle.com/datasets/kishorkhengare/cement-sales-demand)
* **ช่วงเวลา:** 2010-2022 (รายเดือน)
* **ตัวแปรสำคัญ:** Production, Sales, Demand, GDP, Population, Interest Rate, etc.
* **ที่เก็บข้อมูล:** `data/raw/raw_cement_data.csv`

### ขั้นตอนการทำงาน
1.  **Data Ingestion & Pipeline:** สร้าง ETL pipeline (`src/pipeline.py`) เพื่ออ่านข้อมูลดิบ ทำความสะอาด (ใช้ `src/data_cleaner.py` - Pandas) และโหลดเข้าฐานข้อมูล SQLite (`data/processed/cement_factory.db`)
2.  **Exploratory Data Analysis (EDA):** วิเคราะห์แนวโน้มเบื้องต้น รูปแบบตามฤดูกาล (Seasonal Patterns) โดยใช้ Matplotlib/Seaborn ใน Notebook (`notebooks/01_analysis_and_forecasting.ipynb`)
3.  **KPI Analysis:** คำนวณและวิเคราะห์ Key Performance Indicators (KPIs) เช่น Production Efficiency และ Demand Fulfillment โดยใช้ SQL Queries (`sql_queries/`) และ Pandas
4.  **Cost Driver Analysis:** ใช้ Ridge Regression (Scikit-learn) เพื่อหาความสัมพันธ์ระหว่างปัจจัยเศรษฐกิจ (GDP, Interest Rate, etc.) กับยอดขาย
5.  **Sales Forecasting:** ใช้ Prophet เพื่อพยากรณ์ยอดขาย 12 เดือนข้างหน้า
6.  **Visualization:** สร้าง Dashboard ด้วย Power BI (เชื่อมต่อกับ SQLite หรือไฟล์ CSV ผลลัพธ์จาก Query)

### ผลการวิเคราะห์หลัก
* ยอดขายมีการเติบโตอย่างต่อเนื่อง แต่มีรูปแบบตามฤดูกาลชัดเจน (พีคช่วงกลางปี)
* KPI ด้าน Efficiency และ Fulfillment อยู่ในระดับสูง (>95%) แสดงถึงประสิทธิภาพที่ดี
* GDP เป็นปัจจัยขับเคลื่อนยอดขายที่สำคัญที่สุด
* การพยากรณ์คาดว่ายอดขายจะเติบโต ~5-8% ในปีถัดไป

---

<a name="english-version"></a>
## 🇬🇧 English Version

### Project Overview
This project analyzes monthly cement sales data from 2010 to 2022. The objective is to understand growth trends and seasonal patterns, calculate and evaluate key performance indicators (KPIs) such as production efficiency and market demand fulfillment, and forecast future sales for the next 12 months using a Time Series model (Prophet). This project demonstrates data analysis and modeling skills as part of preparation for a Data Analyst/Data Scientist internship application.

### Dataset
* **Source:** [Kaggle: Cement Sales Demand](https://www.kaggle.com/datasets/kishorkhengare/cement-sales-demand)
* **Time Period:** 2010-2022 (Monthly)
* **Key Variables:** Production, Sales, Demand, GDP, Population, Interest Rate, etc.
* **Data Storage:** `data/raw/raw_cement_data.csv`

### Methodology / Workflow
1.  **Data Ingestion & Pipeline:** Built an ETL pipeline (`src/pipeline.py`) to read raw data, clean it (using `src/data_cleaner.py` - Pandas), and load it into an SQLite database (`data/processed/cement_factory.db`).
2.  **Exploratory Data Analysis (EDA):** Analyzed initial trends and seasonal patterns using Matplotlib/Seaborn in Notebook (`notebooks/01_analysis_and_forecasting.ipynb`).
3.  **KPI Analysis:** Calculated and analyzed Key Performance Indicators (KPIs) such as Production Efficiency and Demand Fulfillment using SQL Queries (`sql_queries/`) and Pandas.
4.  **Cost Driver Analysis:** Used Ridge Regression (Scikit-learn) to find correlations between economic factors (GDP, Interest Rate, etc.) and sales.
5.  **Sales Forecasting:** Used Prophet to forecast sales for the next 12 months.
6.  **Visualization:** Created a dashboard using Power BI (connected to SQLite or CSV query results).

### Key Findings / Insights
* Sales show continuous growth but with clear seasonal patterns (peaking mid-year).
* KPIs for Efficiency and Fulfillment are high (>95%), indicating good performance.
* GDP is the most significant driver of sales.
* Forecasts predict sales growth of ~5-8% in the coming year.

