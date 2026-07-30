from pathlib import Path
import pandas as pd
import numpy as np

DATA_FILE = Path(__file__).resolve().parent / "data" / "software_companies_dataset_v2.csv"

CATEGORICAL_COLUMNS = [
    "Company_Name", "Industry", "Headquarters_City", "Country",
    "Ownership_Type", "Customer_Segment", "Primary_Cloud", "Risk_Rating"
]

NUMERIC_COLUMNS = [
    "Employees", "Annual_Revenue", "Profit_Margin", "Market_Share",
    "Product_Lines", "R&D_Spending", "Average_Salary",
    "Training_Hours_Per_Employee", "Employee_Satisfaction",
    "Adoption_Rate_AI", "Adoption_Rate_Cloud", "Adoption_Rate_Blockchain",
    "CEO_Tenure_Years", "Year_Founded"
]


def load_data():
    """Load and prepare the software-company dataset for dashboard use.

    Missing categorical values are labelled ``Unknown``. Missing numeric values
    are filled with their column median so Plotly axes, bubble sizes, KPI
    calculations and sorting operations remain valid.
    """
    df = pd.read_csv(DATA_FILE)

    for col in ["Incorporation_Date", "Last_Funding_Date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    for col in CATEGORICAL_COLUMNS:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown").astype(str).str.strip()
            df.loc[df[col].eq(""), col] = "Unknown"

    for col in NUMERIC_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            median = df[col].median()
            df[col] = df[col].fillna(0 if pd.isna(median) else median)

    # Plotly logarithmic axes require strictly positive values.
    df["Annual_Revenue"] = df["Annual_Revenue"].clip(lower=1)
    df["Employees"] = df["Employees"].clip(lower=1)

    df["Company_Age"] = (pd.Timestamp.today().year - df["Year_Founded"]).clip(lower=0)
    df["Revenue_Per_Employee"] = df["Annual_Revenue"] / df["Employees"].replace(0, np.nan)
    df["R&D_Intensity"] = 100 * df["R&D_Spending"] / df["Annual_Revenue"].replace(0, np.nan)
    df["Technology_Index"] = df[
        ["Adoption_Rate_AI", "Adoption_Rate_Cloud", "Adoption_Rate_Blockchain"]
    ].mean(axis=1)
    df["Profit_Estimate"] = df["Annual_Revenue"] * df["Profit_Margin"] / 100
    return df


def filtered(df, countries=None, industries=None, risks=None):
    out = df.copy()
    if countries:
        out = out[out["Country"].isin(countries)]
    if industries:
        out = out[out["Industry"].isin(industries)]
    if risks:
        out = out[out["Risk_Rating"].isin(risks)]
    return out
