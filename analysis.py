import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
df = pd.read_csv("data/districts.csv")

# Compute weighted risk score
df["risk_score"] = (
    df["road_gap"] * 0.35 +
    df["connectivity_gap"] * 0.30 +
    df["cold_storage_gap"] * 0.20 +
    df["weather_stress"] * 0.15
) * 100

# Round and sort
df["risk_score"] = df["risk_score"].round(1)
df = df.sort_values("risk_score", ascending=False).reset_index(drop=True)

# Flag critical districts
df["status"] = df["risk_score"].apply(
    lambda x: "Critical" if x >= 80 else "High" if x >= 70 else "Moderate"
)

# Print top 10
print("\n🌾 CropShield — Top 10 Highest Risk Districts\n")
print(df[["district", "state", "risk_score", "status"]].head(10).to_string(index=False))

# Chart 1 — Bar chart of top 20 districts
colors = {"Critical": "#E24B4A", "High": "#F5A623", "Moderate": "#1D9E75"}
fig1 = px.bar(
    df.head(20),
    x="risk_score",
    y="district",
    orientation="h",
    color="status",
    color_discrete_map=colors,
    title="Top 20 Districts by Infrastructure Crop Risk Index",
    labels={"risk_score": "Risk Score (0–100)", "district": "District"},
    text="risk_score"
)
fig1.update_layout(
    plot_bgcolor="#0D1117",
    paper_bgcolor="#0D1117",
    font_color="#E6EDF3",
    title_font_size=16,
    yaxis={"categoryorder": "total ascending"},
    legend_title="Risk Level",
    height=600
)
fig1.update_traces(textposition="outside", textfont_color="#E6EDF3")
fig1.write_image("chart1_top20_districts.png")
print("\n✅ Chart 1 saved: chart1_top20_districts.png")

# Chart 2 — Average factor contribution
factors = {
    "Road gap (35%)": df["road_gap"].mean() * 0.35,
    "Connectivity gap (30%)": df["connectivity_gap"].mean() * 0.30,
    "Cold storage gap (20%)": df["cold_storage_gap"].mean() * 0.20,
    "Weather stress (15%)": df["weather_stress"].mean() * 0.15
}
fig2 = go.Figure(go.Bar(
    x=list(factors.keys()),
    y=[round(v * 100, 1) for v in factors.values()],
    marker_color=["#F5A623", "#1D9E75", "#E24B4A", "#378ADD"],
    text=[f"{round(v*100,1)}" for v in factors.values()],
    textposition="outside"
))
fig2.update_layout(
    title="Average Contribution of Each Infrastructure Factor to Risk Score",
    plot_bgcolor="#0D1117",
    paper_bgcolor="#0D1117",
    font_color="#E6EDF3",
    title_font_size=16,
    yaxis_title="Contribution to Risk Score",
    height=450
)
fig2.write_image("chart2_factor_breakdown.png")
print("✅ Chart 2 saved: chart2_factor_breakdown.png\n")
