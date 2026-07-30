import streamlit as st
import pandas as pd
from pathlib import Path
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(page_title="Persistent PyGWalker Workspace", layout="wide")
st.title("Persistent PyGWalker Workspace")
st.caption("Build charts visually and save the workspace specification.")

@st.cache_resource
def get_renderer():
    df = pd.read_csv(Path(__file__).parent / "data" / "software_companies_dataset_v2.csv")
    df["Technology_Index"] = df[
        ["Adoption_Rate_AI", "Adoption_Rate_Cloud", "Adoption_Rate_Blockchain"]
    ].mean(axis=1)
    return StreamlitRenderer(
        df,
        spec=str(Path(__file__).parent / "pygwalker_workspace.json"),
        spec_io_mode="rw"
    )

renderer = get_renderer()
renderer.explorer()
