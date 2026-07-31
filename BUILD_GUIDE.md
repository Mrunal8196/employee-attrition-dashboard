# 🧭 Build Guide — Attrition Dashboard in Power BI Desktop

Follow top to bottom. First full build ≈ 4–5 hours.
You need **Power BI Desktop** (free, Windows) — download from Microsoft.

---

## Step 0 — Get the data
- Run `python generate_hr_data.py` → produces `hr_employees.csv` (~1,500 rows), **or**
- Download the IBM HR Attrition dataset from Kaggle and use that CSV instead.

---

## Step 1 — Load & check (20 min)
1. Power BI Desktop → **Home > Get data > Text/CSV** → select `hr_employees.csv` → **Load**.
2. **Transform data** (Power Query): confirm data types — `Attrition`, `OverTime`, `Department`, `JobRole`, `Gender` = Text; `Age`, `MonthlyIncome`, `YearsAtCompany`, ratings = Whole number.
3. Check no nulls (Column quality). **Close & Apply**.
4. Rename the table to **Employees** if needed (matches the DAX file).

## Step 2 — Add measures & columns (45 min)
- Open `measures.dax`. For each **measure**: *Modeling > New measure*, paste, Enter.
- For each **calculated column** (Age Band, Tenure Band, Income Band, Distance Band, High Risk Flag): *Modeling > New column*, paste.
- Select `Attrition Rate`, `Attrition Rate (Overtime/No Overtime)` → **Format as Percentage** (Measure tools > %).

## Step 3 — Page 1: Overview "Where" (75 min)
Layout top-to-bottom:
1. **Title bar** (text box): "Employee Attrition — Overview" + your name.
2. **KPI cards** (Card visual, one each): `Attrition Rate`, `Total Employees`, `Attrition Count`, `Avg Tenure`, `Avg Monthly Income`.
3. **Clustered bar chart** — Attrition Rate by `Department`.
4. **Clustered bar chart** — Attrition Rate by `JobRole`.
5. **Clustered column chart** — Attrition Rate by `Age Band`.
6. **Clustered column chart** — Attrition Rate by `Tenure Band`.
7. **Slicers** (top or side): `Department`, `Gender`, `JobRole`, `OverTime`.
- Sort bar charts descending by Attrition Rate. Use one accent colour for "high" bars.

## Step 4 — Page 2: Drivers & Risk "Why / Who" (75 min)
1. **Title bar**: "Attrition Drivers & Risk".
2. **Column chart** — Attrition Rate by `OverTime` (the headline driver).
3. **Column chart** — Attrition Rate by `JobSatisfaction` and by `WorkLifeBalance`.
4. **Column chart** — Attrition Rate by `Income Band` and by `Distance Band`.
5. **Table/Matrix** — rows = `High Risk Flag`, values = `Total Employees`, `Attrition Rate`.
6. **Insight callouts** (text boxes): e.g.
   - "Employees on overtime leave at **[Overtime Risk Multiple]×** the rate of others."
   - "**0–2 yr** tenure is the highest-risk group."
   - Use the actual numbers from your visuals.

## Step 5 — Polish (30 min)
- One consistent accent colour; align visuals to a grid; clear titles on every visual.
- Turn off unnecessary gridlines; format % and € consistently.
- Add a subtle footer: "Data: synthetic / IBM sample · Built by Mrunali Patil".

## Step 6 — Capture & publish (30 min)
1. **Screenshots:** export/screenshot each page → save as `screenshots/page1.png`, `page2.png`.
2. **Save** the file as `attrition_dashboard.pbix`.
3. **Publish to web** (needs free Power BI account): *File > Publish > Power BI service*, then in the service *File > Embed report > Publish to web (public)* → copy the link.
4. Paste that link into `README.md` (Live dashboard) and your CV header.

## Step 7 — Fill in real numbers
Open `README.md` and replace the placeholder insight numbers with your actual results.

---

## ✅ Done checklist
- [ ] Two clean pages, consistent styling
- [ ] All KPI cards + DAX measures working
- [ ] 3+ insight callouts with real numbers
- [ ] Screenshots saved
- [ ] Published-to-web link live
- [ ] README updated with link + real figures
- [ ] Repo pushed to GitHub (see PUSH_TO_GITHUB.md)
