import streamlit as st
import plotly.express as px
from common import load_data

st.set_page_config(page_title="Workforce Intelligence", layout="wide")
df = load_data()
st.title("Workforce Intelligence Dashboard")

segment = st.multiselect("Customer segments", sorted(df["Customer_Segment"].dropna().astype(str).unique().tolist()))
view = df if not segment else df[df["Customer_Segment"].isin(segment)]

salary_q = st.slider("Average salary percentile range", 0, 100, (10, 90))
low, high = view["Average_Salary"].quantile([salary_q[0]/100, salary_q[1]/100])
view = view[view["Average_Salary"].between(low, high)]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Employees", f"{view['Employees'].sum():,.0f}")
c2.metric("Avg. satisfaction", f"{view['Employee_Satisfaction'].mean():.2f}/5")
c3.metric("Training hours", f"{view['Training_Hours_Per_Employee'].mean():.1f}")
c4.metric("Revenue/employee", f"${view['Revenue_Per_Employee'].mean():,.0f}")

left, right = st.columns(2)
left.plotly_chart(px.scatter(view, x="Training_Hours_Per_Employee",
                             y="Employee_Satisfaction", size="Employees",
                             color="Industry", hover_name="Company_Name",
                             trendline="ols",
                             title="Training investment versus satisfaction"),
                  use_container_width=True)
right.plotly_chart(px.box(view, x="Ownership_Type", y="Average_Salary",
                          color="Risk_Rating", points=False,
                          title="Salary distribution by ownership and risk"),
                   use_container_width=True)

heat = view.pivot_table(index="Industry", columns="Country",
                        values="Employee_Satisfaction", aggfunc="mean")
st.plotly_chart(px.imshow(heat, text_auto=".2f", aspect="auto",
                          title="Employee satisfaction heatmap"),
                use_container_width=True)

view["Talent_Alert"] = (
    (view["Employee_Satisfaction"] < view["Employee_Satisfaction"].quantile(.25)) &
    (view["Training_Hours_Per_Employee"] < view["Training_Hours_Per_Employee"].median())
)
st.subheader("Potential talent-risk watchlist")
st.dataframe(view.loc[view["Talent_Alert"],
    ["Company_Name", "Country", "Industry", "Employees",
     "Employee_Satisfaction", "Training_Hours_Per_Employee", "Average_Salary"]
].sort_values("Employees", ascending=False), use_container_width=True)
