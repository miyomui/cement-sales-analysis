# Cement Sales Analysis & ETL Pipeline

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## บทนำ (Introduction / Business Problem)

โปรเจกต์นี้เป็นการวิเคราะห์ข้อมูลยอดขายปูนซีเมนต์รายเดือนตั้งแต่ปี 2010 ถึง 2022 โดยมีวัตถุประสงค์เพื่อทำความเข้าใจแนวโน้มการเติบโตและรูปแบบตามฤดูกาล คำนวณและประเมิน Key Performance Indicators (KPIs) ที่สำคัญ เช่น ประสิทธิภาพการผลิตและการตอบสนองต่อความต้องการของตลาด รวมถึงการพยากรณ์ยอดขายในอนาคต 12 เดือนข้างหน้าโดยใช้โมเดล Time Series (Prophet) โปรเจกต์นี้จัดทำขึ้นเพื่อแสดงทักษะด้านการวิเคราะห์ข้อมูลและการสร้างแบบจำลอง ซึ่งเป็นส่วนหนึ่งของการเตรียมตัวสมัครฝึกงานในตำแหน่ง Data Analyst/Data Scientist ที่ SCG

## ชุดข้อมูล (Dataset)

อธิบายข้อมูลที่ใช้:
* **แหล่งที่มา:** [https://www.kaggle.com/datasets/kishorkhengare/cement-sales-demand](https://www.kaggle.com/datasets/kishorkhengare/cement-sales-demand)
* **ช่วงเวลา:** 2010-2022 (รายเดือน)
* **ตัวแปรสำคัญ:** Production, Sales, Demand, GDP, Population, Interest Rate, etc.
* **ที่เก็บข้อมูล:** `data/raw/raw_cement_data.csv`

## ขั้นตอนการทำงาน (Methodology / Workflow)

1.  **Data Ingestion & Pipeline:** สร้าง ETL pipeline (`src/pipeline.py`) เพื่ออ่านข้อมูลดิบ ทำความสะอาด (ใช้ `src/data_cleaner.py` - Pandas) และโหลดเข้าฐานข้อมูล SQLite (`data/processed/cement_factory.db`)
2.  **Exploratory Data Analysis (EDA):** วิเคราะห์แนวโน้มเบื้องต้น รูปแบบตามฤดูกาล (Seasonal Patterns) โดยใช้ Matplotlib/Seaborn ใน Notebook (`notebooks/01_analysis_and_forecasting.ipynb`)
3.  **KPI Analysis:** คำนวณและวิเคราะห์ Key Performance Indicators (KPIs) เช่น Production Efficiency และ Demand Fulfillment โดยใช้ SQL Queries (`sql_queries/`) และ Pandas
4.  **Cost Driver Analysis:** ใช้ Ridge Regression (Scikit-learn) เพื่อหาความสัมพันธ์ระหว่างปัจจัยเศรษฐกิจ (GDP, Interest Rate, etc.) กับยอดขาย
5.  **Sales Forecasting:** ใช้ Prophet เพื่อพยากรณ์ยอดขาย 12 เดือนข้างหน้า
6.  **Visualization:** สร้าง Dashboard ด้วย Power BI (เชื่อมต่อกับ SQLite หรือไฟล์ CSV ผลลัพธ์จาก Query)

## ผลการวิเคราะห์หลัก (Key Findings / Insights)


* ยอดขายมีการเติบโตอย่างต่อเนื่อง แต่มีรูปแบบตามฤดูกาลชัดเจน (พีคช่วงกลางปี)
* KPI ด้าน Efficiency และ Fulfillment อยู่ในระดับสูง (>95%) แสดงถึงประสิทธิภาพที่ดี
* GDP เป็นปัจจัยขับเคลื่อนยอดขายที่สำคัญที่สุด
* การพยากรณ์คาดว่ายอดขายจะเติบโต ~5-8% ในปีถัดไป
* 
   ```markdown
   ![Sales Trend](บลาบลารอใส่รูป.png)
