import streamlit as st
import plotly.express as px
import pandas as pd
from common import load_data

st.set_page_config(page_title="Financial Scenario Lab", layout="wide")
df = load_data()
st.title("Financial Scenario and Sensitivity Lab")
st.caption("Model the effect of revenue growth, margin changes and R&D investment.")

industry = st.selectbox("Industry", ["All"] + sorted(df["Industry"].dropna().astype(str).unique().tolist()))
view = df if industry == "All" else df[df["Industry"] == industry]

c1, c2, c3 = st.columns(3)
growth = c1.slider("Revenue growth assumption (%)", -20, 40, 8)
margin_delta = c2.slider("Profit-margin change (points)", -10.0, 10.0, 1.5, 0.5)
rd_delta = c3.slider("R&D spending change (%)", -30, 60, 10)

scenario = view.copy()
scenario["Scenario_Revenue"] = scenario["Annual_Revenue"] * (1 + growth / 100)
scenario["Scenario_Margin"] = (scenario["Profit_Margin"] + margin_delta).clip(-100, 100)
scenario["Scenario_Profit"] = scenario["Scenario_Revenue"] * scenario["Scenario_Margin"] / 100
scenario["Scenario_R&D"] = scenario["R&D_Spending"] * (1 + rd_delta / 100)
scenario["Incremental_Profit"] = scenario["Scenario_Profit"] - scenario["Profit_Estimate"]

b1, b2, b3, b4 = st.columns(4)
b1.metric("Base revenue", f"${view['Annual_Revenue'].sum()/1e9:,.2f}B")
b2.metric("Scenario revenue", f"${scenario['Scenario_Revenue'].sum()/1e9:,.2f}B",
          f"{growth}%")
b3.metric("Incremental profit", f"${scenario['Incremental_Profit'].sum()/1e6:,.1f}M")
b4.metric("Scenario R&D", f"${scenario['Scenario_R&D'].sum()/1e6:,.1f}M")

agg = scenario.groupby("Industry", as_index=False).agg(
    Base_Profit=("Profit_Estimate", "sum"),
    Scenario_Profit=("Scenario_Profit", "sum"),
    Incremental_Profit=("Incremental_Profit", "sum")
)
long = agg.melt(id_vars="Industry", value_vars=["Base_Profit", "Scenario_Profit"],
                var_name="Case", value_name="Profit")
st.plotly_chart(px.bar(long, x="Industry", y="Profit", color="Case", barmode="group",
                       title="Base versus scenario profit"), use_container_width=True)

st.subheader("Companies most affected")
cols = ["Company_Name", "Industry", "Annual_Revenue", "Profit_Margin",
        "Scenario_Revenue", "Scenario_Margin", "Incremental_Profit"]
st.dataframe(scenario[cols].sort_values("Incremental_Profit", ascending=False).head(25),
             use_container_width=True)
st.download_button("Download scenario results", scenario.to_csv(index=False),
                   "financial_scenario_results.csv", "text/csv")
