from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
from common import load_data

df = load_data()
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Workforce Drill-down"),
    dcc.RangeSlider(0, 100, 5, value=[10,90], id="salary_pct",
                    marks={i:str(i) for i in range(0,101,20)}),
    html.Div([
        dcc.Graph(id="workforce_scatter"),
        dcc.Graph(id="workforce_box")
    ], style={"display":"grid","gridTemplateColumns":"1fr 1fr"}),
    dcc.Graph(id="country_detail")
], style={"padding":"20px"})

@callback(
    Output("workforce_scatter","figure"), Output("workforce_box","figure"),
    Input("salary_pct","value")
)
def update(percentiles):
    lo, hi = df["Average_Salary"].quantile([percentiles[0]/100, percentiles[1]/100])
    view = df[df["Average_Salary"].between(lo, hi)]
    scatter = px.scatter(view, x="Training_Hours_Per_Employee",
                         y="Employee_Satisfaction", size="Employees",
                         color="Country", hover_name="Company_Name",
                         custom_data=["Country"], title="Training versus satisfaction")
    box = px.box(view, x="Ownership_Type", y="Average_Salary",
                 color="Risk_Rating", title="Compensation distribution")
    return scatter, box

@callback(Output("country_detail","figure"), Input("workforce_scatter","clickData"))
def country_detail(click):
    country = click["points"][0]["customdata"][0] if click else df["Country"].mode()[0]
    view = df[df["Country"] == country].groupby("Industry", as_index=False).agg(
        Employees=("Employees","sum"), Satisfaction=("Employee_Satisfaction","mean")
    )
    return px.bar(view, x="Industry", y="Employees", color="Satisfaction",
                  title=f"Industry workforce profile: {country}")

if __name__ == "__main__":
    app.run(debug=True)
