# 🌾 CropShield — Infrastructure Crop Risk Predictor

> An open-source tool that predicts which Indian districts are most at 
> risk of post-harvest crop loss due to infrastructure gaps.
> Built for SDG 9 — Industry, Innovation and Infrastructure.

## 🔴 The Problem

India loses ₹90,000 crore of crops annually — not due to poor farming, 
but due to broken infrastructure. Unpaved roads, absent cold storage, 
and poor connectivity turn good harvests into losses.

## ✅ What CropShield Does

CropShield combines four publicly available government datasets to 
generate a district-level **Infrastructure Crop Risk Index (0–100)**:

|         Factor        | Weight | Source      |
|-----------------------|--------|-------------|
| Road connectivity gap | 35%    | data.gov.in |
| Telecom coverage gap  | 30%    | TRAI        |
| Cold storage gap      | 20%    | NHB         |
| Weather stress index  | 15%    | IMD         |

Districts scoring above 70 are flagged as **critical intervention zones**.

## 🗂️ Repository Structure
cropshield/
├── index.html          ← Live landing page
├── analysis.py         ← Risk scoring script
├── data/
│   └── districts.csv   ← District-level dataset
└── README.md

## 🚀 Run It Yourself

```bash
pip install pandas plotly kaleido
python analysis.py
```

Charts are saved automatically to your working directory.

## 🌏 Live Site

👉 https://akshithprasad.github.io/cropshield

## 🎯 Built For

Future Minds Summit 2026 — Thailand
SDG 9: Industry, Innovation and Infrastructure
