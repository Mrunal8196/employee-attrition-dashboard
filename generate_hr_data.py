"""
generate_hr_data.py
Creates a realistic synthetic HR dataset (~1,500 employees) for the
Employee Attrition People Analytics dashboard.

Attrition is generated with realistic drivers so the dashboard tells a story:
overtime, low satisfaction, short tenure, low income and long commute all
increase the chance an employee has left.

Usage:
    python generate_hr_data.py
Output:
    hr_employees.csv
"""

import csv
import random

random.seed(42)                      # reproducible output
N = 1500

departments = {
    "Sales":        ["Sales Executive", "Sales Representative", "Manager"],
    "R&D":          ["Research Scientist", "Laboratory Technician", "Manager"],
    "HR":           ["HR Specialist", "Recruiter", "Manager"],
    "IT":           ["Data Analyst", "Software Engineer", "IT Manager"],
    "Finance":      ["Accountant", "Financial Analyst", "Manager"],
}
dept_weights = [0.30, 0.30, 0.10, 0.18, 0.12]
genders = ["Male", "Female"]
education = ["Below College", "College", "Bachelor", "Master", "Doctorate"]
marital = ["Single", "Married", "Divorced"]
travel = ["Non-Travel", "Travel_Rarely", "Travel_Frequently"]

def rating():                        # 1 (low) .. 4 (high)
    return random.randint(1, 4)

def attrition_probability(overtime, satisfaction, wlb, years, income, distance, age):
    """Higher score => more likely to have left. Returns 0/1."""
    p = 0.06                                    # base rate
    if overtime == "Yes":            p += 0.22
    if satisfaction <= 2:            p += 0.12
    if wlb <= 2:                     p += 0.08
    if years <= 2:                   p += 0.15
    if income < 3000:                p += 0.10
    if distance > 15:                p += 0.05
    if age < 30:                     p += 0.05
    p = min(p, 0.9)
    return 1 if random.random() < p else 0

rows = []
for emp_id in range(1001, 1001 + N):
    dept = random.choices(list(departments), weights=dept_weights)[0]
    role = random.choice(departments[dept])
    age = random.randint(20, 60)
    gender = random.choice(genders)
    total_working_years = max(0, age - random.randint(20, 24))
    years_at_company = min(total_working_years, random.randint(0, 20))
    overtime = random.choices(["Yes", "No"], weights=[0.28, 0.72])[0]
    job_sat = rating()
    wlb = rating()
    env_sat = rating()
    # income scales with role seniority + tenure
    base = 2500 if "Manager" not in role else 6000
    monthly_income = int(base + years_at_company * 250 + random.randint(-500, 1500))
    distance = random.randint(1, 29)
    edu = random.choices(education, weights=[0.05, 0.20, 0.40, 0.28, 0.07])[0]
    ms = random.choice(marital)
    bt = random.choices(travel, weights=[0.10, 0.70, 0.20])[0]
    promo = random.randint(0, min(years_at_company, 10))

    attr = attrition_probability(overtime, job_sat, wlb,
                                 years_at_company, monthly_income, distance, age)

    rows.append({
        "EmployeeID": emp_id,
        "Age": age,
        "Gender": gender,
        "Department": dept,
        "JobRole": role,
        "Education": edu,
        "MaritalStatus": ms,
        "BusinessTravel": bt,
        "OverTime": overtime,
        "MonthlyIncome": monthly_income,
        "YearsAtCompany": years_at_company,
        "TotalWorkingYears": total_working_years,
        "YearsSinceLastPromotion": promo,
        "DistanceFromHome": distance,
        "JobSatisfaction": job_sat,
        "WorkLifeBalance": wlb,
        "EnvironmentSatisfaction": env_sat,
        "Attrition": "Yes" if attr == 1 else "No",
    })

fieldnames = list(rows[0].keys())
with open("hr_employees.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

left = sum(1 for r in rows if r["Attrition"] == "Yes")
print(f"Wrote hr_employees.csv  |  {len(rows)} employees  |  "
      f"attrition rate {left/len(rows):.1%}")
