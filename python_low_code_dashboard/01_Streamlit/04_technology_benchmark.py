import streamlit as st
import plotly.express as px
from common import load_data

st.set_page_config(page_title="Technology Benchmark", layout="wide")
df = load_data()
st.title("Technology Adoption Benchmark")

company = st.selectbox("Select a company", sorted(df["Company_Name"].dropna().astype(str).unique().tolist()))
peer_mode = st.radio("Peer group", ["Same industry", "Same country", "Same customer segment"],
                     horizontal=True)
row = df[df["Company_Name"] == company].iloc[0]
if peer_mode == "Same industry":
    peers = df[df["Industry"] == row["Industry"]]
elif peer_mode == "Same country":
    peers = df[df["Country"] == row["Country"]]
else:
    peers = df[df["Customer_Segment"] == row["Customer_Segment"]]

metrics = ["Adoption_Rate_AI", "Adoption_Rate_Cloud", "Adoption_Rate_Blockchain"]
labels = ["AI", "Cloud", "Blockchain"]
comparison = []
for metric, label in zip(metrics, labels):
    comparison.append({"Technology": label, "Selected company": row[metric],
                       "Peer median": peers[metric].median(),
                       "Peer top quartile": peers[metric].quantile(.75)})

import pandas as pd
comp = pd.DataFrame(comparison).melt(id_vars="Technology", var_name="Benchmark",
                                     value_name="Adoption")
st.plotly_chart(px.bar(comp, x="Technology", y="Adoption", color="Benchmark",
                       barmode="group", range_y=[0, 100],
                       title=f"{company}: technology benchmark"),
                use_container_width=True)

st.plotly_chart(px.scatter(peers, x="Technology_Index", y="Profit_Margin",
                           size="Annual_Revenue", color="Primary_Cloud",
                           hover_name="Company_Name",
                           title="Peer technology maturity versus profitability"),
                use_container_width=True)

ranked = peers.assign(
    Tech_Percentile=peers["Technology_Index"].rank(pct=True) * 100,
    Profit_Percentile=peers["Profit_Margin"].rank(pct=True) * 100
)
ranked["Opportunity_Score"] = ranked["Profit_Percentile"] - ranked["Tech_Percentile"]
st.subheader("Peers with profitability ahead of technology maturity")
st.dataframe(ranked.nlargest(15, "Opportunity_Score")[
    ["Company_Name", "Technology_Index", "Profit_Margin",
     "Tech_Percentile", "Profit_Percentile", "Opportunity_Score"]
], use_container_width=True)
