# E-Governance Data Ingestion, Hygiene & Exploratory Analytics Pipeline

**Internship:** Yuva Intern / NSDC Data Analytics Track  
**Domain:** Digital Public Services & E-Governance Analytics  
**Repository:** End-to-End Data Ingestion, Automated Quality Hygiene & Exploratory Analysis Engine  

---

## Repository Structure

```text
├── scripts/
│   ├── clean_data.py          # Week 2: Automated data ingestion & hygiene engine
│   └── eda_analysis.py        # Week 3: Visual EDA & inferential hypothesis engine
├── data/
│   ├── raw/                   # Raw transactional logs (raw_egov_transactions.csv)
│   └── processed/             # Audited output data, quality summaries & plots
│       ├── cleaned_egov_services.csv
│       ├── cleaning_audit_summary.txt
│       ├── eda_summary_statistics.csv
│       └── visualizations/    # Generated high-resolution PNG charts
│           ├── viz1_state_volume.png
│           ├── viz2_department_latency_boxplot.png
│           ├── viz3_timeseries_surge.png
│           └── viz4_correlation_heatmap.png
├── requirements.txt           # Environment dependencies
└── README.md                  # Unified technical documentation