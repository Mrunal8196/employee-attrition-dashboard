# 🚀 Push to GitHub

## 1. Arrange the files (one-time)
Create this structure on your computer and move the delivered files in:

```
attrition-people-analytics/
├── README.md
├── data/
│   └── generate_hr_data.py        (hr_employees.csv appears after you run it)
├── dax/
│   └── measures.dax
├── docs/
│   └── BUILD_GUIDE.md
├── screenshots/
│   ├── page1.png
│   └── page2.png
├── attrition_dashboard.pbix
├── PUSH_TO_GITHUB.md
└── .gitignore
```

## 2. Create the repo on GitHub
- github.com → **New repository** → name `attrition-people-analytics` → **Public** → Create.
- (Don't add a README there — you already have one.)

## 3. Push from your computer
```bash
cd path/to/attrition-people-analytics

git init
git add .
git commit -m "People Analytics: employee attrition dashboard (Power BI)"
git branch -M main
git remote add origin https://github.com/<your-username>/attrition-people-analytics.git
git push -u origin main
```

## 4. After pushing
- Confirm the screenshots render in the README on GitHub.
- Copy the repo URL into your CV (Portfolio: …) and post it on LinkedIn.

**Tip:** the `.pbix` can be large — that's fine for a public portfolio repo. If GitHub
warns about size, you can instead link the published-to-web dashboard and skip committing
the `.pbix`.
