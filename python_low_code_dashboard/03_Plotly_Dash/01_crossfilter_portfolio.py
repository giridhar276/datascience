from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
from common import load_data

df = load_data()
app = Dash(__name__)
app.title = "Crossfilter Portfolio"

app.layout = html.Div([
    html.H1("Crossfilter Company Portfolio"),
    html.Div([
        dcc.Dropdown(options=sorted(df["Country"].dropna().astype(str).unique().tolist()), multi=True,
                     placeholder="Filter countries", id="country"),
        dcc.Dropdown(options=sorted(df["Industry"].dropna().astype(str).unique().tolist()), multi=True,
                     placeholder="Filter industries", id="industry"),
    ], style={"display":"grid","gridTemplateColumns":"1fr 1fr","gap":"12px"}),
    html.Div(id="kpis"),
    html.Div([
        dcc.Graph(id="scatter"),
        dcc.Graph(id="bars")
    ], style={"display":"grid","gridTemplateColumns":"1fr 1fr"}),
    html.H3("Click a company in the scatter plot"),
    html.Pre(id="details")
], style={"padding":"20px"})

@callback(
    Output("scatter","figure"), Output("bars","figure"), Output("kpis","children"),
    Input("country","value"), Input("industry","value")
)
def update(countries, industries):
    view = df.copy()
    if countries: view = view[view["Country"].isin(countries)]
    if industries: view = view[view["Industry"].isin(industries)]
    scatter = px.scatter(view, x="Annual_Revenue", y="Profit_Margin",
                         size="Employees", color="Risk_Rating",
                         hover_name="Company_Name", custom_data=["Company_ID"],
                         log_x=True, title="Revenue versus margin")
    agg = view.groupby("Industry", as_index=False)["Profit_Estimate"].sum()
    bars = px.bar(agg.sort_values("Profit_Estimate"), x="Profit_Estimate",
                  y="Industry", orientation="h", title="Estimated profit by industry")
    kpis = html.Div([
        html.B(f"Companies: {len(view):,}"), html.Span(" | "),
        html.B(f"Revenue: ${view['Annual_Revenue'].sum()/1e9:,.2f}B"), html.Span(" | "),
        html.B(f"Employees: {view['Employees'].sum():,.0f}")
    ], style={"padding":"14px 0"})
    return scatter, bars, kpis

@callback(Output("details","children"), Input("scatter","clickData"))
def show_details(click):
    if not click:
        return "Select a point to inspect a company."
    cid = click["points"][0]["customdata"][0]
    row = df[df["Company_ID"] == cid].iloc[0]
    return "\n".join([
        f"Company: {row['Company_Name']}",
        f"Industry: {row['Industry']}",
        f"Country: {row['Country']}",
        f"Revenue: ${row['Annual_Revenue']:,.0f}",
        f"Profit margin: {row['Profit_Margin']:.2f}%",
        f"Technology index: {row['Technology_Index']:.1f}"
    ])

if __name__ == "__main__":
    app.run(debug=True)
