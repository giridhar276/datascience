from dash import Dash, dcc, html, Input, Output, callback, dash_table
import plotly.express as px
import plotly.graph_objects as go
from common import load_data

df = load_data()
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Revenue and Margin Scenario Planner"),
    html.Label("Revenue growth assumption"),
    dcc.Slider(-20, 40, 2, value=8, marks={i:f"{i}%" for i in range(-20,41,10)}, id="growth"),
    html.Label("Margin change"),
    dcc.Slider(-10, 10, .5, value=1.5, marks={i:str(i) for i in range(-10,11,5)}, id="margin"),
    dcc.Dropdown(options=["All"] + sorted(df["Industry"].dropna().astype(str).unique().tolist()), value="All", id="industry"),
    html.Div(id="summary", style={"padding":"16px 0"}),
    dcc.Graph(id="scenario_chart"),
    dash_table.DataTable(id="scenario_table", page_size=12, sort_action="native",
                         style_table={"overflowX":"auto"})
], style={"padding":"20px"})

@callback(
    Output("summary","children"), Output("scenario_chart","figure"),
    Output("scenario_table","data"), Output("scenario_table","columns"),
    Input("growth","value"), Input("margin","value"), Input("industry","value")
)
def update(growth, margin, industry):
    view = df.copy() if industry == "All" else df[df["Industry"] == industry].copy()
    view["Scenario_Revenue"] = view["Annual_Revenue"] * (1 + growth/100)
    view["Scenario_Margin"] = view["Profit_Margin"] + margin
    view["Scenario_Profit"] = view["Scenario_Revenue"] * view["Scenario_Margin"]/100
    view["Incremental_Profit"] = view["Scenario_Profit"] - view["Profit_Estimate"]
    summary = html.H3(f"Incremental portfolio profit: ${view['Incremental_Profit'].sum()/1e6:,.1f}M")
    impacts = view.nlargest(20, "Incremental_Profit").sort_values("Incremental_Profit")
    chart = go.Figure(go.Waterfall(
        x=impacts["Company_Name"],
        y=impacts["Incremental_Profit"],
        measure=["relative"] * len(impacts)
    ))
    chart.update_layout(title="Largest positive scenario impacts", showlegend=False)
    cols = ["Company_Name","Industry","Annual_Revenue","Profit_Margin",
            "Scenario_Revenue","Scenario_Margin","Incremental_Profit"]
    table = view[cols].sort_values("Incremental_Profit", ascending=False).round(2)
    return summary, chart, table.to_dict("records"), [{"name":c,"id":c} for c in cols]

if __name__ == "__main__":
    app.run(debug=True)
