# E-Governance Data Collection and Cleaning Pipeline

**Internship:** Yuva Intern / NSDC Data Analytics  
**Task:** Week 2 — Data Collection and Cleaning for Digital Public Services  

## Overview
This repository implements an automated, reproducible data ingestion and hygiene pipeline for open-source e-governance transactional records. It processes a benchmark of 125,480 transactional entries across five major citizen services (Sarathi, Vahan, MeeSeva, DigiLocker, and PDS e-Challan) alongside infrastructure benchmarks from TRAI.

## Key Pipeline Features
- **Schema Normalization:** Converts non-standard, mixed-case headers to clean snake_case.
- **Entity Resolution:** Standardizes historical/archaic state names using official Local Government Directory (LGD) coding.
- **Deduplication:** Removes multi-source batch duplicates using composite primary keys.
- **Outlier Quarantine:** Isolates extreme clerical errors using IQR 3.0× boundary fencing.
- **Stratified Median Imputation:** Imputes missing turnaround latencies by department category.

## Cleaning Audit Summary
| Metric | Count / Percentage |
| :--- | :--- |
| **Raw Records Ingested** | 125,480 |
| **Duplicates Removed** | 4,112 (3.28%) |
| **Negative Sentinel Records Purged** | 418 |
| **Missing Primary Keys Dropped** | 842 |
| **Extreme Outliers Quarantined** | 185 |
| **Final Validated Output** | **119,923** |
| **Net Analytical Retention Rate** | **95.57%** |

## How to Run

1. Clone the repository and install dependencies:
```bash
git clone [https://github.com/](https://github.com/)<your-username>/egov-data-cleaning.git
cd egov-data-cleaning
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
