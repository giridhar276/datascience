from dash import Dash, dcc, html, Input, Output, callback, dash_table
import plotly.express as px
from common import load_data

df = load_data()
risk_map = {"Low":1, "Medium":2, "High":3, "Very High":4}
df["Composite_Risk"] = (
    40 * df["Risk_Rating"].map(risk_map).fillna(2)/4 +
    30 * (1-df["Profit_Margin"].rank(pct=True)) +
    30 * (1-df["Technology_Index"].rank(pct=True))
)

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Risk Analytics Center"),
    dcc.Tabs(id="tab", value="overview", children=[
        dcc.Tab(label="Overview", value="overview"),
        dcc.Tab(label="Risk Matrix", value="matrix"),
        dcc.Tab(label="Watchlist", value="watchlist"),
    ]),
    html.Div(id="tab_content")
], style={"padding":"20px"})

@callback(Output("tab_content","children"), Input("tab","value"))
def render(tab):
    if tab == "overview":
        agg = df.groupby("Risk_Rating", as_index=False).agg(
            Companies=("Company_ID","count"), Revenue=("Annual_Revenue","sum")
        )
        return html.Div([
            dcc.Graph(figure=px.bar(agg, x="Risk_Rating", y="Revenue",
                                    color="Companies", title="Revenue exposure by risk"))
        ])
    if tab == "matrix":
        return dcc.Graph(figure=px.scatter(
            df, x="Composite_Risk", y="Annual_Revenue", size="Employees",
            color="Risk_Rating", hover_name="Company_Name", log_y=True,
            title="Composite-risk matrix"
        ))
    watch = df.nlargest(50, "Composite_Risk")
    cols = ["Company_Name","Country","Industry","Risk_Rating","Composite_Risk",
            "Annual_Revenue","Profit_Margin","Technology_Index"]
    return dash_table.DataTable(
        data=watch[cols].round(2).to_dict("records"),
        columns=[{"name":c,"id":c} for c in cols],
        page_size=15, sort_action="native", filter_action="native",
        style_table={"overflowX":"auto"}
    )

if __name__ == "__main__":
    app.run(debug=True)
