# 📊 Employee Attrition — People Analytics Dashboard

An interactive Power BI dashboard that answers a real HR business question:
**"Where are we losing people, who is most at risk, and what's driving it?"**

Built to demonstrate end-to-end People Analytics: data preparation, DAX modelling,
and turning workforce data into decisions for HR and leadership.

> **Live dashboard:** _add your Power BI "Publish to web" link here_
> **Author:** Mrunali Patil · People Analytics / HR Data Analyst · Berlin

---

## 🔎 Business question

HR leadership needs to know **where attrition is concentrated, which employees are most
at risk, and what factors drive it** — so retention effort and budget go to the right places.

## 💡 Key insights (fill in with your own numbers after building)

- Overall attrition rate: **~16%** (1,470 employees).
- Employees working **overtime leave at roughly 3× the rate** of those who don't.
- Attrition is highest in the **first 1–2 years of tenure** and among **lower-income bands**.
- **Low job satisfaction + overtime + short tenure** = the highest-risk segment.

*(Replace the above with the exact figures from your build — recruiters love specifics.)*

---

## 🗂️ Dashboard pages

**Page 1 — Overview ("Where")**
KPI cards (attrition rate, headcount, attrition count, avg tenure, avg income) +
attrition by department, job role, age band and tenure band. Slicers for department,
gender, job role, overtime.

**Page 2 — Drivers & Risk ("Why / Who")**
Attrition by overtime, job satisfaction, work-life balance, income band and distance
from home, plus a high-risk-segment table and written insight callouts.

---

## 🧱 How it's built

| Layer | Tool |
|---|---|
| Data | `generate_hr_data.py` (synthetic, ~1,500 rows) *or* IBM HR Attrition dataset |
| Modelling & measures | Power BI + DAX (see `measures.dax`) |
| Visualisation | Power BI Desktop → Power BI Service |

Full step-by-step in **BUILD_GUIDE.md**.

---

## ▶️ Reproduce it

```bash
# Option A: generate synthetic data
python generate_hr_data.py        # creates hr_employees.csv

# Option B: download the IBM HR Attrition dataset from Kaggle and use that CSV
```
Then open Power BI Desktop, load `hr_employees.csv`, and follow `BUILD_GUIDE.md`.

---

## 📁 Recommended repo structure

```
attrition-people-analytics/
├── README.md
├── data/
│   ├── generate_hr_data.py
│   └── hr_employees.csv        # produced by the script
├── dax/
│   └── measures.dax
├── docs/
│   └── BUILD_GUIDE.md
├── screenshots/                # add page1.png, page2.png after building
└── attrition_dashboard.pbix    # add after you build it in Power BI Desktop
```
*(The files in this folder are flat — move them into the structure above when you set up the repo.)*

## 🛠️ Skills demonstrated

Data modelling · DAX measures · data cleansing & banding · KPI design ·
People Analytics (attrition, retention, headcount, DEI) · dashboard storytelling.
