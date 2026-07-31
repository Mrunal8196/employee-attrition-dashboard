# Employee Attrition Dashboard (Power BI)

I built this project while teaching myself Power BI, as I move from data analysis toward a
People Analytics / HR Data Analyst role. I wanted to practise the whole workflow end to end —
preparing the data, writing my own DAX, and turning it into something an HR team could
actually use to make decisions, not just a set of charts.

The question I set out to answer: **where are we losing people, who is most at risk, and
what's driving it?**

*(The dataset is synthetic — I generated ~1,500 employee records with realistic patterns so
there's no real personal data involved.)*

## Screenshots

![Overview page](screenshots/page1.png)
![Drivers and risk page](screenshots/page2.png)

You can also open `attrition_dashboard.pdf` to see both pages, or `attrition_dashboard.pbix`
in Power BI Desktop to explore it interactively.

## What I found

- Attrition sits at about **32%** overall across the 1,500 employees.
- The strongest driver by far is **overtime** — people working overtime leave at roughly
  **2× the rate** of those who don't. That surprised me; it beat income as a predictor.
- Exits are concentrated in the **first 0–2 years** of tenure and in the **lowest income band**.
- When I combined the risk factors (overtime + low job satisfaction + short tenure), that
  small segment showed a **72% attrition rate** vs about 31% for everyone else.

## What I'd tell an HR team to do about it

- Look hard at overtime for early-tenure employees — that's where most exits come from.
- Put retention and onboarding effort into the first two years.
- Track the high-risk segment as a standing metric rather than reacting after people leave.

## How I built it

- **Data:** a Python script (`data/generate_hr_data.py`) that generates the employee dataset
  with attrition weighted by overtime, tenure, satisfaction, income and commute distance.
- **Modelling:** DAX measures and calculated columns in Power BI — attrition rate, the
  overtime comparison, and banding columns for age, tenure, income and distance
  (see `dax/measures.dax`).
- **Report:** two pages in Power BI Desktop — an overview and a drivers/risk view, with
  slicers so you can filter by department, gender, role and overtime.

If you want to rebuild it, run `python data/generate_hr_data.py` to create the CSV, then open
the `.pbix` (my build notes are in `docs/BUILD_GUIDE.md`).

## What I'd do next

- Rebuild it on a real HR dataset instead of synthetic data.
- Add a simple predictive risk score per employee rather than a rules-based flag.
- Add trend-over-time once there's historical data to work with.

---

Built by Mrunali Patil while transitioning into People Analytics. Feedback is welcome —
I'm still learning and happy to hear how to make it better.
