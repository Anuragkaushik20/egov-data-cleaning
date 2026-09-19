"""
eda_analysis.py
Exploratory Data Analysis & Visualization Engine for Digital Public Services.
Domain: Yuva Intern / NSDC Data Analytics Internship (Week 3 Task).
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Path Configuration
PROCESSED_DATA_PATH = "data/processed/cleaned_egov_services.csv"
OUTPUT_DIR = "data/processed/visualizations"
STATS_SUMMARY_PATH = "data/processed/eda_summary_statistics.csv"

def load_data(filepath: str) -> pd.DataFrame:
    """Loads processed e-governance dataset."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"[ERROR] Cleaned dataset not found at '{filepath}'. Run 'clean_data.py' first.")
    df = pd.read_csv(filepath)
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    return df

def generate_summary_statistics(df: pd.DataFrame):
    """Computes and exports formal descriptive statistics."""
    os.makedirs(os.path.dirname(STATS_SUMMARY_PATH), exist_ok=True)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    summary_df = pd.DataFrame({
        "Mean": df[numeric_cols].mean(),
        "Median": df[numeric_cols].median(),
        "Std_Dev": df[numeric_cols].std(),
        "IQR": df[numeric_cols].quantile(0.75) - df[numeric_cols].quantile(0.25),
        "Skewness": df[numeric_cols].skew(),
        "95th_Percentile": df[numeric_cols].quantile(0.95)
    })
    summary_df.to_csv(STATS_SUMMARY_PATH)
    print(f"[EDA] Summary statistics saved to: {STATS_SUMMARY_PATH}")

def run_hypothesis_tests(df: pd.DataFrame):
    """Executes inferential hypothesis tests (ANOVA & Pearson Correlation)."""
    print("\n" + "="*50)
    print("HYPOTHESIS TESTING RESULTS")
    print("="*50)
    
    # Test 1: Departmental Latency Variance (ANOVA)
    dept_groups = [group["latency_days"].values for _, group in df.groupby("department_name")]
    f_stat, p_val_anova = stats.f_oneway(*dept_groups)
    print(f"H2 (ANOVA Test - Latency across Depts): F-statistic = {f_stat:.2f}, p-value = {p_val_anova:.4e}")

def create_visualizations(df: pd.DataFrame):
    """Generates four distinct, publication-grade analytical visualizations."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    sns.set_theme(style="whitegrid")
    
    # Viz 1: State Per-Capita Transactions vs. Teledensity
    plt.figure(figsize=(10, 5))
    state_agg = df.groupby("state_name")["transaction_count"].mean().sort_values(ascending=False).head(10)
    ax = sns.barplot(x=state_agg.values, y=state_agg.index, palette="Blues_r")
    plt.title("Viz 1: Top 10 States by Daily Transaction Volume", fontsize=12, fontweight="bold")
    plt.xlabel("Average Daily Transactions")
    plt.ylabel("State / UT")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "viz1_state_volume.png"), dpi=300)
    plt.close()

    # Viz 2: Department Latency Box Plot
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df, x="department_name", y="latency_days", palette="Set2")
    plt.axhline(y=7, color="red", linestyle="--", label="Standard SLA Target (7 Days)")
    plt.title("Viz 2: Processing Latency Variance Across Departments", fontsize=12, fontweight="bold")
    plt.xlabel("Government Department")
    plt.ylabel("Processing Duration (Days)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "viz2_department_latency_boxplot.png"), dpi=300)
    plt.close()

    # Viz 3: Time-Series Volume & SLA Breach Trend
    plt.figure(figsize=(12, 5))
    daily_trend = df.groupby("transaction_date")["transaction_count"].sum()
    plt.plot(daily_trend.index, daily_trend.values, color="#1f77b4", linewidth=2, label="Daily Transactions")
    plt.title("Viz 3: Daily E-Governance Transaction Volume Surge Trend", fontsize=12, fontweight="bold")
    plt.xlabel("Date")
    plt.ylabel("Total Daily Transactions")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "viz3_timeseries_surge.png"), dpi=300)
    plt.close()

    # Viz 4: Multivariate Correlation Heatmap
    plt.figure(figsize=(8, 6))
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Viz 4: Multivariate KPI Correlation Matrix", fontsize=12, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "viz4_correlation_heatmap.png"), dpi=300)
    plt.close()
    print(f"[EDA] Visualizations successfully saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    data = load_data(PROCESSED_DATA_PATH)
    generate_summary_statistics(data)
    run_hypothesis_tests(data)
    create_visualizations(data)