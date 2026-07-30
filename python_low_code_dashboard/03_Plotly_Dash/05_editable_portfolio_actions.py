from dash import Dash, dcc, html, Input, Output, State, callback, dash_table
from common import load_data

df = load_data().nlargest(100, "Annual_Revenue").copy()
df["Action"] = "Review"
df["Owner"] = ""
df["Priority"] = df["Risk_Rating"].map({"High":"Critical","Medium":"Medium","Low":"Low"})

cols = ["Company_Name","Country","Industry","Risk_Rating","Annual_Revenue",
        "Profit_Margin","Technology_Index","Priority","Owner","Action"]
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Editable Portfolio Action Register"),
    html.P("Edit Priority, Owner and Action directly in the table."),
    dash_table.DataTable(
        id="action_table", data=df[cols].round(2).to_dict("records"),
        columns=[{"name":c,"id":c,"editable":c in ["Priority","Owner","Action"]}
                 for c in cols],
        page_size=15, sort_action="native", filter_action="native",
        export_format="csv", style_table={"overflowX":"auto"}
    ),
    html.Button("Summarize actions", id="summarize"),
    html.Div(id="action_summary", style={"padding":"15px"})
], style={"padding":"20px"})

@callback(Output("action_summary","children"),
          Input("summarize","n_clicks"), State("action_table","data"),
          prevent_initial_call=True)
def summarize(_, records):
    counts = {}
    for row in records:
        key = row.get("Action") or "Unspecified"
        counts[key] = counts.get(key, 0) + 1
    return html.Ul([html.Li(f"{action}: {count}") for action, count in sorted(counts.items())])

if __name__ == "__main__":
    app.run(debug=True)
